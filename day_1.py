# part 1
pos = 50
count = 0
total_0 = 0
with open('1_in.txt','r') as f:
  for line in f:
    num = int(line[1:])
    if line.startswith('L'):
      final_pos = (pos - num) % 100
    else:
     final_pos = (pos + num) % 100

    if final_pos == 0:
     count += 1

    pos = final_pos
  
  print(count)

  # part 2
with open('1_in.txt', 'r') as f:
    for line in f:
        num = int(line[1:]) 
        for _ in range(num): # moving one by one to see if we cross zero
          if line.startswith('L'):
           pos = (pos -1) % 100 # moves to the left
          else:
           pos = (pos + 1) % 100 # moves to the right

          if pos == 0:
            total_0 += 1
print(total_0)
   
      
