# Human-in-the-loop operating model

## Goal
Use AI agents to accelerate repeatable work without giving up ownership of irreversible decisions.

## Principles
1. **Clear ownership** - every workflow has a human owner who can stop it.
2. **Least privilege for agents** - draft and prepare by default; mutate only inside agreed bounds.
3. **Human gates for irreversible steps** - identity checks, captchas, payments, assessments, outbound messages that commit you.
4. **Observable state** - ledger / logs so failures are visible (expired captchas, bad drafts, portal resets).
5. **Honest disclosure** - when useful for AI-native roles, say that AI helped prepare the work and that humans stayed in the loop.

## Example split (job-search / ops agent)
| Agent | Human |
|---|---|
| Score roles, draft CV variants, update trackers | Decide apply / skip |
| Fill known profile fields on forms | Captcha, OTP, e-sign |
| Prepare digests and interview packs | Assessments and interviews |
| Draft outreach | Approve before send |

## What this is not
This portfolio does not claim production LLM platform engineering or unsupervised autonomous applying.
