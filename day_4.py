# part 1
with open("4_in.txt", "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]

    height = len(grid)
    accessible_count = 0

    for row in range(height):
        curr_line = grid[row]
        width = len(curr_line)

        for col in range(width):
            if curr_line[col] != "@":
              continue

            adjacent_count = 0

            directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1),]

            for dr, dc in directions:
                neighbor_row = row + dr
                neighbor_col = col + dc

                if 0 <= neighbor_row < height and 0 <= neighbor_col < len(grid[neighbor_row]):
                    if grid[neighbor_row][neighbor_col] == "@":
                        adjacent_count += 1

            if adjacent_count < 4:
                accessible_count += 1

print(accessible_count)


# part 2
total_removed = 0

while True:
        cells_to_remove = []

        for row in range(height):
            curr_row = grid[row]
            width = len(curr_row)

            for col in range(width):
                if curr_row[col] != "@":
                    continue

                adjacent_count = 0

                for dr, dc in directions:
                    neighbor_row = row + dr
                    neighbor_col = col + dc

                    if 0 <= neighbor_row < height and 0 <= neighbor_col < len(grid[neighbor_row]):
                        if grid[neighbor_row][neighbor_col] == "@":
                            adjacent_count += 1

                if adjacent_count < 4:
                    cells_to_remove.append((row, col))

        if not cells_to_remove:
            break

        for row, col in cells_to_remove:
            grid[row][col] = "."

        total_removed += len(cells_to_remove)

print(total_removed)
