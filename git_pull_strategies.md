# Git Pull Strategies: Merge, Rebase, and Fast-Forward

When you run `git pull`, Git fetches changes from the remote repository and integrates them into your local branch. Depending on the situation, Git may use one of three strategies to integrate changes: **merge**, **rebase**, or **fast-forward**. Here's a detailed explanation of each strategy.

---

## 1. Git Merge

### What is it?

`git merge` creates a new commit that combines the changes from the remote branch with your local branch. This strategy preserves the history of both branches.

### When to use?

- When you want to keep a clear history of all merges.
- When working in a team where multiple developers are contributing to the same branch.

### Example

```bash
# Pull changes using merge
$ git pull --merge
```

### Result

- A new merge commit is created.
- The history shows the divergence and the merge point.

---

## 2. Git Rebase

### What is it?

`git rebase` rewrites the commit history by applying your local changes on top of the remote branch. This creates a linear history.

### When to use?

- When you want a clean, linear history without merge commits.
- When working on a feature branch that will be merged later.

### Example

```bash
# Pull changes using rebase
$ git pull --rebase
```

### Result

- Your local commits are replayed on top of the remote branch.
- The history becomes linear, but the commit hashes change.

> **Note:** Be cautious when rebasing shared branches, as it rewrites history.

---

## 3. Fast-Forward

### What is it?

`git pull` performs a fast-forward when your local branch is directly behind the remote branch. In this case, Git simply moves the branch pointer forward without creating a new commit.

### When to use?

- When your local branch has no unique commits.
- When you want to avoid unnecessary merge commits.

### Example

```bash
# Pull changes using fast-forward
$ git pull --ff-only
```

### Result

- The branch pointer is updated to match the remote branch.
- No new commits are created.

---

## Configuring Default Pull Behavior

You can configure Git to use a specific strategy by default:

### Set Merge as Default

```bash
git config --global pull.rebase false
```

### Set Rebase as Default

```bash
git config --global pull.rebase true
```

### Set Fast-Forward Only as Default

```bash
git config --global pull.ff only
```

---

## Summary

| Strategy       | History       | Use Case                                   |
|----------------|---------------|-------------------------------------------|
| **Merge**      | Divergent     | Collaborative work with multiple branches |
| **Rebase**     | Linear        | Clean history for feature branches        |
| **Fast-Forward** | Linear        | No local changes, simple updates          |

Choose the strategy that best fits your workflow and team preferences!
