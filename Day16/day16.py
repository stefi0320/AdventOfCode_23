from pathlib import Path
import time

def open_file_safely(file_name):
    """ File open """
    try:
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir / file_name

        with open(file_path, 'r', encoding="utf-8") as file:
            content = [line.strip() for line in file]
        return content

    except FileNotFoundError:
        print(
            "The file '{file_name}' was not found in the same directory as the script.")
        return None
    
def ray_tracing(grid, start) :
    n = len(grid)
    m = len(grid[0])

    point_stack = []
    point_stack.append(start)
    visited_points = []
    visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
    while len(point_stack) != 0:
        current = point_stack.pop()
        i = current[0]
        j = current[1]
        direction = current[2]
        direction = current[2]
       
        visited[i][j] = 1
        visited_points.append(current)
        
        match(direction):
            case 'up':
                if i > 0:
                    if (grid[i-1][j] ==  '.' or grid[i-1][j] == '|') and [i-1, j, 'up'] not in point_stack and [i-1, j, 'up'] not in visited_points:
                        point_stack.append([i-1, j, 'up']) # Move up        
                    elif grid[i-1][j] == '\\' and [i-1, j, 'left'] not in point_stack and [i-1, j, 'left'] not in visited_points:
                            point_stack.append([i-1, j, 'left']) # Move left
                    elif grid[i-1][j] == '/' and [i-1, j, 'right'] not in point_stack and [i-1, j, 'right'] not in visited_points:
                            point_stack.append([i-1, j, 'right']) # Move right
                    elif grid[i-1][j] == '-':
                        if [i-1, j, 'right'] not in point_stack and [i-1, j, 'right'] not in visited_points:
                            point_stack.append([i-1, j, 'right']) # Move right 
                        if [i-1, j, 'left'] not in point_stack and [i-1, j, 'left'] not in visited_points:
                            point_stack.append([i-1, j, 'left']) # Move left
            case 'down':
                if i < n-1:
                    if (grid[i+1][j] ==  '.' or grid[i+1][j] == '|') and [i+1, j, 'down'] not in point_stack and [i+1, j, 'down'] not in visited_points:
                        point_stack.append([i+1, j, 'down']) # Move down
                    elif grid[i+1][j] == '\\' and [i+1, j, 'right'] not in point_stack and [i+1, j, 'right'] not in visited_points:
                            point_stack.append([i+1, j, 'right']) # Move right
                    elif grid[i+1][j] == '/' and  [i+1, j, 'left'] not in point_stack and [i+1, j, 'left'] not in visited_points:
                            point_stack.append([i+1, j, 'left']) # Move left                          
                    elif grid[i+1][j] == '-':
                        if [i+1, j, 'right'] not in point_stack and [i+1, j, 'right'] not in visited_points:
                            point_stack.append([i+1, j, 'right']) # Move right 
                        if [i+1, j, 'left'] not in point_stack and [i+1, j, 'left'] not in visited_points:
                            point_stack.append([i+1, j, 'left']) # Move left

            case 'left':
                if j > 0:
                    if (grid[i][j-1] ==  '.' or grid[i][j-1] == '-') and  [i, j-1, 'left'] not in point_stack and [i, j-1, 'left'] not in visited_points:
                        point_stack.append([i, j-1, 'left']) # Move left
                    elif grid[i][j-1] == '\\' and  [i, j-1, 'up'] not in point_stack and [i, j-1, 'up'] not in visited_points:
                            point_stack.append([i, j-1, 'up']) # Move up                        
                    elif grid[i][j-1] == '/' and  [i, j-1, 'down'] not in point_stack and [i, j-1, 'down'] not in visited_points:
                            point_stack.append([i, j-1, 'down']) # Move down
                    elif grid[i][j-1] == '|':
                        if [i, j-1, 'up'] not in point_stack and [i, j-1, 'up'] not in visited_points:
                            point_stack.append([i, j-1, 'up']) # Move up
                        if [i, j-1, 'down'] not in point_stack and [i, j-1, 'down'] not in visited_points: 
                            point_stack.append([i, j-1, 'down']) # Move down
            case 'right':
                if j < m-1:
                    if (grid[i][j+1] ==  '.' or grid[i][j+1] == '-') and [i, j+1, 'right'] not in point_stack and [i, j+1, 'right'] not in visited_points:
                        point_stack.append([i, j+1, 'right']) # Move right
                    elif grid[i][j+1] == '\\' and [i, j+1, 'down'] not in point_stack and [i, j+1, 'down'] not in visited_points:
                            point_stack.append([i, j+1, 'down']) # Move down
                    elif grid[i][j+1] == '/' and [i, j+1, 'up'] not in point_stack and [i, j+1, 'up'] not in visited_points:
                            point_stack.append([i, j+1, 'up']) # Move up
                    elif grid[i][j+1] == '|':
                        if [i, j+1, 'up'] not in point_stack and [i, j+1, 'up'] not in visited_points:
                            point_stack.append([i, j+1, 'up']) # Move up
                        if [i, j+1, 'down'] not in point_stack and [i, j+1, 'down'] not in visited_points:
                            point_stack.append([i, j+1, 'down']) # Move down
    sum_nodes = 0                       
    for v in visited:
        for y in v:
          sum_nodes += y
    return sum_nodes

