# Results

`results/local/` is for generated local runs and is ignored by Git.

A result snapshot may be committed outside `results/local/` only after review.
Include provenance (a generated manifest or equivalent source/data record), exact
configuration and analysis commands, source evidence or a documented access path,
summary, interpretation, and limitations. For the scripted pilot, preserve its
generated manifest, configuration, and trial-level traces. Existing-data studies
must also identify source revisions, permissions, and transformations. Follow the
[experiment record](../docs/experiment-record.md). Never commit sensitive or restricted data.

Deterministic scripted runs validate the harness. Label them as fixture or validation results rather than empirical findings about model behavior.

## Large evidence files

Keep small reviewed tables, figures and analysis scripts in the repository. Before
uploading a large trace set, agree a durable storage location and access with the
instructor; no external storage service is provisioned by this guide. Do not rely
on a laptop path or an expiring sharing link for the final handoff.

In the pair's case document or snapshot README, record the exact artifact version,
download/access location, filenames, SHA-256 checksums, and analysis command. Explain
any access restrictions and provide permitted derived evidence needed to inspect
the claims. A reviewer must confirm they can retrieve the evidence and reproduce
the reported analysis. Keep originals and documented transformations distinguishable.
