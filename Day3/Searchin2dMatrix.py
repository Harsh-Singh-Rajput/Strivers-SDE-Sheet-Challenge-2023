def searchMatrix(mat, target: int) -> bool:
    row, col = len(mat), len(mat[0])
    curr_row, curr_col = row - 1, 0
    while(curr_row >= 0):
        if mat[curr_row][curr_col] == target:
            return True
        elif target < mat[curr_row][curr_col]:
            curr_row -= 1
        else:
            if curr_col < col:
                curr_col += 1
            if curr_col >= col:
                return False