# 部署说明

要将 AI 创业故事网站部署到 GitHub Pages，您可以使用以下两种方式之一：

## 方式 1: 使用 PowerShell 脚本 (推荐用于 Windows)

1. 确保您已在 GitHub 上创建了名为 `ai-entrepreneur-story` 的仓库
2. 获取您的 GitHub Personal Access Token (PAT)
3. 在 PowerShell 中设置环境变量：
   ```powershell
   $env:GH_TOKEN="your_personal_access_token_here"
   ```
4. 运行部署脚本：
   ```powershell
   cd C:\Users\39653\.openclaw\workspace\ai-entrepreneur-story
   .\deploy.ps1
   ```

## 方式 2: 手动部署

1. 确保您已在 GitHub 上创建了名为 `ai-entrepreneur-story` 的仓库
2. 打开命令行并导航到项目目录：
   ```bash
   cd C:\Users\39653\.openclaw\workspace\ai-entrepreneur-story
   ```
3. 初始化 git 仓库：
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
4. 添加远程仓库地址（替换为您自己的 GitHub 用户名）：
   ```bash
   git remote add origin https://github.com/aientrepreneurial/ai-entrepreneur-story.git
   ```
5. 推送代码：
   ```bash
   git branch -M main
   git push -u origin main
   ```

## 启用 GitHub Pages

部署完成后，您需要在 GitHub 仓库设置中启用 GitHub Pages：
1. 访问您的 GitHub 仓库页面
2. 点击 "Settings" 选项卡
3. 在左侧菜单中选择 "Pages"
4. 在 "Source" 部分选择 "Deploy from a branch"
5. 选择 "main" 分支和 "/" 目录
6. 点击 "Save"

完成后，您的网站将在 https://aientrepreneurial.github.io/ai-entrepreneur-story/ 上可用。