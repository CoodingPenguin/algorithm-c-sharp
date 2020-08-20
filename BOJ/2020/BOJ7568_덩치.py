def weight_rank(pList):
      rank = [1] * len(pList)
  for i in range(len(pList)):
    for j in range(0, i):
      if pList[i]['weight'] > pList[j]['weight']  and pList[i]['height'] > pList[j]['height']:
        rank[j] += 1
      elif pList[i]['weight'] < pList[j]['weight'] and pList[i]['height'] < pList[j]['height']:
        rank[i] += 1 
  return rank


pList = list()
for i in range(int(input())):
  x, y = map(int, input().split())
  pList.append({'weight':x, 'height':y})
rank = map(str, weight_rank(pList))
print(' '.join(rank))