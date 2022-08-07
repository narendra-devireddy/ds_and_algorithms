def spiralTraverse(array):
    # Write your code here.
    result = []
    spiralTraverseHelper(array,0,len(array)-1, 0, len(array[0])-1,result)
    return result

def spiralTraverseHelper(array,start_row, end_row,start_col,end_col,result):
    if start_row > end_row and start_col > end_col:
    	return
    for col in range(start_col,end_col+1):
    	result.append(array[start_row][col])
    for row in range(start_row+1,end_row+1):
     	result.append(array[row][end_col])
    for col in reversed(range(start_col,end_col)):
    	result.append(array[end_row][col])
    for row in reversed(range(start_row+1,end_row)):
     	result.append(array[row][start_col])
    spiralTraverseHelper(array,start_row+1,end_row-1,start_col+1,end_col-1,result)
