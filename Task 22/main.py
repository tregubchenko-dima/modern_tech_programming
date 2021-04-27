maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]


def find_exits(pos, maze):
    lab = []
    for string in maze:
        lab.append(list(string))

    def get(pos, lab):
       return lab[pos[1]][pos[0]]

    if get(pos, lab) == '#':
        print('Не верные координаты')
        return

    if pos[1] < 0 or pos[1] >= len(lab[0]) or pos[0] < 0 or pos[0] >= len(lab):
        print('Не верные координаты')
        return

    def set(pos, lab, value):
       lab[pos[1]][pos[0]] = value

    exits = []

    def find_exit(pos, lab):
        cell = get(pos, lab)
        if cell == '#':
            return
        if cell == ' ':
            lab_copy = lab.copy()
            set(pos, lab_copy, '#')
            find_exit((pos[0] + 1, pos[1]), lab_copy)
            find_exit((pos[0] - 1, pos[1]), lab_copy)
            find_exit((pos[0], pos[1] + 1), lab_copy)
            find_exit((pos[0], pos[1] - 1), lab_copy)
            return
        exits.append(cell)
    find_exit(pos, lab)

    if len(exits) > 0:
        for i in exits:
            print(i, end=' ')
        print()
    else:
        print('Выхода нет')


try:
    x, y = map(int, input().split())
except ValueError:
    print("Вы ввели недопустимое значение")
    exit(1)

find_exits((x, y), maze)
