---
paths:
  - ".github/workflows/**"
  - ".github/dependabot.yml"
---

# GitHub Actions Workflow Guidelines

Action dependencies are pinned by the workflow dependency lockfile `.github/workflows/actions.lock` (see [Workflow dependency lockfiles](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles)).

- In `uses:`, write the **full release tag** (e.g., `actions/checkout@v6.0.2`), not a commit SHA. The lockfile pins the commit, including transitive dependencies.
- **Never edit `actions.lock` by hand.** After adding a workflow or changing any `uses:`, regenerate it with `gh actions-lock` (GitHub CLI extension `github/gh-actions-lock`) and commit it together with the workflow change.
- Review lockfile diffs: a changed `commit` is new code that will run; a changed `owner_id` / `repo_id` means the repository behind the name changed and must be investigated.
- `verify-lockfile.yml` runs `gh actions-lock --verify` on pull requests and fails when the lockfile is stale.
- Dependabot (`.github/dependabot.yml`) bumps action versions and regenerates the matching lockfile entries in the same pull request.
