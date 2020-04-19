def reveal(field, num_rows, num_cols, given_i, given_j):
    field[given_i][given_j] = -2
    for i in range((given_i - 1), (given_i + 2)):
        for j in range((given_j - 1), (given_j + 2)):
            if ((i >= 0) and (j >= 0) and (i < num_rows) and (j < num_cols)):
                #print("We are in location: " + str(i) + " " + str(j))
                #print("We are in element: " + str(field[i][j]))
                if(field[i][j] == 0):
                    reveal(field, num_rows, num_cols, i, j)
    return field
            

def click(field, num_rows, num_cols, given_i, given_j):
    if(field[given_i][given_j] == 0):
        reveal(field, num_rows, num_cols, given_i, given_j)
    return field

def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'
    
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(to_string(click(field1, 3, 5, 2, 2))))
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(to_string(click(field1, 3, 5, 1, 4)))
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


print(to_string(click(field2, 4, 4, 0, 1)))
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(to_string(click(field2, 4, 4, 1, 3)))
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
