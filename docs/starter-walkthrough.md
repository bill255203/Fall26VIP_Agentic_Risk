# Guided starter walkthrough

**Optional practice:** use any part of this walkthrough if it helps. There is no
required submission or deadline, and skipping it does not affect your grade or
block pair work. You can read the worked example without installing anything.

If you want feedback or contribution credit for an attempt, use your own
Individual task under [#1](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/1).
Existing work remains valid Foundation evidence under the normal rubric.
The walkthrough introduces traces and research critique; it is not another assignment or a
case-study result. If setup is blocked, discuss the worked example below with a
partner or instructor and record the blocker. You can inspect your own run later.

## 1. Understand the small workflow

The [default configuration](../experiments/pilot.toml) uses synthetic limits of 100
and 50. The policy is **low risk → keep 100; high risk → reduce to 50**.
Four scripted stages pass information: monitor → analyze → approve → execute.
There are no model calls, real accounts, or credit decisions.

- `clean` supplies the correct low/high signal; `flip` supplies the opposite signal.
- The authority cap determines whether a proposal can be approved and executed.
- With execution enabled, the **oracle verifier** can read the fixture's true risk
  and block a wrong proposal. It cannot repair it. Real agents do not normally
  have this answer key.

Each of 40 base cases is reused in 12 conditions: three authority caps × two
verifier settings × two input conditions. That makes **480 scripted trials**, not
480 independent observations of model behavior.

## 2. Follow one high-risk case

This table describes the scripted behavior for a high-risk case with authority
`execute`. Its policy requires a final limit of **50**.

| Input / verifier | Proposed operation | Execution | Final limit | Task success |
| --- | --- | --- | ---: | --- |
| Clean / off | `reduce_limit` | Executes the correct operation | 50 | True |
| Flip / off | `keep_limit` | Executes an incorrect operation | 100 | False |
| Flip / on | `keep_limit` | Oracle blocks the incorrect operation | 100 | False |

The last row has no erroneous execution, but the required reduction still has not
happened. **Blocking is different from recovery.** Compare the final state, expected
state, and task success as well as the action-error count. The pilot measures no
actual financial loss or business harm.

Now consider low risk: the correct operation is to keep 100. A flipped signal
causes an unnecessary reduction to 50 without verification; the oracle can block it
and leave 100. Even here, a blocked operation is not counted as completed work.

## 3. Inspect the actual trace

Run the [README commands](../README.md#run-the-pilot), then open Python from the
repository folder: `python` in the activated macOS/Linux environment, or
`.\.venv\Scripts\python.exe` in Windows PowerShell. At Python's `>>>` prompt, paste
these lines (omit any prompt symbols). Adjust the output path if you used another.

```python
import json
from pathlib import Path
from pprint import pprint
trials = [json.loads(line) for line in Path("results/local/pilot/trials.jsonl").read_text(encoding="utf-8").splitlines()]
case_id = next(t["case_id"] for t in trials if t["evaluator"]["true_risk"] == "high")
matched = [t for t in trials if t["case_id"] == case_id and t["condition"]["authority"] == "execute"]
pprint([(t["condition"], t["executed"], t["final_limit"], t["task_success"]) for t in matched])
trace = next(t for t in matched if t["condition"]["fault"] == "flip" and t["condition"]["verification"])
pprint(trace)
```

`matched` contains four conditions for the **same case**, including clean/verifier-on.
The full `trace` is the flipped/verifier-on example. Locate:

| Trace field | What to look for |
| --- | --- |
| `condition` and `case_id` | Which comparison and base case this record represents |
| `evaluator` | True risk and expected decision/state; this is the answer key |
| `stages` | Each role's input, output, and acceptance/block status |
| `verification_trace` | The oracle's evidence and allow/block decision |
| `erroneous_execution`, `harmful_state_change` | Wrong executed decisions versus wrong state-changing decisions |
| `final_limit`, `task_success` | What actually remained and whether the correct operation completed |

Type `exit()` to return to your terminal. Do not edit generated traces to make
them match the example. If values differ, check the configuration and command and
record the difference in your task.

## 4. Read the summary carefully

Open `summary.csv` in a spreadsheet or text editor. For the default 40-case run,
the execution-enabled rows should contain:

| Input / verifier | Trials | Executions | Wrong executions | Harmful state changes | Successful tasks |
| --- | ---: | ---: | ---: | ---: | ---: |
| Clean / off | 40 | 40 | 0 | 0 | 40 |
| Clean / on | 40 | 40 | 0 | 0 | 40 |
| Flip / off | 40 | 40 | 40 | 20 | 0 |
| Flip / on | 40 | 0 | 0 | 0 | 0 |

The 40 wrong executions include 20 wrong reductions and 20 wrong keep decisions.
Only the reductions change state, so `harmful_state_change` misses the wrong keeps.
Its name denotes that narrow fixture metric, not every possible harm.

A rate “among executed” has no denominator when nothing executes: its CSV cell
is **blank**, not zero. Similarly, task-success rates are blank under authority
caps that cannot execute. Zero executions under those caps confirm the restriction;
they do not establish better reasoning. See [outcome definitions](research-plan.md#outcomes).

## 5. Record one observation or question

In your existing task, record your command, source revision (`git rev-parse HEAD`),
result or setup blocker, and a short explanation of one observation/question.
Link a relevant field, case ID or summary row. Use your own reasoning: reproducing
the expected numbers alone does not establish a research finding.

Possible questions: what should happen after a request is blocked? Which metric
would detect an unmet required action? What evidence could a practical verifier
use without the answer key? What changes before this can test a real agent?

Keep local generated output in `results/local/`; follow the [results guide](../results/README.md)
if preserving a reviewed snapshot. No extra report, new framework, or paid access
is needed for this walkthrough. Share optional external examples or setup findings
under [#6](https://github.com/zhongnz/Fall26VIP_Agentic_Risk/issues/6) when useful; no central genuine-agent teaching package is promised.
