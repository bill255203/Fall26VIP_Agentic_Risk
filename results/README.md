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
