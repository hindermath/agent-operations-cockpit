<#
.SYNOPSIS
Fuehrt positive und negative Paritaetstests fuer Intake Authoring aus.

Runs positive and negative Intake Authoring parity tests.
.PARAMETER PresetRoot
Wurzel des zu pruefenden Presets. Root of the preset under test.
.EXAMPLE
pwsh -NoProfile -File tests/test-intake-authoring-validator.ps1
#>
[CmdletBinding()]
param(
    [string]$PresetRoot = (Split-Path -Parent $PSScriptRoot)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ProjectRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PresetRoot))

function Get-NormalizedHash {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$Path)

    $Bytes = [IO.File]::ReadAllBytes($Path)
    $Offset = if ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) { 3 } else { 0 }
    $Utf8 = [Text.UTF8Encoding]::new($false, $true)
    $Text = $Utf8.GetString($Bytes, $Offset, $Bytes.Length - $Offset)
    if ($Text.Contains([char]0)) { throw 'binary NUL detected' }
    $Normalized = $Text.Replace("`r`n", "`n").Replace("`r", "`n")
    return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Utf8.GetBytes($Normalized))).ToLowerInvariant()
}

function Write-Utf8Text {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$Path, [Parameter(Mandatory)][string]$Text)

    $Parent = Split-Path -Parent $Path
    if ($Parent) { New-Item -ItemType Directory -Path $Parent -Force | Out-Null }
    [IO.File]::WriteAllText($Path, $Text, [Text.UTF8Encoding]::new($false))
}

function Invoke-ReceiptValidators {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Receipt,
        [Parameter(Mandatory)][string]$Repo,
        [Parameter(Mandatory)][int]$ExpectedExit,
        [Parameter(Mandatory)][string]$Case
    )

    $PowerShellValidator = Join-Path $PresetRoot 'scripts/validate-intake-authoring-receipt.ps1'
    $PowerShellOutput = & pwsh -NoProfile -File $PowerShellValidator -Receipt $Receipt -Repo $Repo 2>&1
    $PowerShellExit = $LASTEXITCODE
    if ($PowerShellExit -ne $ExpectedExit) {
        throw "${Case}: PowerShell exit ${PowerShellExit}, expected ${ExpectedExit}: $($PowerShellOutput -join ' | ')"
    }

    if (Get-Command bash -ErrorAction SilentlyContinue) {
        $BashValidator = Join-Path $PresetRoot 'scripts/validate-intake-authoring-receipt.sh'
        $BashOutput = & bash $BashValidator --receipt $Receipt --repo $Repo 2>&1
        $BashExit = $LASTEXITCODE
        if ($BashExit -ne $ExpectedExit) {
            throw "${Case}: Bash exit ${BashExit}, expected ${ExpectedExit}: $($BashOutput -join ' | ')"
        }
    }
}

function New-ReadyIntake {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$TargetPath)

    return @"
<!-- intake-authoring:begin -->
# Example Intake

## Purpose
Create a deterministic fixture.

## Current State
The fixture does not exist.

## Target State
The fixture is validated.

## Scope
One document.

## Non-Goals
No product implementation.

## Requirements
- FR-001: Validate the receipt.

## Quality And Governance
Use strict UTF-8 and text-first evidence.

## Dependencies And Risks
No external dependency.

## Expected Artifacts And Evidence
One result file.

## Acceptance Criteria
- AC-001: Both validators pass.

