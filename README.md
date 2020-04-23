# fifteen
A terminal-based implementation of the 'fifteen' game

# Installation
```
git clone 'https://github.com/k-vernooy/fifteen'
```
On some terminals (including the macOS builtin terminal), you may have to tell the shell you are 256 color compatible, or `curses` will throw an error. To do so:
```
TERM=xterm-256color
```

# Usage

From inside the project directory:
```
python3 fifteen
```

To use different size boards:

```
python3 fifteen --board-size=x,y
```
Control is through the <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> keys.
