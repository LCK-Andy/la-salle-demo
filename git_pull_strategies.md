# Git Pull: Merge, Rebase, and Fast-Forward

When you use `git pull`, Git gets updates from the remote repository (the shared version of your code) and adds them to your local branch (your copy of the code). There are three ways Git can do this: **merge**, **rebase**, and **fast-forward**. Let’s break them down simply.

---

## 1. Git Merge

### What is it?

`git merge` combines the changes from the remote branch with your local branch. It creates a new "merge commit" to show that two branches were joined together.

### When to use?

- When you want to keep a record of all changes and merges.
- When working with a team where everyone is making changes.

### Example

```bash
# Pull changes using merge
$ git pull --merge
```

### What happens?

- A new commit is created to show the merge.
- The history shows where the branches split and came back together.

---

## 2. Git Rebase

### What is it?

`git rebase` takes your changes and puts them on top of the remote branch’s changes. This makes the history look like a straight line.

### When to use?

- When you want a clean and simple history.
- When you’re working on your own feature branch.

### Example

```bash
# Pull changes using rebase
$ git pull --rebase
```

### What happens?

- Your changes are moved to the top of the history.
- The history looks neat, but the commit IDs change.

> **Be careful!** Don’t rebase if you’re sharing your branch with others. It can cause confusion.

---

## 3. Fast-Forward

### What is it?

`git pull` does a fast-forward when your branch is already behind the remote branch. Git just moves your branch forward to match the remote branch. No new commits are made.

### When to use?

- When you haven’t made any changes locally.
- When you just want to update your branch.

### Example

```bash
# Pull changes using fast-forward
$ git pull --ff-only
```

### What happens?

- Your branch is updated to match the remote branch.
- No extra commits are created.

---

## How to Set a Default Pull Method

You can tell Git which method to use by default:

### Use Merge as Default

```bash
git config --global pull.rebase false
```

### Use Rebase as Default

```bash
git config --global pull.rebase true
```

### Use Fast-Forward Only as Default

```bash
git config --global pull.ff only
```

---

## Quick Summary

| Method          | History       | When to Use                              |
|-----------------|---------------|-----------------------------------------|
| **Merge**       | Shows splits  | Teamwork with lots of changes           |
| **Rebase**      | Straight line | Clean history for your own work         |
| **Fast-Forward**| Straight line | Simple updates with no local changes    |

Pick the method that works best for your project!
