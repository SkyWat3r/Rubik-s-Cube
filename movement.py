def test_movement_choice():
    import timeit
    import copy

    #print(timeit.timeit(lambda: movement_Uprime(copy.deepcopy(cube)), number=100))
    #print(timeit.timeit(lambda: movement_Uprime2(copy.deepcopy(cube)), number=100))

#test_movement_choice()

def rotate_face(cube, face, direction):
    """
    012
    345
    678

     R        L
    630      258
    741  OR  147
    852      036
    """

    save_cube = {0: cube[f"{face}"][0],
                 1: cube[f"{face}"][1],
                 2: cube[f"{face}"][2],
                 3: cube[f"{face}"][3],
                 4: cube[f"{face}"][4],
                 5: cube[f"{face}"][5],
                 6: cube[f"{face}"][6],
                 7: cube[f"{face}"][7],
                 8: cube[f"{face}"][8]
                 }

    if direction == "R":
        cube[f"{face}"][0] = save_cube[6]
        cube[f"{face}"][1] = save_cube[3]
        cube[f"{face}"][2] = save_cube[0]
        cube[f"{face}"][3] = save_cube[7]
        cube[f"{face}"][4] = save_cube[4]
        cube[f"{face}"][5] = save_cube[1]
        cube[f"{face}"][6] = save_cube[8]
        cube[f"{face}"][7] = save_cube[5]
        cube[f"{face}"][8] = save_cube[2]

    elif direction == "L":
        cube[f"{face}"][0] = save_cube[2]
        cube[f"{face}"][1] = save_cube[5]
        cube[f"{face}"][2] = save_cube[8]
        cube[f"{face}"][3] = save_cube[1]
        cube[f"{face}"][4] = save_cube[4]
        cube[f"{face}"][5] = save_cube[7]
        cube[f"{face}"][6] = save_cube[0]
        cube[f"{face}"][7] = save_cube[3]
        cube[f"{face}"][8] = save_cube[6]


def movement_D(cube):

    R, B, O, G = cube["R"][-3:], cube["B"][-3:], cube["O"][-3:], cube["G"][-3:]

    cube["R"][-3:] = G
    cube["B"][-3:] = R
    cube["O"][-3:] = B
    cube["G"][-3:] = O

    rotate_face(cube, "Y", "R")

def movement_Dprime(cube):

    R, B, O, G = cube["R"][-3:], cube["B"][-3:], cube["O"][-3:], cube["G"][-3:]

    cube["R"][-3:] = B
    cube["B"][-3:] = O
    cube["O"][-3:] = G
    cube["G"][-3:] = R

    rotate_face(cube, "Y", "L")

"""
#Too slow
def movement_Uprime2(cube):
    for i in range(3):
        movement_U(cube)
"""

def movement_U(cube):

    R, B, O, G = cube["R"][:3], cube["B"][:3], cube["O"][:3], cube["G"][:3]

    cube["R"][:3] = B
    cube["B"][:3] = O
    cube["O"][:3] = G
    cube["G"][:3] = R

    rotate_face(cube, "W", "R")

def movement_Uprime(cube):

    R, B, O, G = cube["R"][:3], cube["B"][:3], cube["O"][:3], cube["G"][:3]

    cube["R"][:3] = G
    cube["B"][:3] = R
    cube["O"][:3] = B
    cube["G"][:3] = O

    rotate_face(cube, "W", "L")

def movement_R(cube):

    W, B, Y, G = cube["W"][2::3][::-1], cube["B"][::3][::-1], cube["Y"][2::3], cube["G"][2::3]

    cube["W"][2::3] = G
    cube["B"][::3] = W
    cube["Y"][2::3] = B
    cube["G"][2::3] = Y

    rotate_face(cube, "R", "R")

def movement_Rprime(cube):

    W, B, Y, G = cube["W"][2::3], cube["B"][::3][::-1], cube["Y"][2::3][::-1], cube["G"][2::3]

    cube["W"][2::3] = B
    cube["B"][::3] = Y
    cube["Y"][2::3] = G
    cube["G"][2::3] = W

    rotate_face(cube, "R", "L")

def serie_movement(List, cube):

    movements = {"D": movement_D, "D'": movement_Dprime, "U": movement_U, "U'": movement_Uprime, "R": movement_R, "R'": movement_Rprime}
    #[R, U, R, D']
    for move in List:
        movements[move](cube)

    return cube



