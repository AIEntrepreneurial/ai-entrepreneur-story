#!/bin/bash
# GitHub Pages Deployment Script for AI Entrepreneur Story Website

# This script assumes:
# 1. You have git installed
# 2. You have set GH_TOKEN environment variable with your GitHub Personal Access Token
# 3. The repository name is ai-entrepreneur-story under your account

REPO_NAME="ai-entrepreneur-story"
GITHUB_USER="aientrepreneurial"  # Replace with your GitHub username if different
REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "Starting deployment of AI Entrepreneur Story Website..."

# Check if GH_TOKEN is set
if [ -z "$GH_TOKEN" ]; then
    echo "Error: GH_TOKEN environment variable is not set."
    echo "Please set it to your GitHub Personal Access Token before running this script."
    exit 1
fi

# Check if we're in the correct directory
if [ ! -f "index.html" ]; then
    echo "Error: index.html not found in current directory."
    echo "Please run this script from the ai-entrepreneur-story directory."
    exit 1
fi

# Configure git
git config --global user.name "OpenClaw Assistant"
git config --global user.email "openclaw@example.com"

# Initialize git repo if not already initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files
echo "Adding all files..."
git add .

# Commit changes
echo "Committing changes..."
git commit -m "Deploy AI Entrepreneur Story Website" || echo "No changes to commit"

# Set the remote origin
echo "Setting remote origin..."
git remote set-url origin $REPO_URL

# Push to main branch
echo "Pushing to GitHub..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
    echo "Your website should be available at: https://$GITHUB_USER.github.io/$REPO_NAME/"
    echo "Note: It may take a few minutes for GitHub Pages to process the deployment."
else
    echo "Deployment failed. Please check your GitHub credentials and repository settings."
fi