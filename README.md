Very simple first script, written because I wanted a ruler with marks on it (useful if you're copying a photo and trying to measure proportions in terms of "eye-width units" or some other convenient visual yardstick).

 * if you're not in a layer named "Ruler", it selects a layer named "Ruler" and activates the Transform tool
 * if you're in a layer named "Ruler", it switches back to whichever layer you were in previously, and activates whichever tool you were using previously

## Installation

Copy `toggle_ruler_layer.action` into the folder `~/.local/share/krita/actions/` on your computer (you may need to create it), and the file `toggle_ruler_layer.desktop` and folder `toggle_ruler_layer/` into the folder `~/.local/share/krita/pykrita/`, then restart Krita.

By default it uses the keyboard shortcut Alt+Ctrl+Shift+R, go to "Settings" menu > "Configure Krita..." > "Keyboard Shortcuts" > "Action: Scripts / My Scripts / Toggle Ruler Layer" to change that.