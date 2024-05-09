# Conflicts

## Identify Conflicts

When you encounter a conflict, Git will notify you. Use the git status command to see which files have conflicts.
Conflicting files will be marked as "both modified" in the status output.
##  Open Conflicting Files

Open the conflicting file(s) in your code editor. Git marks the conflicting sections within the file.

## Understand Conflict Markers

Git marks conflicts with special markers: <<<<<<<, =======, and >>>>>>>.
Everything between <<<<<<< and ======= represents changes from the current branch.
Everything between ======= and >>>>>>> represents changes from the incoming branch.

## Resolve Conflicts

Manually edit the conflicting sections to resolve differences.
Decide which changes to keep, modify, or discard.
Delete the conflict markers (<<<<<<<, =======, >>>>>>>) once you've resolved the conflict.

## Add and Commit Changes

Use git add <file> to stage the resolved file(s) for commit.
Once all conflicts are resolved, commit the changes using git commit.

For some Automatically generated files (like package-lock.json) it's always best to regenerate the file through npm install.