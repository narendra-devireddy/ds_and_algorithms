def apartmentHunting(blocks, reqs):
    # Write your code here.
    result = [[len(blocks)]*len(reqs) for _ in range(len(blocks))]
    for i,block_details in enumerate(blocks):
      for j in range(len(reqs)):
        if block_details[reqs[j]] == True:
          result[i][j] = 0
        else:
          if i-1 >= 0:
            result[i][j] = min(result[i][j],result[i-1][j]+1)

    for i in reversed(range(len(blocks)-1)):
      for j in range(len(reqs)):
        result[i][j] = min(result[i][j],result[i+1][j]+1)
    max_distances = [max(x) for x in result]
    return max_distances.index(min(max_distances))
