# part 1
import math

lines = []
math_probs = []
answers = []


with open('6_in.txt','r') as f:
    for line in f:
        line = line.strip()
        if line:
            lines.append(line.split())


cols = list(zip(*lines)) # accesing only vertical lines

for c in cols:
    *nums, operator = c
    nums = list(map(int, nums))
    math_probs.append((nums, operator)) # storing problems


for nums, operator in math_probs: # solving problems
    if operator == '+':
        answers.append(sum(nums))
    elif operator == '*':
        answers.append(math.prod(nums))

print(sum(answers))

# part 2
with open("6_in.txt") as f:
  lines = [line for line in f]
  cols = list(zip(*lines))
  cols.append(tuple())

  answer2 = 0
  nums = []
  op = None
  for col in cols:
      num_str = "".join(c for c in col if c.isdigit()) # extracts all digits from this column and treat them as one integer

      if not num_str:
          assert op
          answer2 += op(nums) # evalulates the problem
          op = None
          nums = []
          continue

      if op is None:
          op = {"+": sum, "*": math.prod}[col[-1]] # selects operator from the last char in the column

      nums.append(int(num_str))
  print(answer2)

