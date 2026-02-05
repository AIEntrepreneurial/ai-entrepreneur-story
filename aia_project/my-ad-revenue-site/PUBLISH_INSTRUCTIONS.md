# 发布到GitHub Pages的简化步骤

## 第一步：安装GitHub CLI（如果尚未安装）
访问 https://cli.github.com/ 下载并安装GitHub CLI

## 第二步：在命令行中登录GitHub
```
gh auth login
```
按照提示完成身份验证

## 第三步：在项目目录中运行以下命令
```
cd E:\aia\my-ad-revenue-site

# 如果仓库不存在，创建它
gh repo create my-ad-revenue-site --public --push --remote=upstream
```

## 第四步：启用GitHub Pages
```
gh pages enable
```

## 第五步：配置GitHub Pages使用main分支
```
gh pages configure --source=main
```

完成这些步骤后，你的网站将在 https://[你的用户名].github.io/my-ad-revenue-site/ 可访问

注意：首次部署可能需要几分钟时间生效。