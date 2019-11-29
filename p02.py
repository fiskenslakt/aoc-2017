from itertools import combinations

from aocd import data


rows = data.splitlines()
checksum = 0
divisible_sum = 0

for row in rows:
    numbers = [int(n) for n in row.split()]
    checksum += max(numbers) - min(numbers)
    for combo in combinations(numbers, 2):
        if max(combo) % min(combo) == 0:
            divisible_sum += max(combo) // min(combo)
            break

print('Part 1:', checksum)
print('Part 2:', divisible_sum)
