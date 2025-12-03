# Git 拉取策略：合并、变基和快进  
Git Pull Strategies: Merge, Rebase, and Fast-Forward

当你运行 `git pull` 时，Git 会从远程仓库获取更改并将其集成到你的本地分支。根据情况，Git 可能会使用三种策略之一来集成更改：**合并（merge）**、**变基（rebase）** 或 **快进（fast-forward）**。  
When you run `git pull`, Git fetches changes from the remote repository and integrates them into your local branch. Git may use one of three strategies: **merge**, **rebase**, or **fast-forward**.

---

## 1. 合并（Merge）  
### 什么是合并？  
What is Merge?

`git merge` 会创建一个新的提交，将远程分支的更改与本地分支合并，保留两个分支的历史。  
`git merge` creates a new commit that combines changes from the remote branch with your local branch, preserving both histories.

### 何时使用？  
When to Use?

- 保留所有合并的历史  
  Keep a clear history of all merges  
- 团队协作开发  
  Teamwork with multiple contributors  

### 示例  
Example

```bash
git pull --merge
```

### 结果  
Result

- 创建一个新的合并提交  
  A new merge commit is created  
- 历史显示分叉和合并点  
  History shows divergence and merge points  

---

## 2. 变基（Rebase）  
### 什么是变基？  
What is Rebase?

`git rebase` 会将你的本地提交应用到远程分支之上，重写提交历史，形成线性历史。  
`git rebase` rewrites commit history by applying your local changes on top of the remote branch, creating a linear history.

### 何时使用？  
When to Use?

- 需要干净、线性的历史  
  Want a clean, linear history  
- 功能分支开发  
  Working on a feature branch  

### 示例  
Example

```bash
git pull --rebase
```

### 结果  
Result

- 本地提交被重新应用到远程分支  
  Local commits are replayed on top of the remote branch  
- 历史变为线性，提交哈希改变  
  History becomes linear, commit hashes change  

> **注意：** 在共享分支上变基需谨慎，因为它会重写历史。  
> **Note:** Be cautious when rebasing shared branches, as it rewrites history.

---

## 3. 快进（Fast-Forward）  
### 什么是快进？  
What is Fast-Forward?

当本地分支直接落后于远程分支时，`git pull` 会执行快进操作，只需将分支指针向前移动，无需新提交。  
When your local branch is directly behind the remote branch, `git pull` performs a fast-forward by moving the branch pointer forward without creating a new commit.

### 何时使用？  
When to Use?

- 本地分支没有独特提交  
  No unique local commits  
- 避免不必要的合并提交  
  Avoid unnecessary merge commits  

### 示例  
Example

```bash
git pull --ff-only
```

### 结果  
Result

- 分支指针更新为与远程一致  
  Branch pointer updated to match remote  
- 不会创建新提交  
  No new commits created  

---

## 配置默认拉取行为  
Configuring Default Pull Behavior

你可以配置 Git 默认使用某种策略：  
You can set Git to use a specific strategy by default:

- 设置合并为默认  
  Set Merge as Default  

  ```bash
  git config --global pull.rebase false
  ```

- 设置变基为默认  
  Set Rebase as Default  

  ```bash
  git config --global pull.rebase true
  ```

- 设置仅快进为默认  
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