# Public release review

## Extraction summary

- Copied unchanged: no files. The helper and ignore rules were adapted from the source.
- Modified: four workflow exports, Docker Compose configuration and development helper. Source-specific instance metadata, the stored sub-workflow reference, embedded sample data and a historical target were removed or replaced.
- Synthetic replacements: functional cases, example inputs and historical route labels. Previous results were excluded because they do not evaluate these fixtures.
- Excluded: task materials, original datasets, drawings, screenshots, presentations, planning notes and source Git history. Source-specific preparation and finalisation scripts depended on private review schemas, fixed population counts and original datasets. The fixture validator retains useful field, uniqueness and route checks; the full preparation and review-matching pipeline is not included.

## Confidentiality review

This review inspected all files present in the destination, including full workflow node parameters, prompts and code, fixtures, documentation, helper, configuration and ignore rules. Case-insensitive identifier and credential-pattern searches supplemented manual inspection. No original company identifier, private email, secret, internal URL or original order identifier was identified in the publishable files. Localhost URLs and container paths are local configuration. Pattern searches cannot establish that every sensitive value has been detected.

- **Workflow exports:** No workflow-level instance ID, credential binding or account reference was found. The batch workflow deliberately contains an empty classifier workflow ID and requires manual selection after import. Node and assignment IDs remain, including node IDs shared with the source exports; these are workflow-internal identifiers, not demonstrated instance or credential IDs. Owner review of their suitability for release remains appropriate.
- **Embedded prompts and code:** The classifier retains detailed routing and evidence-handling instructions from the source implementation. No company name or unavailable private-document reference was identified in the prompt. Their generic appearance does not establish reuse rights or that every business rule is non-confidential; the owner should review the **Classify Clarification** node and retained workflow logic.
- **Fixtures:** The 15 functional cases, example requests and six historical labels are marked or described as synthetic. Comparison against the source functional cases, historical labels and conversation CSV found no obvious verbatim copied supplier message; recurring generic manufacturing scenarios and routing language remain. Independent creation and absence of lightly adapted source material cannot be established conclusively by this comparison. A source-derived technical scenario or wording requires owner judgement; no confidential source text is reproduced here.
- **Documentation and configuration:** No original company identifier or recruitment context was found. The image uses an unpinned `latest` tag. The named volume can hold credentials and execution history, and `.gitignore` excludes common environment, database and local n8n files; it cannot prevent accidental inclusion of secrets under other names. No ignored runtime files were visible in the destination at review time; the Docker volume was not inspected.
- **Git history:** The destination has an unborn HEAD, no commits, refs, loose objects or packed objects. It therefore currently contains no source Git history or objects. All project files are untracked; there are no staged files. This is a local observation, not an assessment of remote content.

## Validation status

- **Static validation:** `python3 scripts/validate-data.py` passed for 15 functional cases and six historical labels; workflow JSON was inspected and the classifier JSON parsed successfully.
- **Isolated deterministic checks:** Representative valid and invalid input, output guardrail and synthetic KPI arithmetic checks passed in a standalone JavaScript harness. These do not exercise n8n integration.
- **Docker startup:** The owner confirmed that the destination n8n container started and opened in a browser. Its exact image version was not established. No container or volume was started, stopped or inspected during this review.
- **Workflow import:** Not verified by this review or implied by container startup.
- **Live AI execution and end-to-end evaluation:** Not performed for the replacement fixtures. No accuracy or production deflection result is claimed.

## Outstanding concerns

Human review is required for reuse rights and confidentiality of the retained prompts, workflow logic and synthetic scenarios, including whether retained node identifiers are acceptable. The source comparison cannot prove independent fixture creation or legal ownership. No legal clearance is asserted. The unpinned image and unverified imports and live execution limit reproducibility and demonstrated behaviour.

## Publication checklist

- [ ] Owner reviews retained prompts, workflow logic, node identifiers and synthetic examples for confidentiality and reuse rights.
- [ ] Owner confirms publication and licensing decisions and reviews the exact files to be included.
- [ ] Before any later commit, inspect staged files and local runtime exports for credentials or private data.
- [ ] If reproducible execution or demonstrated model behaviour is required for publication, establish the image version and separately verify workflow imports and the synthetic evaluation with appropriate credentials.
