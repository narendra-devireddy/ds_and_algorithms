#o(n^2) time complexity | o(n) space complexity
def lineThroughPoints(points):
    # Write your code here.
    max_points = 1
    for i in range(len(points)):
      x1,y1 = points[i]
      slope_intercept_dict = dict()
      for j in range(i+1,len(points)):
        x2,y2 = points[j]
        #slope
        if x2-x1 == 0:
          slope = float('inf')
        else:
          slope = (y2-y1)/(x2-x1)
        # intercept - for infinite slope, store x coordinate
        if slope!=float('inf'):
          intercept = y1-(slope*x1)
        else:
          intercept = x1

        if (slope,intercept) in slope_intercept_dict: 
          point_count= slope_intercept_dict[(slope,intercept)]+1
          slope_intercept_dict[(slope,intercept)]=point_count
          max_points = max(max_points,point_count)
        else:
          slope_intercept_dict[(slope,intercept)]=2
          max_points = max(max_points,2)
    return max_points