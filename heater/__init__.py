## TODO  Test Numpy it might work!!!!
## TODO Scale gradient to fit window
## TODO new Github repo ✅
## TODO Numpy Support ✅
## TODO Remove all Deps ✅
## TODO cleanup of __init__.py ✅
## TODO Examples and a README.md ✅
## TODO Create a package for Pypi ✅
## TODO More gradient themes
## TODO More Examples and a README.md
## TODO Actually use the lib for our origin intent
## TODO 
## TODO More Themes and Gradients
## TODO 
## TODO Scale down if needed to fit in window

def plot(input, theme='heatmap', lightness=4) -> None:
    kind = type(input).__name__
    if kind == "ndarray":
        a = input / input.max()
    elif kind == 'Tensor':
        a = input / input.abs().max()
        #a = a.unsqueeze(dim=1)
    else:
        return "Must be a Numpy ndarray or PyTorch Tensor"
        
    width, height = a.shape
    top = '▄' * (width+2)
    bottom = '▀' * (width+2)
    print(top)
    for h in range(height):
        row = []
        row.append('█') # left border
        for w in range(width):
            value = a[w,h]
            row.append(shade(value, theme))
        row.append('█') # rigth border
        print(''.join(row))
    print(bottom)

def sample():
    shades = ' ░▒▓█'
    print('▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█    ░▓▓█▒░█')
    print('█   ░▒▓█▒░ █')
    print('█  ░▒▓█▒░  █')
    print('█ ░▒▓█▒░   █')
    print('▀▀▀▀▀▀▀▀▀▀▀▀')

themes = {
    'heatmap' : [
        (86,13,168),
        (160,32,169),
        (234,51,134),
        (239,141,52),
        (249,216,73),
    ],
    'rainbow' : [
        (255,0,0),
        (255,128,0),
        (255,255,0),
        (0,255,0),
        (0,128,255),
        (0,255,255),
        (0,0,255),
        (110,0,180),
    ],
}

def shade(value: float, theme='heatmap', lightness=4) -> str:
    rgb = themes[theme]
    v = value.item()
    p = round(v * (len(rgb) - 1))
    s = rgb[p]
    f = rgb[p]
    r = int(s[0] + (f[0] - s[0]) * v)
    g = int(s[1] + (f[1] - s[1]) * v)
    b = int(s[2] + (f[2] - s[2]) * v)
    return f'\033[38;2;{r};{g};{b}m█\033[0m'
