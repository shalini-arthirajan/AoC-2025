#part 1

sum = 0
with open('2_in.txt', 'r') as f:
    line = f.readline().strip().split(',')
    for item in line:
        a, b = map(int, item.split('-')) 
        for i in range(a, b + 1):  
            i_str = str(i) 
            if i_str[0] != '0': 
                half = len(str(b))//2
                if i_str[:half] == i_str[half:]:
                  print(i)
                  sum += i
print(sum)

#part 2

sum = 0
with open('2_in.txt', 'r') as f:
    line = f.readline().strip().split(',')
    for item in line:
        a, b = map(int, item.split('-')) 
        for i in range(a, b + 1):  
            i_str = str(i) 
            if i_str[0] != '0': 
              for length in range(1, len(i_str) // 2 + 1): 
                    pattern = i_str[:length]  
                    if pattern * (len(i_str) // length) == i_str: # checks if the pattern is recurring and forms original id
                        sum += i 
print(sum)

