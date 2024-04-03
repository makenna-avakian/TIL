Useful git commands:

- history: list of command from the current session
- git log: list of previous commits
- git status: see changes staged for commit or untracked files
- git commits
    git add: add files to commit
    git stash: revert changes
    git stash pop: revert stashed changes in memory
    git stash save example-name: saved working directory
    git reset: change status of git, everything gets reset. different that stash becuase it does not preserve log of commands. only resets added files.
    git commit -v -m "commit message": it means you're committing changes with a verbose diff displayed and providing a commit message directly from the command line
    Git commit messages:
        :q to quit
        :w to write
        :qw to write & quit
        :q! to force quit
    git reset --soft HEAD~1: git revert commits - tilda # number resets to specified commit (look in git log). soft preserves the log of the mistake (good!). this is less messy that git reset XXXXXXXX.
- git commit --amend: allows you to update the last commit, either the files or the message
- git diff: shows the changes in vim
- git add -p: lets you choose which lines to add to staging 
- git reflog: detailed version of git log with references with hashes. Able to grab hash for specific actions



