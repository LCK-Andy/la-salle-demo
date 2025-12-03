# Git 拉取策略：合并、变基和快进  
Git Pull Strategies: Merge, Rebase, and Fast-Forward

当你运行 `git pull` 时，Git 会从远程仓库获取更改并将其集成到你的本地分支。根据情况，Git 可能会使用三种策略之一来集成更改：**合并（merge）**、**变基（rebase）** 或 **快进（fast-forward）**。以下是每种策略的详细说明。  
When you run `git pull`, Git fetches changes from the remote repository and integrates them into your local branch. Depending on the situation, Git may use one of three strategies to integrate changes: **merge**, **rebase**, or **fast-forward**. Here's a detailed explanation of each strategy.

---

## 1. Git 合并（Merge）

### 什么是合并？  
What is it?

`git merge` 会创建一个新的提交，将远程分支的更改与本地分支合并。此策略会保留两个分支的历史。  
`git merge` creates a new commit that combines the changes from the remote branch with your local branch. This strategy preserves the history of both branches.

### 何时使用？  
When to use?

- 当你想保留所有合并的清晰历史时  
    When you want to keep a clear history of all merges.
- 当团队中有多个开发者在同一分支协作时  
    When working in a team where multiple developers are contributing to the same branch.

### 示例  
Example

```bash
# 使用合并方式拉取更改
$ git pull --merge
```

### 结果  
Result

- 会创建一个新的合并提交  
    A new merge commit is created.
- 历史记录显示分支的分叉和合并点  
    The history shows the divergence and the merge point.

---

## 2. Git 变基（Rebase）

### 什么是变基？  
What is it?

`git rebase` 会通过将你的本地更改应用到远程分支之上来重写提交历史，从而创建线性的历史。  
`git rebase` rewrites the commit history by applying your local changes on top of the remote branch. This creates a linear history.

### 何时使用？  
When to use?

- 当你想要一个干净、线性的历史且不需要合并提交时  
    When you want a clean, linear history without merge commits.
- 当你在开发将来会合并的功能分支时  
    When working on a feature branch that will be merged later.

### 示例  
Example

```bash
# 使用变基方式拉取更改
$ git pull --rebase
```

### 结果  
Result

- 你的本地提交会被重新应用到远程分支之上  
    Your local commits are replayed on top of the remote branch.
- 历史变为线性，但提交哈希会改变  
    The history becomes linear, but the commit hashes change.

> **注意：** 在共享分支上变基需谨慎，因为它会重写历史。  
> **Note:** Be cautious when rebasing shared branches, as it rewrites history.

---

## 3. 快进（Fast-Forward）

### 什么是快进？  
What is it?

当你的本地分支直接落后于远程分支时，`git pull` 会执行快进操作，此时 Git 只需将分支指针向前移动，无需创建新提交。  
`git pull` performs a fast-forward when your local branch is directly behind the remote branch. In this case, Git simply moves the branch pointer forward without creating a new commit.

### 何时使用？  
When to use?

- 当你的本地分支没有独特的提交时  
    When your local branch has no unique commits.
- 当你想避免不必要的合并提交时  
    When you want to avoid unnecessary merge commits.

### 示例  
Example

```bash
# 使用快进方式拉取更改
$ git pull --ff-only
```

### 结果  
Result

- 分支指针被更新为与远程分支一致  
    The branch pointer is updated to match the remote branch.
- 不会创建新的提交  
    No new commits are created.

---

## 配置默认拉取行为  
Configuring Default Pull Behavior

你可以配置 Git 默认使用某种策略：  
You can configure Git to use a specific strategy by default:

### 设置合并为默认  
Set Merge as Default

```bash
git config --global pull.rebase false
```

### 设置变基为默认  
Set Rebase as Default

```bash
git config --global pull.rebase true
```

### 设置仅快进为默认  
Set Fast-Forward Only as Default

```bash
git config --global pull.ff only
```

---

## 总结  
Summary

| 策略         | 历史类型   | 使用场景                                   |  
|--------------|------------|--------------------------------------------|  
| **合并**     | 分叉       | 多分支协作开发                             |  
| **变基**     | 线性       | 功能分支，保持历史整洁                     |  
| **快进**     | 线性       | 无本地更改，简单更新                       |  

| Strategy       | History       | Use Case                                   |  
|----------------|---------------|-------------------------------------------|  
| **Merge**      | Divergent     | Collaborative work with multiple branches |  
| **Rebase**     | Linear        | Clean history for feature branches        |  
| **Fast-Forward** | Linear        | No local changes, simple updates          |  

选择最适合你的工作流和团队偏好的策略！  
Choose the strategy that best fits your workflow and team preferences!
