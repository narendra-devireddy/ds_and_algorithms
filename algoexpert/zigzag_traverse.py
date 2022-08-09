#not my solution
#solution by Clement is a lot cleaner
#o(N) complexity and o(N) Space
def zigzagTraverse(array):
    # Write your code here.
    height = len(array)-1
    width = len(array[0])-1
    row=col=0
    going_down = True
    result = []
    while row >=0 and row <= height and col >=0 and col <= width:
      result.append(array[row][col])
      if going_down:
        if col==0 or row==height:
          going_down=False
          if row==height:
            col+=1
          else:
            row+=1
        else:
          row+=1
          col-=1
      else:
        if row==0 or col==width:
          going_down=True
          if col==width:
            row+=1
          else:
            col+=1
        else:
          row-=1
          col+=1
    return result