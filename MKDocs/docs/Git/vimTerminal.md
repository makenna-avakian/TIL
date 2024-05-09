## Vim mode in Terminal 

In Unix-based systems, you can use the 'set -o vi' command to enable Vim mode in the terminal. This allows you to use Vim keybindings for command-line editing. 

To enable Vim mode in the terminal, run the following command:

```bash
nano ~/.zshrc
```

And add the following line to the file:
```bash
set -o vi
```


Once Vim mode is enabled, you can use the following keybindings:

- `Esc`: Switch to command mode from input mode.
- `b`: Move the cursor back one word.
- `w`: Move the cursor forward one word.
- `a`: Switch to input mode after the cursor.
