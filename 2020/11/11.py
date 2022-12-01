#!/usr/local/bin/python3

initial_grid = list(map(lambda row: [char for char in row], open("11-data.txt", "r").read().split("\n")))

def count_occupied_seats(grid, x, y):
    def lookatseat(i, j):
        if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid):
            return False
        return grid[j][i] == '#'
    seats = list(map(lambda offset: lookatseat(x+offset[0], y+offset[1]), [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]))
    return sum(seats)

def count_occupied_seats_part2(grid, x, y):
    def is_valid_coordinates(x, y):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return False
        return True

    def occupied_in_direction(grid, x, y, direction):
        factor = 1
        while is_valid_coordinates(x+direction[0]*factor, y+direction[1]*factor):
            spot = grid[y+direction[1]*factor][x+direction[0]*factor]
            if '#' == spot:
                return True
            if 'L' == spot:
                return False
            factor += 1
        return False

    occupied = 0
    for direction in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
        if occupied_in_direction(grid, x, y, direction):
            occupied += 1
    return occupied

def simulate_step(grid):
    next = [['_' for i in range(len(grid[0]))] for i in range(len(grid))]
    changed = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.':
                next[y][x] = '.'
            else:
                occupied = count_occupied_seats_part2(grid, x, y)
                if 0 == occupied and grid[y][x] == 'L':
                    next[y][x] = '#'
                    changed = True
                elif occupied >= 5 and grid[y][x] == '#':
                    next[y][x] = 'L'
                    changed = True
                else:
                    next[y][x] = grid[y][x]
    return next, changed

def print_grid(grid):
    for row in range(len(grid)):
        print("".join(grid[row]))

def simulate(init_grid):
    changed = True
    grid = init_grid
    while changed:
        grid, changed = simulate_step(grid)
    print_grid(grid)
    return grid

def total_seats_occupied(grid):
    occupied = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                occupied += 1
    return occupied

final_grid = simulate(initial_grid)
print("Final grid has {0} seats occupied".format(total_seats_occupied(final_grid)))
