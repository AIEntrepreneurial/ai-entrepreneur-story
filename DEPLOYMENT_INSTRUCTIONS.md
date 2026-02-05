# AI创业故事网站部署说明

## 部署步骤

### 1. 创建 GitHub 仓库
- 登录 GitHub
- 创建新仓库，命名为 `ai-entrepreneur-story`
- 组织设为 `aientrepreneurial` (或您的用户名)

### 2. 推送文件到仓库
```bash
cd C:\Users\39653\.openclaw\workspace\ai-entrepreneur-story
git init
git add .
git commit -m "Initial commit for AI Entrepreneur Story website"
git remote add origin https://github.com/aientrepreneurial/ai-entrepreneur-story.git
git branch -M main
git push -u origin main
```

### 3. 启用 GitHub Pages
- 在 GitHub 仓库中，转到 Settings > Pages
- Source 选择 "Deploy from a branch"
- Branch 选择 "main" 并保持根目录(/)
- 点击 Save

### 4. 等待部署完成
- GitHub Actions 会自动运行部署流程
- 部署完成后，网站将在 https://aientrepreneurial.github.io/ai-entrepreneur-story/ 上线

### 5. 验证网站
- 访问 https://aientrepreneurial.github.io/ai-entrepreneur-story/
- 确认所有页面都能正常访问

## 注意事项
- 仓库名称必须与 GitHub Pages URL 一致
- 确保 GitHub Actions 已启用
- 部署可能需要几分钟时间