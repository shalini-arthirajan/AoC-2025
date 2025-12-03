part1 = 0
part2 = 0
def max_jolt(lst, length):
    jolt = ""
    while len(jolt) < length:
        highest = max(lst[:len(lst) - length + len(jolt) + 1]) # picking the largest digit from the slice
        jolt += str(highest)
        lst = lst[lst.index(highest) + 1:] # forming a sublist of what to consider in later iterations
    return int(jolt)

with open('3_in.txt','r') as f:
  for line in f:
      line = tuple(map(int, line.strip()))
      part1 += max_jolt(line, 2)
      part2 += max_jolt(line,12)
print(part1)
print(part2)