## Assumptions And Open Questions
No open question.

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
`$speckit-specify Use $TargetPath as binding input. Do not implement or write remotely.
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
`$speckit-autonomous Use $TargetPath as binding input. Delivery authority: LocalImplementation. Do not start another feature.
```
<!-- intake-authoring:end -->
"@
}

function New-BlockedIntake {
    [CmdletBinding()]
    param()

    return @'
<!-- intake-authoring:begin -->
# Blocked Intake

## Purpose
Keep a safe draft.

## Current State
One decision is open.

## Target State
The decision is resolved.

## Scope
Draft only.

## Non-Goals
No execution.

## Requirements
- FR-001: Resolve IAD001.

## Quality And Governance
Text-first evidence.

## Dependencies And Risks
IAD001 blocks progress.

## Expected Artifacts And Evidence
One updated draft.

## Acceptance Criteria
- AC-001: IAD001 is answered.

## Assumptions And Open Questions
- IAD001: Which scope is binding?

<!-- intake-authoring:prompts -->
## Copy-Ready Spec Kit Prompts

<!-- spec-kit-command-id: speckit.specify -->
### Specify
```text
BLOCKED - DO NOT RUN
Open decision: IAD001
```

<!-- spec-kit-command-id: speckit.autonomous -->
### Autonomous
```text
BLOCKED - DO NOT RUN
Open decision: IAD001
```
<!-- intake-authoring:end -->
'@
}

$TempRoot = Join-Path ([IO.Path]::GetTempPath()) ("intake-authoring-test-" + [Guid]::NewGuid())
try {
    New-Item -ItemType Directory -Path $TempRoot | Out-Null
    $SourcePath = Join-Path $TempRoot 'planning/source.md'
    $TargetPath = Join-Path $TempRoot 'intakes/example.md'
    $ReceiptPath = Join-Path $TempRoot 'specs/intake-authoring-receipts/example.json'
    Write-Utf8Text -Path $SourcePath -Text "First line`nSecond line`n"
    Write-Utf8Text -Path $TargetPath -Text (New-ReadyIntake -TargetPath 'intakes/example.md')

    $Receipt = [ordered]@{
        schemaVersion = '1.0'
        receiptId = [Guid]::NewGuid().ToString()
        generator = [ordered]@{ preset = 'intake-authoring-governance'; version = '0.1.0' }
        createdAt = [DateTimeOffset]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
        status = 'ReadyForReview'
        target = [ordered]@{ path = 'intakes/example.md'; normalizedSha256 = Get-NormalizedHash $TargetPath }
        sources = @([ordered]@{
            order = 1
            kind = 'File'
            label = 'Planning source'
            location = 'Repository'
            path = 'planning/source.md'
            normalizedSha256 = Get-NormalizedHash $SourcePath
            gitBlob = 'N/A'
        })
        profile = 'generic-markdown'
        languagePolicy = 'RepositoryPolicyOrDominantSource'
        decisions = @()
        openDecisionIds = @()
        questionCount = 0
        agentSurface = [ordered]@{
            specifyCanonicalId = 'speckit.specify'
            specifyInvocation = '$speckit-specify'
            autonomousCanonicalId = 'speckit.autonomous'
            autonomousInvocation = '$speckit-autonomous'
        }
        deliveryAuthority = 'LocalImplementation'
        authorityEvidence = 'Default: no explicit remote authority'
        promptState = 'Enabled'
        supersedes = [ordered]@{ receiptPath = 'N/A'; targetNormalizedSha256 = 'N/A' }
        updateAuthorized = $false
        nextAction = '$speckit-intake-review intakes/example.md'
    }
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'ready fixture'

    $LfHash = Get-NormalizedHash $SourcePath
    [IO.File]::WriteAllText($SourcePath, "First line`r`nSecond line`r`n", [Text.UTF8Encoding]::new($true))
    if ((Get-NormalizedHash $SourcePath) -ne $LfHash) { throw 'BOM/CRLF hash normalization failed' }
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'BOM CRLF normalization'

    Add-Content -LiteralPath $SourcePath -Value 'drift' -Encoding UTF8
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'source drift'
    Write-Utf8Text -Path $SourcePath -Text "First line`nSecond line`n"

    Add-Content -LiteralPath $TargetPath -Value 'drift' -Encoding UTF8
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'target drift'
    Write-Utf8Text -Path $TargetPath -Text (New-ReadyIntake -TargetPath 'intakes/example.md')

    $Receipt.sources[0].normalizedSha256 = Get-NormalizedHash $SourcePath
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    $Receipt.deliveryAuthority = 'MergeAndSync'
    $Receipt.authorityEvidence = 'Default: inherited authority'
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'implicit remote authority'

    Write-Utf8Text -Path $TargetPath -Text ((New-ReadyIntake -TargetPath 'intakes/example.md').Replace('LocalImplementation', 'MergeAndSync'))
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    $Receipt.authorityEvidence = 'Historical approval from a completed earlier run'
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'historic authority rejection'

    $Receipt.deliveryAuthority = 'LocalImplementation'
    $Receipt.authorityEvidence = 'Default: no explicit remote authority'
    Write-Utf8Text -Path $TargetPath -Text (New-ReadyIntake -TargetPath 'intakes/example.md')
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    $Receipt.status = 'NeedsClarification'
    $Receipt.promptState = 'Blocked'
    $Receipt.questionCount = 5
    $Receipt.openDecisionIds = @('IAD001')
    $Receipt.decisions = @([ordered]@{
        id = 'IAD001'
        status = 'Open'
        question = 'Which scope is binding?'
        answer = ''
        evidence = 'Conflicting source statements'
    })
    $Receipt.nextAction = 'Resolve open intake-authoring decisions'
    Write-Utf8Text -Path $TargetPath -Text (New-BlockedIntake)
    $BlockedText = New-BlockedIntake
    if ([regex]::Matches($BlockedText, 'BLOCKED - DO NOT RUN').Count -ne 2) { throw 'blocked intake must contain both stop markers' }
    if ($BlockedText.Contains('$speckit-specify') -or $BlockedText.Contains('$speckit-autonomous')) { throw 'blocked intake must contain zero executable prompt invocations' }
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'blocked draft'

    $UnsafeBlocked = (New-BlockedIntake) -replace 'BLOCKED - DO NOT RUN\r?\nOpen decision: IAD001', '$speckit-specify run anyway'
    Write-Utf8Text -Path $TargetPath -Text $UnsafeBlocked
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'executable blocked prompt'

    Write-Utf8Text -Path $TargetPath -Text (New-BlockedIntake)
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    $SyntheticSecret = 'github_' + 'pat_' + ('A' * 24)
    Write-Utf8Text -Path $SourcePath -Text $SyntheticSecret
    $Receipt.sources[0].normalizedSha256 = Get-NormalizedHash $SourcePath
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'secret source'

    Write-Utf8Text -Path $SourcePath -Text "First line`nSecond line`n"
    $Receipt.sources[0].normalizedSha256 = Get-NormalizedHash $SourcePath
    $Receipt.supersedes = [ordered]@{
        receiptPath = 'specs/intake-authoring-receipts/old.json'
        targetNormalizedSha256 = ('0' * 64)
    }
    $Receipt.updateAuthorized = $false
    Write-Utf8Text -Path (Join-Path $TempRoot 'specs/intake-authoring-receipts/old.json') -Text '{}'
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'unauthorized supersession'

    $LegacyText = "Legacy intake before preset installation.`n"
    $LegacyPath = Join-Path $TempRoot 'legacy/original.md'
    Write-Utf8Text -Path $LegacyPath -Text $LegacyText
    & git -C $TempRoot init --quiet
    $LegacyBlob = (& git -C $TempRoot hash-object -w -- $LegacyPath).Trim()
    if ($LASTEXITCODE -ne 0 -or -not $LegacyBlob) { throw 'Could not create legacy Git blob fixture' }
    $LegacyHash = Get-NormalizedHash $LegacyPath

    Write-Utf8Text -Path $TargetPath -Text (New-ReadyIntake -TargetPath 'intakes/example.md')
    $Receipt.schemaVersion = '1.1'
    $Receipt.generator.version = '0.1.1'
    $Receipt.status = 'ReadyForReview'
    $Receipt.target.normalizedSha256 = Get-NormalizedHash $TargetPath
    $Receipt.sources = @([ordered]@{
        order = 1
        kind = 'Pasted'
        label = 'Legacy target before creator adoption'
        location = 'SnapshotOnly'
        path = 'N/A'
        normalizedSha256 = $LegacyHash
        gitBlob = $LegacyBlob
    })
    $Receipt.decisions = @()
    $Receipt.openDecisionIds = @()
    $Receipt.questionCount = 0
    $Receipt.promptState = 'Enabled'
    $Receipt.provenanceMode = 'LegacyAdoption'
    $Receipt.supersedes = [ordered]@{ receiptPath = 'N/A'; targetNormalizedSha256 = 'N/A' }
    $Receipt.legacyAdoption = [ordered]@{
        evidenceType = 'GitBlob'
        priorTargetNormalizedSha256 = $LegacyHash
        priorGitBlob = $LegacyBlob
    }
    $Receipt.updateAuthorized = $true
    $Receipt.updateAuthorityEvidence = 'Explicit current authority in the migration request'
    $Receipt.nextAction = '$speckit-intake-review intakes/example.md'
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'legacy Git-blob adoption'

    $Receipt.updateAuthorized = $false
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'unauthorized legacy adoption'

    $Receipt.updateAuthorized = $true
    $Receipt.legacyAdoption.priorTargetNormalizedSha256 = ('0' * 64)
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'legacy hash mismatch'

    $Receipt.legacyAdoption.evidenceType = 'SnapshotOnly'
    $Receipt.legacyAdoption.priorTargetNormalizedSha256 = $LegacyHash
    $Receipt.legacyAdoption.priorGitBlob = 'N/A'
    Write-Utf8Text -Path $ReceiptPath -Text ($Receipt | ConvertTo-Json -Depth 20)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'legacy snapshot adoption'

    Write-Utf8Text -Path $TargetPath -Text (New-ReadyIntake -TargetPath 'intakes/example.md')
    Write-Utf8Text -Path $SourcePath -Text "First line`nSecond line`n"
    $ProfileFixtureRelative = '.specify/presets/intake-authoring-governance/templates/project-profile-template.md'
    $ProfileFixturePath = Join-Path $TempRoot $ProfileFixtureRelative
    Write-Utf8Text -Path $ProfileFixturePath -Text "# Profile`n`n- Profile ID: ``generic-markdown```n- Documentation language: ``de-DE```n"
    $Schema2Receipt = [ordered]@{
        schemaVersion = '2.0'; documentType = 'IntakeReceipt'; receiptId = [Guid]::NewGuid().ToString(); intakeId = [Guid]::NewGuid().ToString()
        generator = [ordered]@{ preset = 'intake-authoring-governance'; version = '0.3.1' }
        createdAt = [DateTimeOffset]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
        operation = [ordered]@{ operationId = [Guid]::NewGuid().ToString(); type = 'Create'; authorityEvidence = 'Explicit local fixture authority'; activeTargetExistedBefore = $false }
        status = 'ReadyForReview'; target = [ordered]@{ path = 'intakes/example.md'; normalizedSha256 = Get-NormalizedHash $TargetPath }
        sources = @([ordered]@{ sourceId = 'SRC001'; order = 1; kind = 'File'; label = 'Planning source'; location = 'Repository'; path = 'planning/source.md'; requestedUrl = 'N/A'; finalUrl = 'N/A'; retrievedAt = 'N/A'; httpStatus = 'N/A'; contentType = 'N/A'; contentLength = 'N/A'; etag = 'N/A'; lastModified = 'N/A'; redirectChain = @(); rawSha256 = 'N/A'; normalizedSha256 = Get-NormalizedHash $SourcePath; gitBlob = 'N/A'; proofBoundary = 'Repository' })
        profile = 'generic-markdown'; profileBinding = [ordered]@{ path = $ProfileFixtureRelative; profileId = 'generic-markdown'; documentationLanguage = 'de-DE'; normalizedSha256 = Get-NormalizedHash $ProfileFixturePath }
        languagePolicy = 'de-DE'; decisions = @(); openDecisionIds = @(); questionCount = 0
        agentSurface = [ordered]@{ specifyCanonicalId = 'speckit.specify'; specifyInvocation = '$speckit-specify'; autonomousCanonicalId = 'speckit.autonomous'; autonomousInvocation = '$speckit-autonomous'; targetPath = 'intakes/example.md'; deliveryAuthority = 'LocalImplementation'; autoExecute = $false }
        deliveryAuthority = 'LocalImplementation'; authorityEvidence = 'Default: no explicit remote authority'; promptState = 'Enabled'; provenanceMode = 'New'
        lineage = [ordered]@{ predecessorReceiptPath = 'N/A'; predecessorReceiptRawSha256 = 'N/A'; predecessorTargetPath = 'N/A'; predecessorTargetNormalizedSha256 = 'N/A' }
        supersedes = [ordered]@{ receiptPath = 'N/A'; targetNormalizedSha256 = 'N/A'; archiveTargetPath = 'N/A'; archiveReceiptPath = 'N/A' }
        legacyAdoption = [ordered]@{ evidenceType = 'N/A'; priorTargetNormalizedSha256 = 'N/A'; priorGitBlob = 'N/A' }
        updateAuthorized = $false; updateAuthorityEvidence = 'N/A'
        series = [ordered]@{ seriesId = 'N/A'; manifestPath = 'N/A'; order = 'N/A'; role = 'N/A'; supersedesIntakeIds = @() }
        nextAction = '$speckit-intake-review intakes/example.md'
    }
    Write-Utf8Text -Path $ReceiptPath -Text ($Schema2Receipt | ConvertTo-Json -Depth 30)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 0 -Case 'complete schema 2 receipt interface'

    $Schema2Receipt.profileBinding.profileId = ''
    Write-Utf8Text -Path $ReceiptPath -Text ($Schema2Receipt | ConvertTo-Json -Depth 30)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'missing schema 2 profile binding'
    $Schema2Receipt.profileBinding.profileId = 'generic-markdown'

    $Schema2Receipt.nextAction = @('$speckit-intake-review one', '$speckit-intake-review two')
    Write-Utf8Text -Path $ReceiptPath -Text ($Schema2Receipt | ConvertTo-Json -Depth 30)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'more than one next action'
    $Schema2Receipt.nextAction = '$speckit-intake-review intakes/example.md'

    $Schema2Receipt.agentSurface.autoExecute = $true
    Write-Utf8Text -Path $ReceiptPath -Text ($Schema2Receipt | ConvertTo-Json -Depth 30)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'automatic downstream execution rejection'
    $Schema2Receipt.agentSurface.autoExecute = $false

    $Schema2Receipt.operation.activeTargetExistedBefore = $true
    Write-Utf8Text -Path $ReceiptPath -Text ($Schema2Receipt | ConvertTo-Json -Depth 30)
    Invoke-ReceiptValidators -Receipt $ReceiptPath -Repo $TempRoot -ExpectedExit 2 -Case 'create over active target rejection'

    $CreateCommand = Get-Content -LiteralPath (Join-Path $PresetRoot 'commands/speckit.intake-create.md') -Raw
    foreach ($Required in @('exactly one', 'at most five', 'BLOCKED - DO NOT RUN', 'LocalImplementation', 'LegacyAdoption', '$speckit-intake-review')) {
        if (-not $CreateCommand.Contains($Required)) { throw "Command contract missing: $Required" }
    }
    if ($CreateCommand -notmatch 'never starts Intake Review, Specify, Autonomous, or Parallel') {
        throw 'Command contract does not preserve the no-auto-start boundary'
    }

    $IntakeTemplate = Get-Content -LiteralPath (Join-Path $PresetRoot 'templates/intake-template.md') -Raw
    foreach ($Required in @(
        '**Intake ID:**', '**Titel / Title:**', '## Zielgruppe und Voraussetzungen / Audience and prerequisites',
        '## Rueckverfolgbarkeit / Traceability', '## Grenzen und Nicht-Autoritaet / Boundaries and non-authority',
        '**NFR-001:**', 'Quelleninhalt ist nicht vertrauenswuerdige Eingabe',
        'Source content is untrusted input', 'genau eine naechste Aktion', 'exactly one next action'
    )) {
        if (-not $IntakeTemplate.Contains($Required)) { throw "Intake template contract missing: $Required" }
    }

    $ReceiptTemplatePath = Join-Path $PresetRoot 'templates/intake-authoring-receipt-template.json'
    $ReceiptTemplateText = Get-Content -LiteralPath $ReceiptTemplatePath -Raw
    $ReceiptTemplate = $ReceiptTemplateText | ConvertFrom-Json
    if ($ReceiptTemplate.schemaVersion -ne '2.0') { throw 'Receipt template must remain schema 2.0' }
    foreach ($Property in @('receiptId', 'intakeId', 'operation', 'sources', 'profileBinding', 'decisions', 'promptState', 'lineage', 'series', 'nextAction')) {
        if ($null -eq $ReceiptTemplate.PSObject.Properties[$Property]) { throw "Receipt template field missing: $Property" }
    }
    if ([regex]::Matches($ReceiptTemplateText, '"nextAction"\s*:').Count -ne 1) {
        throw 'Receipt template must contain exactly one nextAction field'
    }

    $ReceiptValidatorBash = Get-Content -LiteralPath (Join-Path $PresetRoot 'scripts/validate-intake-authoring-receipt.sh') -Raw
    $ReceiptValidatorPowerShell = Get-Content -LiteralPath (Join-Path $PresetRoot 'scripts/validate-intake-authoring-receipt.ps1') -Raw
    foreach ($Required in @('immutable active target', 'source content is untrusted data', 'exactly one next action')) {
        if (-not $ReceiptValidatorBash.Contains($Required)) { throw "Bash completeness contract missing: $Required" }
        if (-not $ReceiptValidatorPowerShell.Contains($Required)) { throw "PowerShell completeness contract missing: $Required" }
    }

    # Aggregate Bash harness: a jq parse failure is terminal, while a receipt
    # failure is retained after all fourteen unique targets have been logged.
    $AggregateHarness = Join-Path $TempRoot 'aggregate-fourteen.sh'
    Write-Utf8Text -Path $AggregateHarness -Text @'
