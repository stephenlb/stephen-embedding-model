import torch
## Color Codes \e0m1
## Color Gradient \e00m1
## Scale down if needed to fit in window

def plot(input: Tensor) -> None:
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
            row.append(shade(value))
        row.append('█') # rigth border
        print(''.join(row))
    print(bottom)

shades = ' ░▒▓█'
colors = [22,34,46,118,154]
def shade(value: float) -> str:
    r = round(value.item() * 4)
    return f'\033[38;5;{colors[r]}m' + shades[r] + '\033[0m'

    


    
    print('▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█    ░▓▒▓█▒█')
    print('█   ░▒▓█▒░ █')
    print('█  ░▒▓█▒░  █')
    print('█ ░▒▓█▒░   █')
    print('▀▀▀▀▀▀▀▀▀▀▀▀')

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
