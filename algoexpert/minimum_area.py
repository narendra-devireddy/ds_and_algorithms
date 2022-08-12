# space complexity o(n)|time complexity o(n^2)
def minimumAreaRectangle(points):
    # Write your code here.
    point_set = set()
    min_area = float('inf')
    for point in points:
      x, y = point
      point_set.add((x,y))
    # find points that are different 
    # we deterministically know what other points must be
    for i,point in enumerate(points):
      x1, y1 = point
      for j in range(i+1, len(points)):
        x2, y2 = points[j]
        if x1 == x2 or y1 == y2:
          continue
        other_point1 = (x1, y2)
        other_point2 = (x2, y1)
        if other_point1 in point_set and other_point2 in point_set:
          current_area = abs((y1-y2)*(x1-x2))
          min_area = min(min_area,current_area)
    if min_area == float('inf'):
        min_area = 0
    return min_area