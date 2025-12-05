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


