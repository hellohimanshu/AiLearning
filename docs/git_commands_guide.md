# Git Commands Guide - AI Learning Project

## 📚 Introduction

This guide explains all the Git commands we used to set up your AI Learning project. Think of Git as a "time machine" for your code that saves every version of your work.

## 🎯 What is Git?

**Git** is a version control system that helps you:
- Track changes in your code
- Save different versions of your work
- Collaborate with others
- Keep your code safe online

## 📋 Basic Git Commands We Used

### 1. **git init** - Start a New Git Repository
```bash
git init
```
**What it does:** Creates a new Git repository in your current folder
**Impact:** Your folder becomes a Git repository (creates a hidden `.git` folder)
**When to use:** Only once when starting a new project

### 2. **git config** - Set Up Your Identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
**What it does:** Tells Git who you are
**Impact:** Git will use this information for all your commits
**When to use:** Once when setting up Git on a new computer

### 3. **git add** - Stage Files for Commit
```bash
git add filename.txt          # Add specific file
git add .                     # Add all files
git add *.py                  # Add all Python files
```
**What it does:** Prepares files to be saved (committed)
**Impact:** Files are staged and ready to be committed
**When to use:** Every time you want to save changes

### 4. **git commit** - Save Your Changes
```bash
git commit -m "Your message here"
```
**What it does:** Saves a snapshot of your current work
**Impact:** Creates a permanent record of your changes
**When to use:** After adding files, when you want to save your progress

### 5. **git status** - Check Current State
```bash
git status
```
**What it does:** Shows what files have changed and what's staged
**Impact:** Helps you understand what Git is tracking
**When to use:** Anytime you want to see what's happening

### 6. **git branch** - Manage Different Versions
```bash
git branch                    # List all branches
git branch -M main           # Rename current branch to 'main'
```
**What it does:** Manages different versions of your code
**Impact:** Allows you to work on different features separately
**When to use:** When you want to organize your work

### 7. **git remote** - Connect to Online Storage
```bash
git remote add origin https://github.com/username/repository.git
git remote -v                # View connected repositories
```
**What it does:** Connects your local folder to GitHub
**Impact:** Enables uploading/downloading code to/from the internet
**When to use:** Once when setting up a new project

### 8. **git push** - Upload to GitHub
```bash
git push origin main
git push -u origin main      # Set up tracking (first time)
```
**What it does:** Uploads your local changes to GitHub
**Impact:** Your code is now safely stored online
**When to use:** When you want to backup or share your code

## 🔄 Complete Workflow Example

Here's the typical workflow we followed:

```bash
# 1. Initialize repository
git init

# 2. Configure your identity (one-time setup)
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# 3. Add files to staging
git add .

# 4. Commit your changes
git commit -m "Initial project setup"

# 5. Connect to GitHub
git remote add origin https://github.com/username/repository.git

# 6. Push to GitHub
git push -u origin main
```

## 📁 Important Files We Created

### `.gitignore`
- **Purpose:** Tells Git which files to ignore
- **Why important:** Prevents unnecessary files from being tracked
- **Example:** Ignores temporary files, virtual environments, etc.

### `README.md`
- **Purpose:** Documentation for your project
- **Why important:** Explains what your project does
- **Example:** Project description, setup instructions, usage guide

### `requirements.txt`
- **Purpose:** Lists all Python packages needed
- **Why important:** Makes it easy to install dependencies
- **Example:** numpy, pandas, tensorflow, etc.

## 🚨 Common Issues and Solutions

### Issue: "git is not recognized"
**Solution:** Install Git from https://git-scm.com/

### Issue: "Author identity unknown"
**Solution:** Run git config commands to set your name and email

### Issue: Push fails with authentication
**Solution:** You may need to authenticate with GitHub (browser will open)

### Issue: "fatal: remote origin already exists"
**Solution:** Use `git remote set-url origin new-url` to change the URL

## 📖 Additional Useful Commands

### View History
```bash
git log                     # Show commit history
git log --oneline          # Compact history view
```

### Undo Changes
```bash
git checkout -- filename   # Undo changes in a file
git reset --hard HEAD      # Undo all changes (DANGEROUS!)
```

### Update from GitHub
```bash
git pull origin main       # Download latest changes
```

### Create New Branch
```bash
git checkout -b new-feature  # Create and switch to new branch
git checkout main            # Switch back to main branch
```

## 🎯 Best Practices

1. **Commit Often**: Save your work frequently
2. **Use Clear Messages**: Write descriptive commit messages
3. **Check Status**: Use `git status` before committing
4. **Pull Before Push**: Always get latest changes before pushing
5. **Use Branches**: Work on new features in separate branches

## 📝 Quick Reference Card

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `git init` | Start new repository | New project |
| `git add .` | Stage all files | Before committing |
| `git commit -m "msg"` | Save changes | After adding files |
| `git push` | Upload to GitHub | After committing |
| `git status` | Check state | Anytime |
| `git pull` | Download changes | Before starting work |

## 🔗 Useful Resources

- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

**Remember:** Git is like a safety net for your code. It saves every version, so you can always go back if something goes wrong!

**Last Updated:** July 30, 2025
**Project:** AI Learning Repository Setup 