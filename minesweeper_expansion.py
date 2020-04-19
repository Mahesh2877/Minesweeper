#Function to print a matrix in readable format - each row in a separate line
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'
            
#Function that is recursively called to check if a selected cell is zero and has to be expanded or not
#If the cell is zero, it is converted to "-2" and the function is recursively called on it's neighbouring cells.
#If the cell is non-zero, the function simply returns the matrix with no change
def click(field, num_rows, num_cols, given_i, given_j):
    if(field[given_i][given_j] == 0):
        field[given_i][given_j] = -2
        for i in range((given_i - 1), (given_i + 2)):
            for j in range((given_j - 1), (given_j + 2)):
                if ((i >= 0) and (j >= 0) and (i < num_rows) and (j < num_cols)):
                    click(field, num_rows, num_cols, i, j)
    return field


#We test the algorithm with two different input matrices    
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

#The expected output for each of the matrics is given below
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
