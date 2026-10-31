#Requires -Version 7.0
[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$presetRoot = Split-Path -Parent $PSScriptRoot
$coordinator = Join-Path $presetRoot 'scripts/orchestrate-parallel-autonomous-runs.ps1'
$fixtureWorker = Join-Path $PSScriptRoot 'fixture-worker.ps1'
$tempRoot = Join-Path ([IO.Path]::GetTempPath()) "parallel-autonomous-tests-$([guid]::NewGuid())"
[void](New-Item -ItemType Directory -Path $tempRoot)

function Assert-Test {
    param([bool] $Condition, [string] $Message)
    if (-not $Condition) {
        throw $Message
    }
}

function Initialize-TestRepository {
    [Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseShouldProcessForStateChangingFunctions', '', Justification = 'Creates only disposable fixture repositories below the test temp root.')]
    param([string] $Name)
    $path = Join-Path $tempRoot $Name
    [void](New-Item -ItemType Directory -Path $path)
    & git -C $path init -b main | Out-Null
    & git -C $path config user.name 'Parallel Fixture'
    & git -C $path config user.email 'parallel-fixture@example.invalid'
    "# $Name" | Set-Content -LiteralPath (Join-Path $path 'README.md') -Encoding utf8NoBOM
    & git -C $path add README.md
    & git -C $path commit -m 'test: baseline' | Out-Null
    return $path
}

function Get-TestWorker {
    param(
        [string] $Id,
        [string] $Repository,
        [string[]] $DependsOn = @()
    )
    return [ordered]@{
        workerId = $Id
        runId = [guid]::NewGuid().ToString()
        repository = $Repository
        baseRef = 'main'
        baseWorkerId = $null
        branch = "parallel/test/$([guid]::NewGuid().ToString('N'))/$Id"
        featureInput = 'README.md'
        dependsOn = @($DependsOn)
        handoffs = @()
    }
}

function Get-TestCampaign {
    param(
        [string] $Name,
        [string] $Topology,
        [object[]] $Workers,
        [string] $DeliveryMode = 'LocalImplementation'
    )
    return [ordered]@{
        schemaVersion = '1.0'
        campaignId = [guid]::NewGuid().ToString()
        name = $Name
        topology = $Topology
        deliveryMode = $DeliveryMode
        maxConcurrency = 3
        runnerProfile = if ($DeliveryMode -eq 'MergeAndSync') { 'ready' } else { 'fixture' }
        requireAutonomousPreset = $false
        operatorInstructions = 'Fixture operator instruction.'
        workers = @($Workers)
        consolidation = [ordered]@{
            allReadyBarrier = $true
            mergeOrder = @($Workers | ForEach-Object { $_.workerId })
            humanSelectionRequired = $Topology -eq 'AlternativeSolutions'
            mergeProfile = 'fixture-merge'
        }
    }
}

function Write-Data {
    param([string] $Path, $Value)
    $Value | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $Path -Encoding utf8NoBOM
}

function Invoke-Campaign {
    param(
        [hashtable] $Campaign,
        [string] $Label
    )
    $caseRoot = Join-Path $tempRoot $Label
    [void](New-Item -ItemType Directory -Path $caseRoot)
    $manifest = Join-Path $caseRoot 'campaign.json'
    $state = Join-Path $caseRoot 'state.json'
    $runtime = Join-Path $caseRoot 'runtime'
    Write-Data $manifest $Campaign
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $manifest -RunnerConfig $script:runnerConfig | Out-Null
    Assert-Test ($LASTEXITCODE -eq 0) "$Label validation failed"
    & pwsh -NoProfile -File $coordinator -Action Start -Manifest $manifest -RunnerConfig $script:runnerConfig -State $state -RuntimeRoot $runtime | Out-Null
    Assert-Test ($LASTEXITCODE -eq 0) "$Label start failed"
    $stateData = Get-Content -LiteralPath $state -Raw | ConvertFrom-Json
    Assert-Test ($stateData.maximumObservedConcurrency -le 3) "$Label exceeded concurrency"
    return @{
        Manifest = $manifest
        State = $state
        Runtime = $runtime
        Data = $stateData
    }
}

try {
    $script:runnerConfig = Join-Path $tempRoot 'runners.json'
    $runnerData = [ordered]@{
        schemaVersion = '1.0'
        profiles = [ordered]@{
            fixture = [ordered]@{
                executable = 'pwsh'
                arguments = @(
                    '-NoProfile', '-File', $fixtureWorker,
                    '-CampaignId', '{campaignId}',
                    '-WorkerId', '{workerId}',
                    '-RunId', '{runId}',
                    '-Worktree', '{worktree}',
                    '-ResultFile', '{resultFile}',
                    '-Mode', 'Completed',
                    '-HandoffsJson', '{handoffsJson}',
                    '-DelayMilliseconds', '250'
                )
            }
            ready = [ordered]@{
                executable = 'pwsh'
                arguments = @(
                    '-NoProfile', '-File', $fixtureWorker,
                    '-CampaignId', '{campaignId}',
                    '-WorkerId', '{workerId}',
                    '-RunId', '{runId}',
                    '-Worktree', '{worktree}',
                    '-ResultFile', '{resultFile}',
                    '-Mode', 'ReadyForMerge',
                    '-HandoffsJson', '{handoffsJson}',
                    '-DelayMilliseconds', '150'
                )
            }
            slow = [ordered]@{
                executable = 'pwsh'
                arguments = @(
                    '-NoProfile', '-File', $fixtureWorker,
                    '-CampaignId', '{campaignId}',
                    '-WorkerId', '{workerId}',
                    '-RunId', '{runId}',
                    '-Worktree', '{worktree}',
                    '-ResultFile', '{resultFile}',
                    '-Mode', 'Completed',
                    '-HandoffsJson', '{handoffsJson}',
                    '-DelayMilliseconds', '1200'
                )
            }
        }
        mergeProfiles = [ordered]@{
            'fixture-merge' = [ordered]@{
                executable = 'pwsh'
                arguments = @('-NoProfile', '-Command', 'exit 0')
            }
        }
    }
    Write-Data $script:runnerConfig $runnerData

    $replicatedWorkers = 1..3 | ForEach-Object {
        Get-TestWorker "replicated-0$_" (Initialize-TestRepository "replicated-repo-0$_")
    }
    $replicated = Invoke-Campaign (Get-TestCampaign 'replicated' 'ReplicatedTargets' $replicatedWorkers) 'replicated'
    Assert-Test ($replicated.Data.status -eq 'Completed') "ReplicatedTargets did not complete: $($replicated.Data.workers | ConvertTo-Json -Compress -Depth 10)"
    Assert-Test ($replicated.Data.maximumObservedConcurrency -ge 2) 'ReplicatedTargets did not prove concurrency'
    $replicatedPrompt = Get-Content -LiteralPath (Join-Path $replicated.Runtime 'prompts/replicated-01.txt') -Raw
    Assert-Test ($replicatedPrompt.Contains('Fixture operator instruction.')) 'Campaign operator instructions were not routed to the worker'
    Assert-Test ($replicatedPrompt.Contains("Remain on the assigned branch '")) 'Assigned branch boundary was not routed to the worker'

    $runnerData.profiles.flood = [ordered]@{
        executable = 'pwsh'
        arguments = @(
            '-NoProfile', '-File', $fixtureWorker,
            '-CampaignId', '{campaignId}', '-WorkerId', '{workerId}',
            '-RunId', '{runId}', '-Worktree', '{worktree}',
            '-ResultFile', '{resultFile}', '-Mode', 'Flood'
        )
    }
    Write-Data $script:runnerConfig $runnerData
    $floodCampaign = Get-TestCampaign 'bounded-output' 'ReplicatedTargets' @(
        (Get-TestWorker 'flood-a' (Initialize-TestRepository 'flood-repo'))
    )
    $floodCampaign.runnerProfile = 'flood'
    $flood = Invoke-Campaign $floodCampaign 'bounded-output'
    Assert-Test ($flood.Data.status -eq 'Failed') 'Output flood did not fail the campaign'
    $floodLog = Join-Path $flood.Runtime 'logs/flood-a.out.log'
    Assert-Test ((Get-Item -LiteralPath $floodLog).Length -le 16777216) 'Output log exceeded its byte limit'

    $faultCampaign = Get-TestCampaign 'log-failure' 'ReplicatedTargets' @(
        (Get-TestWorker 'fault-a' (Initialize-TestRepository 'fault-repo'))
    )
    $faultCampaign.runnerProfile = 'slow'
    $faultRoot = Join-Path $tempRoot 'log-failure'
    $faultRuntime = Join-Path $faultRoot 'runtime'
    [void](New-Item -ItemType Directory -Path (Join-Path $faultRuntime 'logs/fault-a.out.log') -Force)
    $faultManifest = Join-Path $faultRoot 'campaign.json'
    $faultState = Join-Path $faultRoot 'state.json'
    Write-Data $faultManifest $faultCampaign
    $faultStartedAt = [DateTime]::UtcNow
    & pwsh -NoProfile -File $coordinator -Action Start -Manifest $faultManifest `
        -RunnerConfig $script:runnerConfig -State $faultState -RuntimeRoot $faultRuntime | Out-Null
    Assert-Test ($LASTEXITCODE -eq 0) 'Log I/O failure aborted the coordinator'
    Assert-Test (([DateTime]::UtcNow - $faultStartedAt).TotalSeconds -lt 10) `
        'Log I/O failure did not stop the worker promptly'
    $faultData = Get-Content -LiteralPath $faultState -Raw | ConvertFrom-Json
    Assert-Test ($faultData.status -eq 'Failed') 'Log I/O failure did not fail the campaign'

    $runnerData.profiles.retained = [ordered]@{
        executable = 'pwsh'
        arguments = @(
            '-NoProfile', '-File', $fixtureWorker,
            '-CampaignId', '{campaignId}', '-WorkerId', '{workerId}',
            '-RunId', '{runId}', '-Worktree', '{worktree}',
            '-ResultFile', '{resultFile}', '-Mode', 'RetainedPipe'
        )
    }
    Write-Data $script:runnerConfig $runnerData
    $retainedCampaign = Get-TestCampaign 'retained-pipe' 'ReplicatedTargets' @(
        (Get-TestWorker 'retained-a' (Initialize-TestRepository 'retained-repo'))
    )
    $retainedCampaign.runnerProfile = 'retained'
    $retainedStartedAt = [DateTime]::UtcNow
    $retained = Invoke-Campaign $retainedCampaign 'retained-pipe'
    Assert-Test (([DateTime]::UtcNow - $retainedStartedAt).TotalSeconds -lt 12) `
        'Retained output pipe blocked the coordinator'
    Assert-Test ($retained.Data.status -eq 'Failed') 'Retained output pipe did not fail the campaign'

    $runnerData.profiles.strict = [ordered]@{
        executable = 'pwsh'
        arguments = @(
            '-NoProfile', '-File', $fixtureWorker,
            '-CampaignId', '{campaignId}', '-WorkerId', '{workerId}',
            '-RunId', '{runId}', '-Worktree', '{worktree}',
            '-ResultFile', '{resultFile}'
        )
        agentFamily = 'Fixture'
        routingRole = 'script-only'
        model = 'fixture'
        reasoningEffort = 'low'
        preflight = [ordered]@{
            executable = 'pwsh'
            arguments = @('-NoProfile', '-Command', 'Start-Sleep -Seconds 30')
            timeoutSeconds = 1
        }
    }
    Write-Data $script:runnerConfig $runnerData
    $strictCampaign = Get-TestCampaign 'bounded-preflight' 'ReplicatedTargets' @(
        (Get-TestWorker 'strict-a' (Initialize-TestRepository 'strict-repo'))
    )
    $strictCampaign.runnerProfile = 'strict'
    $strictCampaign.routingRole = 'script-only'
    $strictCampaign.fallbackPolicy = 'fail-closed'
    $strictRoot = Join-Path $tempRoot 'bounded-preflight'
    [void](New-Item -ItemType Directory -Path $strictRoot)
    $strictManifest = Join-Path $strictRoot 'campaign.json'
    Write-Data $strictManifest $strictCampaign
    $strictStartedAt = [DateTime]::UtcNow
    & pwsh -NoProfile -File $coordinator -Action Start -Manifest $strictManifest `
        -RunnerConfig $script:runnerConfig -State (Join-Path $strictRoot 'state.json') `
        -RuntimeRoot (Join-Path $strictRoot 'runtime') 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Hanging profile preflight was accepted'
    Assert-Test (([DateTime]::UtcNow - $strictStartedAt).TotalSeconds -lt 10) `
        'Profile command timeout did not stop promptly'

    $runnerData.profiles.strict.preflight.arguments = @(
        '-NoProfile', '-Command', '[Console]::Out.Write(("x" * 1100000))'
    )
    Write-Data $script:runnerConfig $runnerData
    $strictFloodRoot = Join-Path $tempRoot 'bounded-preflight-output'
    [void](New-Item -ItemType Directory -Path $strictFloodRoot)
    $strictFloodManifest = Join-Path $strictFloodRoot 'campaign.json'
    $strictCampaign.campaignId = [guid]::NewGuid().ToString()
    Write-Data $strictFloodManifest $strictCampaign
    & pwsh -NoProfile -File $coordinator -Action Start -Manifest $strictFloodManifest `
        -RunnerConfig $script:runnerConfig -State (Join-Path $strictFloodRoot 'state.json') `
        -RuntimeRoot (Join-Path $strictFloodRoot 'runtime') 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Noisy profile preflight was accepted'

    $independentRepo = Initialize-TestRepository 'independent-repo'
    $independentWorkers = 1..3 | ForEach-Object { Get-TestWorker "independent-0$_" $independentRepo }
    $independent = Invoke-Campaign (Get-TestCampaign 'independent' 'IndependentFeatures' $independentWorkers) 'independent'
    Assert-Test ($independent.Data.status -eq 'Completed') 'IndependentFeatures did not complete'
    Assert-Test ((@($independent.Data.workers.worktree | Sort-Object -Unique)).Count -eq 3) 'Independent worktrees are not unique'

    $alternativeRepo = Initialize-TestRepository 'alternative-repo'
    $alternativeWorkers = 1..3 | ForEach-Object { Get-TestWorker "alternative-0$_" $alternativeRepo }
    $alternative = Invoke-Campaign (Get-TestCampaign 'alternatives' 'AlternativeSolutions' $alternativeWorkers) 'alternatives'
    Assert-Test ($alternative.Data.status -eq 'AwaitingSelection') 'AlternativeSolutions did not await selection'
    & pwsh -NoProfile -File $coordinator -Action Consolidate -Manifest $alternative.Manifest -RunnerConfig $script:runnerConfig -State $alternative.State -RuntimeRoot $alternative.Runtime 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Alternative consolidation accepted missing human selection'
    & pwsh -NoProfile -File $coordinator -Action Consolidate -Manifest $alternative.Manifest -RunnerConfig $script:runnerConfig -State $alternative.State -RuntimeRoot $alternative.Runtime -SelectedWorker 'alternative-02' | Out-Null
    Assert-Test ($LASTEXITCODE -eq 0) 'Selected alternative consolidation failed'

    $pipelineRepo = Initialize-TestRepository 'pipeline-repo'
    $pipelineWorkers = @(
        (Get-TestWorker 'pipeline-a' $pipelineRepo),
        (Get-TestWorker 'pipeline-b' $pipelineRepo @('pipeline-a')),
        (Get-TestWorker 'pipeline-c' $pipelineRepo @('pipeline-a')),
        (Get-TestWorker 'pipeline-d' $pipelineRepo @('pipeline-b', 'pipeline-c'))
    )
    $pipelineWorkers[0].handoffs = @(
        [ordered]@{ consumerWorkerId = 'pipeline-b'; path = 'handoffs/a-to-b.json' },
        [ordered]@{ consumerWorkerId = 'pipeline-c'; path = 'handoffs/a-to-c.json' }
    )
    $pipelineWorkers[1].handoffs = @(
        [ordered]@{ consumerWorkerId = 'pipeline-d'; path = 'handoffs/b-to-d.json' }
    )
    $pipelineWorkers[2].handoffs = @(
        [ordered]@{ consumerWorkerId = 'pipeline-d'; path = 'handoffs/c-to-d.json' }
    )
    $pipelineWorkers[1].baseWorkerId = 'pipeline-a'
    $pipelineWorkers[2].baseWorkerId = 'pipeline-a'
    $pipelineWorkers[3].baseWorkerId = 'pipeline-b'
    $pipeline = Invoke-Campaign (Get-TestCampaign 'pipeline' 'Pipeline' $pipelineWorkers) 'pipeline'
    Assert-Test ($pipeline.Data.status -eq 'Completed') 'Pipeline did not complete'
    Assert-Test ($pipeline.Data.maximumObservedConcurrency -eq 2) 'Pipeline did not execute the B/C wave concurrently'
    $pipelineStates = @{}
    foreach ($workerState in $pipeline.Data.workers) {
        $pipelineStates[$workerState.workerId] = $workerState
    }
    & git -C $pipelineRepo merge-base --is-ancestor $pipelineStates['pipeline-a'].headSha $pipelineStates['pipeline-b'].headSha
    Assert-Test ($LASTEXITCODE -eq 0) 'pipeline-b did not inherit pipeline-a head'
    & git -C $pipelineRepo merge-base --is-ancestor $pipelineStates['pipeline-a'].headSha $pipelineStates['pipeline-c'].headSha
    Assert-Test ($LASTEXITCODE -eq 0) 'pipeline-c did not inherit pipeline-a head'
    & git -C $pipelineRepo merge-base --is-ancestor $pipelineStates['pipeline-b'].headSha $pipelineStates['pipeline-d'].headSha
    Assert-Test ($LASTEXITCODE -eq 0) 'pipeline-d did not inherit pipeline-b head'

    $invalid = Get-TestCampaign 'cycle' 'Pipeline' @(
        (Get-TestWorker 'cycle-a' $pipelineRepo @('cycle-b')),
        (Get-TestWorker 'cycle-b' $pipelineRepo @('cycle-a'))
    )
    $invalid.workers[0].handoffs = @([ordered]@{ consumerWorkerId = 'cycle-b'; path = 'handoffs/a-b.json' })
    $invalid.workers[1].handoffs = @([ordered]@{ consumerWorkerId = 'cycle-a'; path = 'handoffs/b-a.json' })
    $invalidPath = Join-Path $tempRoot 'invalid-cycle.json'
    Write-Data $invalidPath $invalid
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $invalidPath -RunnerConfig $script:runnerConfig 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'DAG cycle was accepted'

    $unsafeWorker = Get-TestCampaign 'unsafe-worker' 'ReplicatedTargets' @(
        (Get-TestWorker '../outside' $pipelineRepo)
    )
    $unsafeWorkerPath = Join-Path $tempRoot 'unsafe-worker.json'
    Write-Data $unsafeWorkerPath $unsafeWorker
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $unsafeWorkerPath -RunnerConfig $script:runnerConfig 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Traversal workerId was accepted'

    $invalidBaseWorker = Get-TestCampaign 'invalid-base-worker' 'Pipeline' @(
        (Get-TestWorker 'base-a' $pipelineRepo),
        (Get-TestWorker 'base-b' $pipelineRepo)
    )
    $invalidBaseWorker.workers[1].baseWorkerId = 'base-a'
    $invalidBaseWorkerPath = Join-Path $tempRoot 'invalid-base-worker.json'
    Write-Data $invalidBaseWorkerPath $invalidBaseWorker
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $invalidBaseWorkerPath -RunnerConfig $script:runnerConfig 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'baseWorkerId outside dependsOn was accepted'

    $invalidConcurrency = Get-TestCampaign 'too-wide' 'ReplicatedTargets' @(
        (Get-TestWorker 'wide-a' $pipelineRepo)
    )
    $invalidConcurrency.maxConcurrency = 4
    $invalidConcurrencyPath = Join-Path $tempRoot 'invalid-concurrency.json'
    Write-Data $invalidConcurrencyPath $invalidConcurrency
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $invalidConcurrencyPath -RunnerConfig $script:runnerConfig 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Concurrency above three was accepted'

    $invalidFallback = Get-TestCampaign 'missing-campaign-fallback' 'ReplicatedTargets' @(
        (Get-TestWorker 'fallback-a' $pipelineRepo)
    )
    $invalidFallback.runnerProfile = 'missing-profile'
    $invalidFallback.workers[0].runnerProfile = 'fixture'
    $invalidFallbackPath = Join-Path $tempRoot 'invalid-campaign-fallback.json'
    Write-Data $invalidFallbackPath $invalidFallback
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $invalidFallbackPath `
        -RunnerConfig $script:runnerConfig 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Missing campaign fallback profile was accepted'

    $legacyMergeCampaign = Get-TestCampaign 'legacy-merge-read' 'ReplicatedTargets' @(
        (Get-TestWorker 'legacy-merge-a' $pipelineRepo)
    ) -DeliveryMode 'MergeAndSync'
    [void]$legacyMergeCampaign.consolidation.Remove('mergeProfile')
    $legacyMergePath = Join-Path $tempRoot 'legacy-merge-read.json'
    Write-Data $legacyMergePath $legacyMergeCampaign
    & pwsh -NoProfile -File $coordinator -Action Validate -Manifest $legacyMergePath -RunnerConfig $script:runnerConfig | Out-Null
    Assert-Test ($LASTEXITCODE -eq 0) 'Schema 1.0 MergeAndSync manifest without mergeProfile was not readable'

    $stopRepo = Initialize-TestRepository 'stop-resume-repo'
    $stopWorkers = 1..3 | ForEach-Object { Get-TestWorker "stop-0$_" $stopRepo }
    $stopCampaign = Get-TestCampaign 'stop-resume' 'IndependentFeatures' $stopWorkers
    $stopCampaign.runnerProfile = 'slow'
    $stopCampaign.maxConcurrency = 1
    $stopRoot = Join-Path $tempRoot 'stop-resume'
    [void](New-Item -ItemType Directory -Path $stopRoot)
    $stopManifest = Join-Path $stopRoot 'campaign.json'
    $stopState = Join-Path $stopRoot 'state.json'
    $stopRuntime = Join-Path $stopRoot 'runtime'
    Write-Data $stopManifest $stopCampaign
    $startProcess = Start-Process -FilePath 'pwsh' -ArgumentList @(
        '-NoProfile', '-File', $coordinator,
        '-Action', 'Start',
        '-Manifest', $stopManifest,
        '-RunnerConfig', $script:runnerConfig,
        '-State', $stopState,
        '-RuntimeRoot', $stopRuntime
    ) -PassThru
    $deadline = [DateTime]::UtcNow.AddSeconds(10)
    do {
        Start-Sleep -Milliseconds 100
        $runningObserved = $false
        if (Test-Path -LiteralPath $stopState) {
            $observedState = Get-Content -LiteralPath $stopState -Raw | ConvertFrom-Json
            $runningObserved = @($observedState.workers | Where-Object status -eq 'Running').Count -eq 1
        }
    } until ($runningObserved -or [DateTime]::UtcNow -gt $deadline)
    Assert-Test $runningObserved 'Stop fixture did not observe a running worker'
    & pwsh -NoProfile -File $coordinator -Action Stop -Manifest $stopManifest -State $stopState | Out-Null
    $stopMarker = "$stopState.stop-requested"
    Assert-Test (Test-Path -LiteralPath $stopMarker -PathType Leaf) `
        'Stop did not persist the durable request marker'
    $startProcess.WaitForExit()
    Assert-Test ($startProcess.ExitCode -eq 0) 'Cooperative stop start process failed'
    $pausedState = Get-Content -LiteralPath $stopState -Raw | ConvertFrom-Json
    Assert-Test ($pausedState.status -eq 'PausedByUser') 'Campaign did not reach PausedByUser'
    Assert-Test (@($pausedState.events | Where-Object type -in @('StopRequested', 'StopRequestObserved')).Count -ge 1) `
        'Paused state did not retain durable stop evidence'
    Assert-Test (@($pausedState.workers | Where-Object status -eq 'Completed').Count -eq 1) 'Running worker did not reach its safe boundary'
    Assert-Test (@($pausedState.workers | Where-Object status -eq 'Pending').Count -eq 2) 'Cooperative stop started extra workers'
    $resumeProcess = Start-Process -FilePath 'pwsh' -ArgumentList @(
        '-NoProfile', '-File', $coordinator,
        '-Action', 'Resume',
        '-Manifest', $stopManifest,
        '-RunnerConfig', $script:runnerConfig,
        '-State', $stopState,
        '-RuntimeRoot', $stopRuntime
    ) -PassThru
    $resumeLock = Join-Path $stopRuntime 'campaign.lock'
    $deadline = [DateTime]::UtcNow.AddSeconds(10)
    do {
        Start-Sleep -Milliseconds 100
        $resumeLockObserved = Test-Path -LiteralPath $resumeLock -PathType Container
    } until ($resumeLockObserved -or [DateTime]::UtcNow -gt $deadline)
    Assert-Test $resumeLockObserved 'Resume fixture did not acquire the campaign lock'
    & pwsh -NoProfile -File $coordinator -Action Resume -Manifest $stopManifest -RunnerConfig $script:runnerConfig -State $stopState -RuntimeRoot $stopRuntime 2>$null
    Assert-Test ($LASTEXITCODE -ne 0) 'Concurrent second resume bypassed the campaign lock'
    $resumeProcess.WaitForExit()
    Assert-Test ($resumeProcess.ExitCode -eq 0) 'Campaign resume failed'
    $resumedState = Get-Content -LiteralPath $stopState -Raw | ConvertFrom-Json
    Assert-Test ($resumedState.status -eq 'Completed') 'Resumed campaign did not complete'
    Assert-Test (-not (Test-Path -LiteralPath $stopMarker)) 'Resume did not clear the durable stop marker'
    Assert-Test (@($resumedState.workers | Where-Object status -eq 'Completed').Count -eq 3) 'Concurrent resume changed the completed worker set'

    Write-Output 'PASS: all parallel autonomous coordinator fixtures passed.'
} finally {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
}
