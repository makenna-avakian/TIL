# Git Alias

Used to make shortcuts for git commands.

## Getting set up

Open your terminal and navigate to your root directory. (cd /)
To create the shorthand file, run:
`touch ~/.gitshorthand`

## Editing your file
You can edit your file in your terminal with:
`nano ~/.gitshorthand`

(After making your changes in Nano, press Ctrl + O. This will prompt you to confirm the file name to save. Press Enter to confirm the file name, then, press Ctrl + X to exit Nano.)

## Adding to .zshrc
Open your ~/.zshrc file in a text editor.
`nano ~/.zshrc`

At the end of your ~/.zshrc file, add the following line:
`source ~/.gitshorthand`

Save the ~/.zshrc file and reload the file to apply the changes. You can run:
`source ~/.zshrc`