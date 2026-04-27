from colorama import *
init(autoreset=True)

colors = {
    "WHITE": Fore.LIGHTWHITE_EX + "⬛ ",
    "YELLOW": Fore.LIGHTYELLOW_EX + "⬛ " ,
    "BLUE": Fore.LIGHTBLUE_EX + "⬛ ",
    "GREEN": Fore.LIGHTGREEN_EX + "⬛ ",
    "ORANGE": Fore.LIGHTRED_EX + "⬛ ",
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
print("===================")
#print(colors)
print(cube)
print("===================")

order = "WGRBOY"

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

#view_cube(cube)


# {'W': ['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE'],
# 'Y': ['YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW'],
# 'B': ['BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE'],
# 'G': ['GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN'],
# 'R': ['RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED'],
# 'O': ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE']}

# TO ->

# {'W': ['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE'],
# 'Y': ['YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW'],
# 'B': ['BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'RED', 'RED', 'RED'],
# 'G': ['GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'ORANGE', 'ORANGE', 'ORANGE'],
# 'R': ['RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'GREEN', 'GREEN', 'GREEN'],
# 'O': ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'BLUE', 'BLUE', 'BLUE']}

cube2 = {'W': ['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE'], 'Y': ['YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW'], 'B': ['BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'RED', 'RED', 'RED'], 'G': ['GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'ORANGE', 'ORANGE', 'ORANGE'], 'R': ['RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'GREEN', 'GREEN', 'GREEN'], 'O': ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'BLUE', 'BLUE', 'BLUE']}

#view_cube(cube2)
def movement_U(cube):

    R, B, O, G = cube["R"][-3:], cube["B"][-3:], cube["O"][-3:], cube["G"][-3:]

    cube["R"][-3:] = G
    cube["B"][-3:] = R
    cube["O"][-3:] = B
    cube["G"][-3:] = O

movement_U(cube2)
movement_U(cube2)
movement_U(cube2)
view_cube(cube2)