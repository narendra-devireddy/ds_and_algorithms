def mergeOverlappingIntervals(intervals):
    # Write your code here.
    result = []
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    i=0
    while i < len(intervals):
      interval_found=False
      interval_begin = intervals[i][0]
      j=i+1
      while not interval_found and j<len(intervals):
        if intervals[i][1] < intervals[j][0]:
          interval_found=True
        else:
          j+=1
          if intervals[i][1]<intervals[i+1][1]:
            i+=1
      interval_array = [interval_begin,max(intervals[i][1],intervals[j-1][1])]
      result.append(interval_array)
      i=j
    return result


### much simpler code from Algoexperts

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x:x[0])
    currentInterval=intervals[0]
    merged_intervals = []
    merged_intervals.append(currentInterval)
    for nextInterval in intervals:
      currentIntervalStart,currentIntervalEnd = currentInterval
      nextIntervalStart,nextIntervalEnd = nextInterval

      if currentIntervalEnd >= nextIntervalStart:
        currentInterval[1] = max(currentIntervalEnd,nextIntervalEnd)
      else:
        currentInterval=nextInterval
        merged_intervals.append(currentInterval)
  
    return merged_intervals