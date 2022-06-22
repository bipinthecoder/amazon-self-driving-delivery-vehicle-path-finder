# importing necessary packages
import random


# function to get the directions to the target coordinate
def get_directions(tgt, obs, n):
    x, y = 0, 0  # initial Coordinates

    blocker_dict = {}  # Dict to keep track of permanent block

    blocker_flag = False  # To track the current coordinate block status

    key = random.randint(0, 7)  # Initializing key randomly. Based on key value direction of traversal is decided.
    path_tracer = [(0, 0)]  # list of coordinates traversed

    while (x, y) != tgt:
        new_coordinate = (x, y)
        # logic for manual redirection to lower complexity of random pick by interpreter in a worst case scenario
        if not blocker_flag:
            if x < tgt[0]:
                key = random.choice([2, 4, 5, 0])
            elif x > tgt[0]:
                key = random.choice([3, 6, 7])
            elif x == tgt[0]:
                if y < tgt[1]:
                    key = 0
                else:
                    key = 1
                # key = random.choice(([0, 1]))
        else:
            key = random.randint(0, 7)  # Re-Pivoting since there is a blocker
            blocker_flag = False

        if path_tracer[-1] != new_coordinate:
            path_tracer.append(new_coordinate)

        # Logic for traversing based on key value
        if key == 0:
            x, y = move_horizontal_right(x, y, n - 1)
        elif key == 1:
            x, y = move_horizontal_left(x, y, n - 1)
        elif key == 2:
            x, y = move_vertical_down(x, y, n - 1)
        elif key == 3:
            x, y = move_vertical_up(x, y)
        elif key == 4:
            x, y = move_diagonal_right_down(x, y, n - 1)
        elif key == 5:
            x, y = move_diagonal_left_down(x, y, n - 1)
        elif key == 6:
            x, y = move_diagonal_right_up(x, y, n - 1)
        elif key == 7:
            x, y = move_diagonal_left_up(x, y)

        # handling blockers en route
        if obs.__contains__((x, y)):
            blocker_flag = True
            if new_coordinate not in blocker_dict:
                blocker_dict[new_coordinate] = 0
            else:
                blocker_dict[new_coordinate] += 1
                if blocker_dict[new_coordinate] > 200:  # Randomly assigned a higher value to capture real deadlocks due
                    # to blockers in the path
                    return "unable to reach delivery point"
            # print(f"Blocker found at {x},{y}")
            x, y = new_coordinate  # Reverting coordinates to previous state since a blocker is found

    # appending final destination to the path_tracer and returning the sequence with the total number of steps
    path_tracer.append((x, y))
    return path_tracer, (len(path_tracer) - 1)


# function to handle horizontal right movement
def move_horizontal_right(x1, y1, k):
    if y1 < k:
        y1 += 1
    return x1, y1


# function to handle horizontal left movement
def move_horizontal_left(x2, y2, k):
    if y2 > 0:
        y2 -= 1
    return x2, y2


# function to handle vertical down movement
def move_vertical_down(x3, y3, k):
    if x3 < k:
        x3 += 1
    return x3, y3


# function to handle vertical up movement
def move_vertical_up(x4, y4):
    if x4 > 0:
        x4 -= 1
    return x4, y4


# function to handle diagonal right down movement
def move_diagonal_right_down(x5, y5, k):
    if x5 < k and y5 < k:
        x5 += 1
        y5 += 1
    return x5, y5


# function to handle diagonal left down movement
def move_diagonal_left_down(x6, y6, k):
    if x6 < k and y6 > 0:
        x6 += 1
        y6 -= 1
    return x6, y6


# function to handle diagonal right up movement
def move_diagonal_right_up(x7, y7, k):
    if x7 > 0 and y7 < k:
        x7 -= 1
        y7 += 1
    return x7, y7


# function to handle diagonal left up movement
def move_diagonal_left_up(x8, y8):
    if x8 > 0 and y8 > 0:
        x8 -= 1
        y8 -= 1
    return x8, y8


# setting Target and obstacles
target = (9, 9)
obstacles = [(9, 7), (8, 7), (6, 7), (6, 8)]


# Calling the main direction function
def get_minimum_obstacle_path():
    compare_dict = {}
    count_list = []
    blocked_flag = False
    final_steps_list = []
    final_steps_count = 0
    for i in range(0, 50):
        trial_result = get_directions(target, obstacles, 10)
        if type(trial_result) == str:
            blocked_flag = True
        else:
            blocked_flag = False
            compare_dict[trial_result[1]] = trial_result[0]
            count_list.append(trial_result[1])

    if not blocked_flag:
        minimum = min(count_list)
        for count, steps in compare_dict.items():
            if count == minimum:
                final_steps_list = steps
                final_steps_count = count
                break
        print(final_steps_list)
        print(f"No. of steps are {final_steps_count}")
    else:
        print("unable to reach delivery point")


# calling the driver function
get_minimum_obstacle_path()
