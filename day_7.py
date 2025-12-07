# part 1

splits = 0
beams = list()
with open('7_in.txt','r') as f:
  for line in f:
      if "S" in line:
          beams = [0] * len(line)
          beams[line.index("S")] = 1
      if "^" in line:
          new_beams = [0] * len(line)
          for x, ch in enumerate(line):
              if ch == "^": # checks for splitter
                  new_beams[x-1] += beams[x]
                  new_beams[x+1] += beams[x]
                  if beams[x]:
                      splits += 1 
              else:
                  new_beams[x] += beams[x]
          beams = new_beams

print(splits)

# part 2

with open("7_in.txt","r") as f:
    grid = [list(line.strip()) for line in f]

def count_beam_paths(grid):
    rows = len(grid)
    cols = len(grid[0])

    # find S
    for start_col in range(cols):
        if grid[0][start_col] == "S":
            break

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # below grid
        if i == rows:
            return 1
        # out of bounds
        if j < 0 or j >= cols:
            return 0

        cell = grid[i][j]

        # checks for splitter
        if cell == "^":
            res = dfs(i+1, j-1) + dfs(i+1, j+1)
        else:
            res = dfs(i+1, j)

        memo[(i, j)] = res    # saves result
        return res

    print("Total exits:", dfs(1, start_col))

count_beam_paths(grid)
