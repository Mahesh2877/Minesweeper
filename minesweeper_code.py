def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for i in bombs:
        field[i[0]][i[1]] = -1
    for i in bombs:
        for x in range((i[0] - 1), (i[0] + 2), 1):
            for y in range((i[1] - 1), (i[1] + 2), 1):
                if not((x < 0) or (x > (num_rows - 1)) or (y < 0) or (y > (num_cols - 1))):
                    if not(field[x][y] == -1):
                        field[x][y] += 1
    return(field)
    
print(mine_sweeper([[0, 2], [2, 0]], 3, 3))
print(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4))
print(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))
