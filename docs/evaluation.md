# Evaluation

The synthetic suite contains five independently specified examples for each operational route. It exercises explicit evidence, conflicting sources, ambiguous requirements, missing evidence, customer choices, substitution and deviation approval. Expected labels and rationales are fixture metadata; they are not interpolated into the classifier prompt. They are compared with actual classifications after the model call.

Run `python3 scripts/validate-data.py`, then import and configure the workflows as described in the README and execute Workflow 02. Inspect the summary, per-case executions and any failed case IDs. Agreement is a comparison against these labels, not independent evidence of safety or production accuracy. Guardrail counts reflect returned cases; a rejected result throws an error and may halt the batch before a summary is produced. Inspect the failing node rather than treating an incomplete execution as a passing run.

The synthetic historical CSV uses retrospective labels, not operational classifications. Workflow 03 treats every supplied row as eligible, validates its route and calculates the illustrative potential deflection percentage. Do not interpret it as observed savings.

The live model evaluation has not been run for these fixtures. Model behaviour, parser compatibility and end-to-end workflow execution require a configured local n8n instance and OpenAI credential.
