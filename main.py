from colorama import *
init(autoreset=True)

from movement import *
colors = {
    "WHITE": Fore.LIGHTWHITE_EX + "⬛ ",
    "YELLOW": Fore.LIGHTYELLOW_EX + "⬛ " ,
    "BLUE": Fore.LIGHTBLUE_EX + "⬛ ",
    "GREEN": Fore.LIGHTGREEN_EX + "⬛ ",
    "ORANGE": Fore.YELLOW + "⬛ ",
    "RED": Fore.RED + "⬛ "
}

cube = {
    "W": ["WHITE"] * 9,
    "Y": ["YELLOW"] * 9,
    "B": ["BLUE"] * 9,
    "G": ["GREEN"] * 9,
    "R": ["RED"] * 9,
    "O": ["ORANGE"] * 9
}
#print("===================")
#print(colors)
#print(cube)
#print("===================")

order = "WOGRBY"

def print_face_line(face, line):
    start = line * 3
    return "".join(colors[face[i]] for i in range(start, start + 3))

def view_cube(cube):
    for line in range(3):
        print("      " + print_face_line(cube[order[0]], line))

    for line in range(3):
        print(
            print_face_line(cube[order[1]], line) +
            print_face_line(cube[order[2]], line) +
            print_face_line(cube[order[3]], line) +
            print_face_line(cube[order[4]], line)
        )

    for line in range(3):
        print("      " + print_face_line(cube[order[5]], line))
    print()

def str_to_list(str):
    list = []
    next = False

    for i in range(len(str)):
        if next:
            next = False
            continue
        if i+1 < len(str) and str[i+1] == "'":
            list.append(str[i]+ "'")
            next = True
        else:
            list.append(str[i])
    return list


#cube2 = {'W': ['WHITE', 'WHITE', 'ORANGE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE'], 'Y': ['YELLOW', 'YELLOW', 'ORANGE', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW'], 'B': ['ORANGE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE'], 'G': ['GREEN', 'GREEN', 'ORANGE', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN'], 'R': ['RED', 'RED', 'ORANGE', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED'], 'O': ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE']}

moves = "URD'URUD'UD'UR"
serie_movement(str_to_list(moves), cube)

view_cube(cube)