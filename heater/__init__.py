#import math
import torch
## Color Codes \e0m1
## Color Gradient \e00m1
## Scale down if needed to fit in window

def plot(input: Tensor, theme='heatmap') -> None:
    a  = input / input.abs().max()
    #a = torch.nn.functional.normalize(input)

    print(a)
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

## TODO More color range ( more than 5 slots )
## TODO more shade varients
## TODO User selectable shade values
shades = '░░▒▒▓'
shades = '░░▒▓█'
shades = '█████'
shades = '░▓▓██'
shades = '░░▒▒▓'
shades = '░░░▒▒'
shades = '░░░░░'
shades = ' ░▒▓█'
shades = '█████'
charmap = ' ░▒▓█'
themes = {
    '1'  : [24,36,48,120,156],
    'ocean'  : [23,35,47,119,155],
    'green'  : [22,34,46,118,154],
    'rainbow' : [19,27,36,118,196],
    'heatmap' : [55,127,198,208,220],
}
def OLDshade(value: float, shade=4, theme='heatmap') -> str:
    r = round(value.item() * 4)
    return f'\033[38;5;{themes[theme][r]}m' + charmap[lightness] + '\033[0m'

    print('▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█    ░▓▒▓█▒█')
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

    return f'\033[38;2;{r};{g};{b}m' + charmap[lightness] + '\033[0m'

def Gradshade(value: float, theme='heatmap', lightness=4) -> str:
    s = (55,27,198)
    f = (255,255,200)

    v = value.item()
    r = int(s[0] + (f[0] - s[0]) * v)
    g = int(s[1] + (f[1] - s[1]) * v)
    b = int(s[2] + (f[2] - s[2]) * v)

    return f'\033[38;2;{r};{g};{b}m' + charmap[lightness] + '\033[0m'


##   Code    Result  Description
##   U+2580  ▀       Upper half block
##   U+2581  ▁       Lower one eighth block
##   U+2582  ▂       Lower one quarter block
##   U+2583  ▃       Lower three eighths block
##   U+2584  ▄       Lower half block
##   U+2585  ▅       Lower five eighths block
##   U+2586  ▆       Lower three quarters block
##   U+2587  ▇       Lower seven eighths block
##   U+2588  █       Full block
##   U+2589  ▉       Left seven eighths block
##   U+258A  ▊       Left three quarters block
##   U+258B  ▋       Left five eighths block
##   U+258C  ▌       Left half block
##   U+258D  ▍       Left three eighths block
##   U+258E  ▎       Left one quarter block
##   U+258F  ▏       Left one eighth block
##   U+2590  ▐       Right half block
##   U+2591  ░       Light shade
##   U+2592  ▒       Medium shade
##   U+2593  ▓       Dark shade
#  
#  a = torch.rand(10,10)
#  heater.plot(a) __init__.py
# ▄▄▄▄▄▄▄▄▄▄▄▄
# █    ░▓▒▓█▒█
# █   ░▒▓█▒░ █
# █  ░▒▓█▒░  █
# █ ░▒▓█▒░   █
# ▀▀▀▀▀▀▀▀▀▀▀▀ ▒
# ▀▀▀▀▀▀▀▀▀▒▒▒▒▒▒
# ╭━━━━━━━━━━━━━━━━━━╮
# ┃░▒  ▓  ▇  ▒       ┃
# ┃ ▒  ▓             ┃
# ┃ ▒                ┃
# ┃ ▒  ▄             ┃
# ┃ ▒  ▅             ┃
# ┃ ▒  ▆             ┃
# ╰━━━━━━━━━━━━━━━━━━╯
# ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ─ │
# ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬ ═ ║
# ╭ ╮ ╯ ╰╯
# ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋ ━ ┃
# ▖

# ▗
# ▘
# ▙

# ▚

# ▛▀▀▀▀▀▀▀▀▄▄▄▄▜
# ▙▄▟

# ▜

# ▝
# ▞

# ▟
#  
# ▚
