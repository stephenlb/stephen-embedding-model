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
        if a.ndim == 1:
            a = a.reshape(-1, 1)
    elif kind == 'Tensor':
        a = input / input.abs().max()
        if a.dim() == 1:
            a = a.unsqueeze(dim=1)
    elif kind in ('list', 'tuple'):
        if not input:
            return
        rows = input if isinstance(input[0], (list, tuple)) else [[v] for v in input]
        m = max(abs(float(v)) for row in rows for v in row) or 1.0
        a = [[float(v) / m for v in row] for row in rows]
    else:
        print(f"heater.plot: unsupported type {kind!r}, expected NumPy ndarray, PyTorch Tensor, or Python list/tuple")
        return

    width = len(a)
    height = len(a[0])
    top = '▄' * (width+2)
    bottom = '▀' * (width+2)
    print(top)
    for h in range(height):
        row = []
        row.append('█') # left border
        for w in range(width):
            value = a[w][h]
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
    'viridis' : [
        (68,1,84),
        (59,82,139),
        (33,145,140),
        (94,201,98),
        (253,231,37),
    ],
    'plasma' : [
        (13,8,135),
        (126,3,168),
        (203,71,119),
        (248,149,64),
        (240,249,33),
    ],
    'magma' : [
        (0,0,4),
        (81,18,124),
        (183,55,121),
        (251,136,97),
        (252,253,191),
    ],
    'inferno' : [
        (0,0,4),
        (87,16,110),
        (188,55,84),
        (249,142,9),
        (252,255,164),
    ],
    'fire' : [
        (0,0,0),
        (87,0,0),
        (200,30,0),
        (255,140,0),
        (255,240,100),
    ],
    'ocean' : [
        (3,5,26),
        (15,56,109),
        (47,119,167),
        (100,184,215),
        (220,240,255),
    ],
    'forest' : [
        (10,40,20),
        (30,90,50),
        (80,150,60),
        (180,210,80),
        (250,245,130),
    ],
    'coolwarm' : [
        (59,76,192),
        (133,165,224),
        (240,240,240),
        (244,154,123),
        (180,4,38),
    ],
    'grayscale' : [
        (0,0,0),
        (64,64,64),
        (128,128,128),
        (192,192,192),
        (255,255,255),
    ],
}

def shade(value: float, theme='heatmap', lightness=4) -> str:
    rgb = themes[theme]
    v = value.item() if hasattr(value, 'item') else float(value)
    p = round(v * (len(rgb) - 1))
    s = rgb[p]
    f = rgb[p]
    r = int(s[0] + (f[0] - s[0]) * v)
    g = int(s[1] + (f[1] - s[1]) * v)
    b = int(s[2] + (f[2] - s[2]) * v)
    return f'\033[38;2;{r};{g};{b}m█\033[0m'
