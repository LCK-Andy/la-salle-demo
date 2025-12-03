# la-salle-demo

## Install Git on macOS （在 macOS 上安装 Git）

### Step 1: Install Homebrew  
（步骤 1：安装 Homebrew）

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Git using Homebrew  
（步骤 2：使用 Homebrew 安装 Git）

```bash
brew install git
```

### Step 3: Configure Git username and email  
（步骤 3：配置 Git 用户名和邮箱）

```bash
git config --global user.name "Your Name" # Name shown on GitHub
git config --global user.email "your.email@example.com" # You can use GitHub private email
```

> **Note / 注意**  
> Remember to turn off: `Block command line pushes that expose my email-Off`  
> When you push to GitHub, if the commit author email is your GitHub private email, GitHub will block the push and warn you.  
> 当你推送到 GitHub 时，如果 commit 的作者邮箱是你的 GitHub 私人邮箱，GitHub 会阻止推送并警告你。

---

## How to use VSCode with GitHub  
## 如何在 VSCode 和 GitHub 搭配使用

1. Create a project on GitHub (done by the leader).  
    在 GitHub 上创建一个项目（由 leader 负责创建）。
2. Create a new folder on your computer.  
    在电脑里新建一个文件夹。
3. Open this folder with VSCode.  
    用 VSCode 打开这个文件夹。
4. Open the terminal in VSCode.  
    打开 VSCode 的终端（Terminal）。
5. Enter the following command in the terminal to clone the project (get the address from the green "Code" button on the GitHub project page):  
    在终端输入以下命令，克隆项目（地址可在 GitHub 项目页面的绿色 “Code” 按钮获取）：
     ```bash
     git clone <github project address>
     ```
     ```bash
     git clone <github项目地址>
     ```
6. Press Enter and wait for the download to complete.  
    回车，等待下载完成。
7. After downloading, you can see the project files in VSCode.  
    下载完成后，在 VSCode 里可以看到项目文件。
8. Edit files in VSCode.  
    在 VSCode 里修改文件。
9. View modified files in the Source Control sidebar.  
    在侧边栏的 Source Control 里查看修改的文件。
10. Click the plus sign to stage the modified files.  
     点击加号将修改的文件 stage。
11. Enter a commit message (Copilot can help write it).  
     输入 commit message（可用 Copilot 帮忙写）。
12. Click Commit to submit.  
     点击提交（Commit）。
13. Click Sync to upload changes to GitHub.  
     点击同步（Sync）将修改上传到 GitHub。
14. Go back to the GitHub project page to confirm the changes have been uploaded successfully.  
     回到 GitHub 项目页面，确认修改已上传成功。
15. Other members can repeat steps 4-6 to download the latest changes to their computers.  
     其他成员可重复 4-6 步，将最新修改下载到自己的电脑。
