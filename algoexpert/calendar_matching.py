def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    calendar1.insert(0,["00:00", dailyBounds1[0]])
    calendar1.append([dailyBounds1[1],"24:00"])
    calendar2.insert(0,["00:00", dailyBounds2[0]])
    calendar2.append([dailyBounds2[1],"24:00"])
    busy_calendar = []
    result = []
    c1_ix = 0
    c2_ix = 0
    while c1_ix < len(calendar1) and c2_ix < len(calendar2):

      if c1_ix < len(calendar1) and c2_ix <len(calendar2):
        start_time = min(calendar1[c1_ix][0],calendar2[c2_ix][0])
      elif c1_ix < len(calendar1):
        start_time = calendar1[c1_ix][0]
      else:
        start_time = calendar2[c2_ix][0]

      #index out of bounds possibility
      while c1_ix+1<len(calendar1) and  calendar1[c1_ix][1] >=  calendar1[c1_ix+1][0]:
        c1_ix+=1
      while c2_ix+1<len(calendar2) and calendar2[c2_ix][1] >=  calendar2[c2_ix+1][0]:
        c2_ix+=1
      if c1_ix < len(calendar1) and c2_ix <len(calendar2):
        end_time = max(calendar1[c1_ix][1],calendar2[c2_ix][1])
      elif c1_ix < len(calendar1):
        end_time = calendar1[c1_ix][1]
      else:
        end_time = calendar2[c2_ix][1]

      c1_ix+=1
      c2_ix+=1
      busy_calendar.append([start_time,end_time])
    print(busy_calendar)
    for i in range(1,len(busy_calendar)):
      start_ = busy_calendar[i-1][1]
      end_ = busy_calendar[i][0]
      if meetingDuration <= int(end.replace(':','')) - int(start_.replace(':','')):
        results.append([start_,end_])
  return results
      