# Git Workflow Guide for Developers

This guide explains the recommended Git workflow for working with our branches:

```
dev → feature-*
```

It includes **macOS/Linux** and **Windows** commands, organized by workflow stages: start of day, during the day, end of day, and pushing to `dev`.

---

## 1. Creating a New Branch

**Objective:**

* Make sure you are up-to-date with `dev`.
* Create or switch to your feature branch.

**macOS/Linux**

```bash
cd path/to/project
# Fetch latest changes
git fetch origin
# Switch to dev branch
git checkout dev
git pull origin dev
# Create a new feature branch if starting new work
git checkout -b feature-myfeature dev
```

**Windows (cmd/powershell)**

```powershell
cd path\to\project
git fetch origin
git checkout dev
git pull origin dev
git checkout -b feature-myfeature dev
```

---

## 2. Updating Your Branch from Dev

**Objective:**

* Regularly sync your feature branch with `dev` to prevent conflicts.
* Stage and commit changes frequently.

**macOS/Linux**

```bash
git branch                  # check current branch
git checkout feature-myfeature
git fetch origin
git merge origin/dev               # merge latest dev changes
git add .                   # stage changes
git commit -m "Short description of work"
git push origin feature-myfeature
```

**Windows**

```powershell
git branch
git checkout feature-myfeature
git fetch origin
git merge origin
git add .
git commit -m "Short description of work"
git push origin feature-myfeature
```

---

## 3. End of the Day

**Objective:**

* Make sure your feature branch is up-to-date.
* Push all changes to remote.

**macOS/Linux**

```bash
git checkout feature-myfeature
git fetch origin
git merge dev
git add .
git commit -m "End-of-day updates"
git push origin feature-myfeature
```

**Windows**

```powershell
git checkout feature-myfeature
git fetch origin
git merge dev
git add .
git commit -m "End-of-day updates"
git push origin feature-myfeature
```

---

## 4. Ready to Push to Dev (Merge Feature Branch)

**Objective:**

* Merge your completed feature branch into `dev` and push via a Pull Request.

**Recommended:** Use a Pull Request (PR) on GitHub/GitLab to merge `feature-*` into `dev`. Direct push is **not allowed**.

**macOS/Linux**

```bash
git checkout feature-myfeature
git fetch origin
git merge dev   # make sure branch is up-to-date
git push origin feature-myfeature
# Create Pull Request on GitHub/GitLab to merge into dev
```

**Windows**

```powershell
git checkout feature-myfeature
git fetch origin
git merge dev
git push origin feature-myfeature
# Create Pull Request on GitHub/GitLab to merge into dev
```

**Notes:**

* Always resolve merge conflicts before pushing to your feature branch.
* Ignore `.pyc` and `__pycache__/` files by adding to `.gitignore`:

```
*.pyc
__pycache__/
```

---

## 5. Helpful Commands

* Check status:

```bash
git status
```

* See recent commits:

```bash
git log --oneline --graph --decorate --all
```

* Switch branches:

```bash
git checkout branch-name
```

* Delete a local branch (after merging):

```bash
git branch -d feature-myfeature
```

* Delete a remote branch:

```bash
git push origin --delete feature-myfeature
```

---

> ⚠️ **Important:** Never make changes directly on `dev`. Always work on a `feature-*` branch and use Pull Requests to merge.
