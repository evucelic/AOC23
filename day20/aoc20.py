from collections import deque
D = open("input.txt").read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])



TYP = {}

R = {}
for line in L:
  src, dest = line.split('->')
  src = src.strip()
  dest = dest.strip()
  dest = dest.split(', ')
  R[src] = dest
  TYP[src[1:]] = src[0]

FROM = {}

for x,ys in R.items():
  tmp = []
  for k in ys:
    if k in TYP:
      tmp.append(TYP[k] + k)
    else:
      tmp.append(k)
  R[x] = tmp
  for y in R[x]:
    if y[0]=='&':
      if y not in FROM:
        FROM[y] = {}
      FROM[y][x] = 'low'

low = 0 
high = 0
Q = deque()
ON = set()
PREV = {}

for t in range(1000):
  Q.append(('broadcaster', 'button', 'low'))

  while Q:
    x, from_, typ = Q.popleft()

    if typ=='low':
      low += 1
    else:
      high += 1

    if x not in R:
      continue
    if x=='broadcaster':
      for y in R[x]:
        Q.append((y, x, typ))
    elif x[0]=='%':
      if typ=='high':
        continue
      else:
        if x not in ON:
          ON.add(x)
          new_typ = 'high'
        else:
          ON.discard(x)
          new_typ = 'low'
        for y in R[x]:
          Q.append((y, x, new_typ))
    elif x[0]=='&':
      FROM[x][from_] = typ
      new_typ = ('low' if all(y=='high' for y in FROM[x].values()) else 'high')
      for y in R[x]:
        Q.append((y, x, new_typ))

print(low*high)

'''
Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens.
However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. 
If it was on, it turns off and sends a low pulse.

Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules;
they initially default to remembering a low pulse for each input. 
When a pulse is received, the conjunction module first updates its memory for that input.
Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
'''