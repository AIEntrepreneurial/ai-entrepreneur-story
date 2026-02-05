# PowerShell Deployment Script for AI Entrepreneur Story Website

# This script assumes:
# 1. You have git installed
# 2. You have set $env:GH_TOKEN environment variable with your GitHub Personal Access Token
# 3. The repository name is ai-entrepreneur-story under your account

$REPO_NAME = "ai-entrepreneur-story"
$GITHUB_USER = "aientrepreneurial"  # Replace with your GitHub username if different
$REPO_URL = "https://github.com/$GITHUB_USER/$REPO_NAME.git"

Write-Host "Starting deployment of AI Entrepreneur Story Website..." -ForegroundColor Green

# Check if GH_TOKEN is set
if (-not $env:GH_TOKEN) {
    Write-Host "Error: GH_TOKEN environment variable is not set." -ForegroundColor Red
    Write-Host "Please set it to your GitHub Personal Access Token before running this script." -ForegroundColor Red
    exit 1
}

# Check if we're in the correct directory
if (-not (Test-Path "index.html")) {
    Write-Host "Error: index.html not found in current directory." -ForegroundColor Red
    Write-Host "Please run this script from the ai-entrepreneur-story directory." -ForegroundColor Red
    exit 1
}

# Configure git
git config --global user.name "OpenClaw Assistant"
git config --global user.email "openclaw@example.com"

# Initialize git repo if not already initialized
if (-not (Test-Path ".git")) {
    Write-Host "Initializing git repository..."
    git init
}

# Add all files
Write-Host "Adding all files..."
git add .

# Commit changes
Write-Host "Committing changes..."
$commitResult = git commit -m "Deploy AI Entrepreneur Story Website"
if ($LASTEXITCODE -ne 0) {
    Write-Host "No changes to commit or other commit issue, continuing..."
}

# Set the remote origin
Write-Host "Setting remote origin..."
git remote set-url origin $REPO_URL

# Push to main branch
Write-Host "Pushing to GitHub..."
git push -u origin main --force

if ($LASTEXITCODE -eq 0) {
    Write-Host "Deployment successful!" -ForegroundColor Green
    Write-Host "Your website should be available at: https://$GITHUB_USER.github.io/$REPO_NAME/" -ForegroundColor Green
    Write-Host "Note: It may take a few minutes for GitHub Pages to process the deployment." -ForegroundColor Yellow
} else {
    Write-Host "Deployment failed. Please check your GitHub credentials and repository settings." -ForegroundColor Red
}