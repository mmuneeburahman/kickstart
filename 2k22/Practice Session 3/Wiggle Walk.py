deltas = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}
reverse = {
  "N": "S",
  "S": "N",
  "E": "W",
  "W": "E"
}
def add_jump(jumps, i, row, col):
  d_r, d_c = deltas[i]
  jumps[i] = (row+d_r, col+d_c)

def jump(table, dir, sr, sc):
  while (sr, sc) in table:
    if dir in table[(sr, sc)]:
      sr, sc = table[(sr, sc)][dir]
    else:
      d_r, d_c = deltas[dir]
      sr+=d_r
      sc+=d_c
  return sr, sc
  
T = int(input())
for t in range(T):
  N, R, C, sr, sc = map(int, input().split())
  table = {}
  sr-=1
  sc-=1
  table[(sr, sc)] = {}
  er, ec = sr, sc
  path = list(input())
  for dir in path:
    er, ec = jump(table, dir, sr, sc)
    table[(er, ec)] = {}
    add_jump(table[(er, ec)], reverse[dir], sr, sc)
    add_jump(table[(sr, sc)], dir, er, ec)
    sr, sc = er, ec
  print(f"Case #{t+1}: {sr+1} {sc+1}")