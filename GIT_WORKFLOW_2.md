# Git Branch Workflow for Developers

This document explains the standard Git workflow for our team using **prod** and **dev** branches.

---

## Branch Structure

* **prod** → The production branch. **Do not make changes directly here.**
* **dev** → The main development branch. All feature branches are created from here.
* **feature branches** → Each developer works in their own branch created from **dev**.

---

## Daily Workflow

### 1. Clone the repository (first time only)

```bash
# Replace with the actual repo URL
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

### 2. Create a feature branch from dev (first time for a new feature)

```bash
git checkout dev
git pull origin dev  # Make sure dev is up to date

# Create and switch to your feature branch
git checkout -b feature-yourname

# Push your new branch to GitHub
git push -u origin feature-yourname
```

---

## Daily Start (Before Working)

Every morning, make sure your feature branch is up to date with the latest changes from **dev**.

```bash
git checkout dev
git pull origin dev  # Get latest changes from dev

git checkout feature-yourname
git merge dev       # Merge those updates into your branch
# OR (if you prefer a cleaner history)
# git rebase dev
```

If there are merge conflicts, resolve them before continuing.

---

## During Development

Make commits regularly as you work.

```bash
git add .
git commit -m "Describe what you did"
git push origin feature-yourname
```

---

## When Your Feature Is Ready

Once your feature is complete and tested:

1. Ensure your branch is fully synced with **dev**:

   ```bash
   git checkout dev
   git pull origin dev
   git checkout feature-yourname
   git merge dev
   ```

2. Push your final version:

   ```bash
   git push origin feature-yourname
   ```

3. Open a **Pull Request (PR)** from your branch → **dev** in GitHub.

   * Title: `Feature: brief description`
   * Reviewers: Tag your team lead or reviewer.

---

## Merging to Dev

Once the PR is reviewed and approved, it will be merged into **dev**.

* Only maintainers or team leads should merge into **dev**.
* Never push directly to **dev** or **prod**.

---

## Summary

| Branch           | Purpose                   | Who Can Push         |
| ---------------- | ------------------------- | -------------------- |
| prod             | Production-ready code     | Leads only           |
| dev              | Active development branch | Leads only (via PRs) |
| feature-yourname | Individual developer work | Each developer       |

---

## Example Quick Commands

```bash
# Sync with dev before working
git checkout dev
git pull origin dev
git checkout feature-yourname
git merge dev

# Push changes
git push origin feature-yourname

# After approval, open PR → dev
```

---

Following this workflow ensures a clean, stable development process and minimizes conflicts between branches.
