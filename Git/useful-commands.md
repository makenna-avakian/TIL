# Useful Git Commands:

**git history**: To view a list of commands executed in the current Git session, you can use history. This command provides a chronological record of the commands you've run, helping you track your workflow.

**git log**: If you want to see a list of previous commits along with their commit messages, authors, and timestamps, use git log. This command provides a comprehensive overview of the commit history of your repository, aiding in understanding the evolution of the project.

**git status**: To check the status of your working directory and staging area, use git status. It allows you to see which files have been modified, staged for commit, or are untracked, helping you manage your changes effectively.

# Git Commits:

**git add**: Use git add to add changes from your working directory to the staging area in preparation for committing.
**git stash**: If you want to temporarily shelve changes in your working directory without committing them, you can use git stash.
**git stash pop**: To retrieve the most recently stashed changes from the stash and apply them to your working directory, use git stash pop.
**git stash save example-name**: You can save the current state of your working directory, including staged changes, with a custom label using git stash save.
**git reset**: To undo changes in your working directory or staging area, you can use git reset. Be cautious as it modifies the repository's history.
**git commit -v -m "commit message"**: This command allows you to commit changes with a verbose diff displayed, aiding in reviewing the changes being committed.
# Git Commit Messages:

Various commands can be used within the Git commit message editor:
:q to quit.
:w to write (save changes).
:qw to write and quit.
:q! to force quit without saving changes.
git reset --soft HEAD~1: Use this command to revert the last commit while preserving the changes in your working directory and staging area. It's less drastic than git reset with a commit hash, as it maintains the commit history.

**git commit --amend**: If you need to modify the last commit's message or include additional changes, you can use git commit --amend. This command combines staging changes and committing with the previous commit, effectively updating it.

**git diff**: To see the difference between the current state of your working directory and the staging area, use git diff. This command opens a Vim-like interface to display the changes.

**git add -p**: Use git add -p to selectively stage changes by interactively choosing which lines or chunks of code to add to the staging area.

**git reflog**: For a detailed history of reference updates in your repository, including commits, branches, merges, and resets, use git reflog. It provides a comprehensive log of all recent actions with corresponding hashes, aiding in navigating and recovering from mistakes.