def check_start(item, direction, start):
    match(item):
        case '/': 
            match(direction):
                case 'left':
                    return 'up'
                case 'right':
                    return 'down'
                case 'up':
                    return 'right'
                case 'down':
                    return 'left'
        case '-':
            match(direction):
                case 'left':
                    return 'left'
                case 'right':
                    return 'right'
                case 'up':
                    if start == 'left':
                        return 'left'
                    if start == 'right':
                        return 'right'
                case 'down':
                    if start == 'left':
                        return 'left'
                    if start == 'right':
                        return 'right'
        case '\\':
            match(direction):
                case 'left':
                    return 'up'
                case 'right':
                    return 'down'
                case 'up':
                    return 'left'
                case 'down':
                    return 'right'
        case '|':
            match(direction):
                case 'left':
                    if start == 'up':
                        return 'up'
                    if start == 'down':
                        return 'down'
                case 'right':
                    if start == 'up':
                        return 'up'                    
                    if start == 'down':
                        return 'down'
                case 'up':
                    return 'up'
                case 'down':
                    return 'down'
        case '.':
            return direction

def day16():
    """Day 16 of Advent of code """
    # record start time
    start = time.time()
    input_txt = open_file_safely("day16.txt")
    
    mirror_grid = []
    
    for line in input_txt:
        mirror_grid.append(list(line))
   
    #left top corner
    tmp_start = check_start(mirror_grid[0][0], 'right', 'down')
    sum_nodes = ray_tracing(mirror_grid,[0,0,tmp_start])   
    print('Part 1: ', sum_nodes)
    row_len = len(mirror_grid)-1
    col_len = len(mirror_grid[0])-1
    sum_all = []
    sum_all.append(sum_nodes)
    #right bottom corner
    tmp_start = check_start(mirror_grid[row_len][col_len], 'left', 'up')
    sum_all.append(ray_tracing(mirror_grid,[row_len, col_len, tmp_start]))
    tmp_start2 = check_start(mirror_grid[row_len][col_len], 'up', 'left')
    if tmp_start!= tmp_start2:
        sum_all.append(ray_tracing(mirror_grid,[row_len, col_len, tmp_start2]))
    #right top corner
    tmp_start = check_start(mirror_grid[0][col_len], 'left', 'down')
    sum_all.append(ray_tracing(mirror_grid,[0, col_len, tmp_start]))
    tmp_start2 = check_start(mirror_grid[0][col_len], 'down', 'left')
    if tmp_start!= tmp_start2:
        sum_all.append(ray_tracing(mirror_grid,[0, col_len, tmp_start2]))
    #left bottom corner
    tmp_start = check_start(mirror_grid[row_len][0], 'right', 'up')
    sum_all.append(ray_tracing(mirror_grid,[row_len, 0, tmp_start]))
    tmp_start2 = check_start(mirror_grid[row_len][0], 'up', 'right')
    if tmp_start!= tmp_start2:
        sum_all.append(ray_tracing(mirror_grid,[row_len, 0, tmp_start2]))
    #left top corner
    tmp_start = check_start(mirror_grid[0][0], 'down', 'right')
    sum_all.append(ray_tracing(mirror_grid,[0,0,tmp_start]))  

    for i in range(1, row_len):
        tmp_start = check_start(mirror_grid[i][0], 'right', 'up')
        sum_all.append(ray_tracing(mirror_grid,[i,0,tmp_start]))
        tmp_start2 = check_start(mirror_grid[i][0], 'right', 'down')
        if tmp_start!= tmp_start2:
            sum_all.append(ray_tracing(mirror_grid,[i,0,tmp_start2])) 
        tmp_start = check_start(mirror_grid[i][col_len], 'left', 'up')
        sum_all.append(ray_tracing(mirror_grid,[i,col_len,tmp_start])) 
        tmp_start2 = check_start(mirror_grid[i][col_len], 'left', 'down')
        if tmp_start!= tmp_start2:
            sum_all.append(ray_tracing(mirror_grid,[i,col_len,tmp_start2])) 
    
    for i in range(1, col_len):
        tmp_start = check_start(mirror_grid[0][i], 'down', 'right')
        sum_all.append(ray_tracing(mirror_grid,[0, i, tmp_start]))
        tmp_start2 = check_start(mirror_grid[0][i], 'down', 'left')
        if tmp_start!= tmp_start2:
            sum_all.append(ray_tracing(mirror_grid,[0, i, tmp_start2])) 
        tmp_start = check_start(mirror_grid[row_len][i], 'up', 'right')
        sum_all.append(ray_tracing(mirror_grid,[row_len, i, tmp_start])) 
        tmp_start2 = check_start(mirror_grid[row_len][i], 'up', 'left')
        if tmp_start!= tmp_start2:
            sum_all.append(ray_tracing(mirror_grid,[row_len, i, tmp_start2])) 
    
    print('Part 2: ', max(sum_all))
    #record end time
    end = time.time()
    print("Runtime :", (end-start) * 10**3, "ms")

day16()