# AI创业故事网站GitHub部署指南

## 步骤1：创建GitHub仓库
1. 登录到您的GitHub账户 (https://github.com)
2. 点击右上角的“+”号，选择“New repository”
3. 输入仓库名称：`ai-entrepreneur-story`
4. 添加描述：“AI创业故事网站”
5. 选择“Public”（公开）
6. 点击“Create repository”按钮

## 步骤2：上传网站文件
1. 进入刚创建的仓库页面
2. 点击“Upload files”按钮
3. 将E:\aia\ai_entrepreneur_story\文件夹中的所有文件拖拽到上传区域
4. 等待文件上传完成
5. 在Commit changes区域输入提交信息，如“Initial commit: AI Entrepreneur Story Website”
6. 点击“Commit changes”按钮

## 步骤3：启用GitHub Pages
1. 在仓库页面，点击“Settings”选项卡
2. 向下滚动到“Pages”部分
3. 在“Source”下拉菜单中选择“Deploy from a branch”
4. 选择“main”分支
5. 点击“Save”按钮
6. 页面会刷新，GitHub Pages会在几分钟内部署完成

## 步骤4：访问您的网站
部署完成后，您可以在以下地址访问您的网站：
https://aientrepreneurial.github.io/ai-entrepreneur-story/

注意：首次部署可能需要几分钟时间生效。

## 备用方案
如果上述方法不可行，您可以使用您之前提供的GitHub token通过命令行操作：
1. 打开命令提示符或Git Bash
2. 使用git clone命令克隆仓库
3. 将网站文件复制到仓库目录
4. 使用git add、git commit和git push命令推送更改