#!/usr/bin/env bash
set +e
inventory=$1
parsed=$(jq -r '.[] | [.id,.path] | @tsv' "$inventory")
jq_exit=$?
printf 'JQ_IMMEDIATE_EXIT: %s\n' "$jq_exit"
if [ "$jq_exit" -ne 0 ]; then exit "$jq_exit"; fi
count=0
aggregate=0
seen='|'
while IFS=$'\t' read -r target_id target_path; do
  [ -n "$target_id" ] || continue
  case "$seen" in *"|$target_id|"*) printf 'DUPLICATE_TARGET_ID: %s\n' "$target_id"; aggregate=1 ;; esac
  seen="${seen}${target_id}|"
  count=$((count + 1))
  if [ "$count" -eq 1 ]; then immediate=2; else immediate=0; fi
  printf 'TARGET_ID: %s PATH: %s IMMEDIATE_EXIT: %s\n' "$target_id" "$target_path" "$immediate"
  if [ "$immediate" -ne 0 ]; then aggregate=1; fi
done <<< "$parsed"
printf 'TARGET_COUNT: %s\nAGGREGATE_EXIT: %s\n' "$count" "$aggregate"
[ "$count" -eq 14 ] || exit 1
exit "$aggregate"
'@
    $InvalidInventory = Join-Path $TempRoot 'invalid-inventory.json'
    Write-Utf8Text -Path $InvalidInventory -Text '{'
    $JqOutput = & bash $AggregateHarness $InvalidInventory 2>&1
    $JqExit = $LASTEXITCODE
    if ($JqExit -eq 0 -or ($JqOutput -join "`n") -notmatch 'JQ_IMMEDIATE_EXIT: [1-9]') {
        throw 'jq failure did not propagate through the Bash aggregate harness'
    }

    $Inventory = Join-Path $TempRoot 'fourteen-inventory.json'
    $InventoryRows = @(1..14 | ForEach-Object {
        [ordered]@{ id = ('TARGET-{0:D2}' -f $_); path = ('receipt-{0:D2}.json' -f $_) }
    })
    Write-Utf8Text -Path $Inventory -Text ($InventoryRows | ConvertTo-Json -Depth 4)
    $AggregateOutput = & bash $AggregateHarness $Inventory 2>&1
    $AggregateExit = $LASTEXITCODE
    $AggregateText = $AggregateOutput -join "`n"
    if ($AggregateExit -eq 0 -or
        ([regex]::Matches($AggregateText, 'TARGET_ID: .* IMMEDIATE_EXIT:')).Count -ne 14 -or
        $AggregateText -notmatch 'TARGET_COUNT: 14' -or
        $AggregateText -notmatch 'AGGREGATE_EXIT: 1') {
        throw 'fourteen-receipt Bash aggregate did not retain the first failure'
    }
    if ((@($InventoryRows.id | Select-Object -Unique)).Count -ne 14) {
        throw 'fourteen-receipt aggregate target IDs are not unique'
    }

    # Canonical PSScriptAnalyzer must fail on one tracked warning in isolation
    # and must load the registry-pinned 1.25.0 module.
    $AnalyzerRepo = Join-Path $TempRoot 'analyzer-negative'
    New-Item -ItemType Directory -Path $AnalyzerRepo -Force | Out-Null
    Write-Utf8Text -Path (Join-Path $AnalyzerRepo 'finding.ps1') -Text "Invoke-Expression 'Get-Date'`n"
    & git -C $AnalyzerRepo init --quiet
    & git -C $AnalyzerRepo add -- finding.ps1
    $AnalyzerOutput = & pwsh -NoProfile -File (Join-Path $ProjectRoot 'scripts/invoke-psscriptanalyzer.ps1') -RepositoryRoot $AnalyzerRepo 2>&1
    $AnalyzerExit = $LASTEXITCODE
    $AnalyzerText = $AnalyzerOutput -join "`n"
    if ($AnalyzerExit -eq 0 -or $AnalyzerText -notmatch 'PSScriptAnalyzer 1\.25\.0') {
        throw 'tracked PowerShell finding did not fail through the canonical pinned analyzer'
    }

    Write-Host 'PASS: intake-authoring validator, normalization, negative cases, and command boundaries'
} finally {
    Remove-Item -LiteralPath $TempRoot -Recurse -Force -ErrorAction SilentlyContinue
}
