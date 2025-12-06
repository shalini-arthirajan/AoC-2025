# part 1
count = 0
ranges = []

with open('5_in.txt','r') as f:
    for line in f:
        line = line.strip()

        if line == "":
            continue

        if '-' in line:
            a, b = map(int, line.split('-'))
            ranges.append((a, b))

        else:
            num = int(line)
            for a, b in ranges:
                if a <= num <= b:
                    count += 1
                    break

print(count)

# part 2 https://youtu.be/hG9QDwiE28w?si=LWYog_JMsv3bnI1B merged intervals reference

ranges = []

with open('5_in.txt','r') as f:
    for line in f:
        line = line.strip()
        if '-' in line:
            a,b = map(int,line.split('-'))
            ranges.append((a,b))

ranges.sort()

merged = []
current_start, current_end = ranges[0]

for a,b in ranges[1:]:
    if a <= current_end+1: # checking to see if they touch or overlap
        current_end = max(current_end,b)
    else:
        merged.append((current_start,current_end))
        current_start,current_end = a,b

merged.append((current_start,current_end))

total = 0

for start, end in merged:
    range_len = end - start + 1  # number of values in this interval
    total += range_len

print(total)




