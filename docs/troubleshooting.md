# Troubleshooting

## Nothing happens when I press the hotkey
1. Click `Set highlight hotkey` and press a letter once in the next 3 seconds. Did the field above the button update to 
`Highlight hotkey: ["'f'"]`, or something similar? If it didn't, the app probably does not have the permission to monitor keyboard input.
2. If the field has updated, try to assign highlight hotkey to one of the recommended options (`ctrl+alt+e` for win, `f10` for mac).
3. If it has updated to something like `['<Key.ctrl_l: <162>>', '<Key.alt_l: <164>>', '<69>']`, you can proceed to the next step.
4. Open a text editor, highlight a simple equation and press the hotkey you have just assigned.

Try restarting the application, if it didn't work

## It just types `c` and nothing else
Make sure you have chosen the correct OS. Don't forget to click the `Save` button after you change any settings above it.

## Wolfram mode does not work
You have probably not provided the app with a valid Wolfram appid

