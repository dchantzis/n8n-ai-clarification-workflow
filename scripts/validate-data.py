#!/usr/bin/env python3
"""Validate the synthetic fixtures before importing them into n8n."""
import csv
import json
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cases = json.loads((root / 'evaluation/evaluation-cases.json').read_text())
labels = {'Resolved', 'Assisted', 'Customer Required'}
attachment = {'not_referenced', 'referenced_not_retrieved', 'retrieval_failed', 'retrieved_not_processed', 'processed', 'processing_failed', 'unsupported'}
order = {'not_supplied', 'not_retrieved', 'retrieval_failed', 'partial', 'retrieved'}
fields = ('test_id', 'conversation_reference', 'conversation_id', 'clarification_text', 'attachment_status', 'attachment_context', 'order_context_status', 'order_context', 'expected_classification', 'expected_rationale')
assert len(cases) == 15
assert Counter(c['expected_classification'] for c in cases) == {x: 5 for x in labels}
assert len({c['test_id'] for c in cases}) == len(cases)
for case in cases:
    assert all(isinstance(case.get(f), str) and case[f].strip() for f in fields)
    assert case['provenance'] == 'synthetic'
    assert case['attachment_status'] in attachment and case['order_context_status'] in order
    if case['expected_classification'] in {'Resolved', 'Assisted'}:
        assert case['attachment_status'] == 'processed' or case['order_context_status'] == 'retrieved'
with (root / 'evaluation/historical-route-labels.csv').open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
routes = {'potential_resolved', 'potential_assisted', 'customer_required', 'indeterminate'}
assert rows and {row['potential_route'] for row in rows} == routes
assert all(row['conversation_reference'].strip() and row['route_reason'].strip() for row in rows)
assert len({row['conversation_reference'] for row in rows}) == len(rows)
print(f'Valid: {len(cases)} synthetic evaluation cases, {len(rows)} synthetic historical labels')
