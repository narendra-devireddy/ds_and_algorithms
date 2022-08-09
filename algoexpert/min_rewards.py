def minRewards(scores):
    # Write your code here.
    gifts_list=[1]*len(scores)
    if len(scores)==1:
      return sum(gifts_list)
    for ix in range(len(scores)):
      critical_elem = -1
      if ix == 0 and scores[ix] < scores[ix+1]:
        critical_elem = ix 
      elif ix == len(scores)-1 and scores[ix] < scores[ix-1]:
        critical_elem = ix
      elif scores[ix] < scores[ix-1] and scores[ix] < scores[ix+1]:
        critical_elem = ix
      if critical_elem != -1:
        print(critical_elem)
        left_traverse(critical_elem,scores, gifts_list)
        right_traverse(critical_elem, scores,gifts_list)
    print(gifts_list)
    return sum(gifts_list)

def left_traverse(ix, scores, gifts_count):
  left_ix = ix-1
  while left_ix >=0 and ((left_ix-1 >= 0 and scores[left_ix] > scores[left_ix-1] ) or \
                        scores[left_ix] > scores[left_ix+1]):
      if scores[left_ix] > scores[left_ix+1]:
        gifts_count[left_ix]=max(gifts_count[left_ix+1]+1,gifts_count[left_ix])
      left_ix-=1
  print(gifts_count)

def right_traverse(ix, scores, gifts_count):
  right_ix = ix+1
  while right_ix <len(scores) and ((scores[right_ix] > scores[right_ix-1]) or \
                        (right_ix+1 < len(scores) and scores[right_ix] > scores[right_ix+1])):
      if scores[right_ix] > scores[right_ix-1]:
        gifts_count[right_ix]=max(gifts_count[right_ix-1]+1,gifts_count[right_ix])
      right_ix+=1
  print(gifts_count)


  #---------------------------------#

  def minRewards(scores):
    # Write your code here.
    gifts = [1]*len(scores)
    for i in range(1,len(scores)):
      if scores[i] > scores[i-1]:
        gifts[i]=gifts[i-1]+1
    for i in reversed(range(len(scores)-1)):
      if scores[i] > scores[i+1]:
        gifts[i] = max(gifts[i],gifts[i+1]+1)
    
    return sum(gifts)