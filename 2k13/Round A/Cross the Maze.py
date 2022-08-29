T = int(input())

def wall(grid, N, x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    return grid[x][y] == '#'

DIRECTIONS_COORDS = [(0, 1), (1,0), (0,-1), (-1,0)]
DIRECTIONS = ['E', 'S', 'W', 'N']

curr_direction = None

def turn_right():
    global curr_direction
    curr_direction += 1
    curr_direction %= 4

def turn_left():
    global curr_direction
    curr_direction -= 1
    curr_direction %= 4

for t in range(1, T+1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    sx, sy, ex, ey = tuple(map(int, input().split()))

    sx -= 1
    sy -= 1
    ex -= 1
    ey -= 1
    
    if (sx, sy) == (0,0):
        curr_direction = 0
    elif (sx, sy) == (0, N-1):
        curr_direction = 1
    elif (sx, sy) == (N-1, N-1):
        curr_direction = 2
    else:
        curr_direction = 3
    
    curr_pos = (sx, sy)
    steps = 0

    visited_directions = [[[False, False, False, False] for _ in range(N)] for _ in range(N)]
    
    found = True
    steps = 0
    path = ""

    while curr_pos != (ex, ey):
        curr_x, curr_y = curr_pos

        if visited_directions[curr_x][curr_y][curr_direction]:
            found = False
            break
        elif steps > 10000:
            found = False
            break
        
        visited_directions[curr_x][curr_y][curr_direction] = True
        dir_x, dir_y = DIRECTIONS_COORDS[curr_direction]

        if wall(grid, N, curr_x + dir_x, curr_y + dir_y):
            turn_right()
        else:
            curr_pos = (curr_x + dir_x, curr_y + dir_y)
            steps += 1
            path += DIRECTIONS[curr_direction]
            turn_left()

    if found:
        print(f"Case #{t}: {steps}")
        print(path)
    else:
        print(f"Case #{t}: Edison ran out of energy.")
