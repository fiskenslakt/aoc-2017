from aocd import data


def solve_captcha(offset=1):
    total = 0

    for i, j in zip(data, data[offset:] + data[:offset]):
        if i == j:
            total += int(i)

    return total


print('Part 1:', solve_captcha())
print('Part 2:', solve_captcha(len(data)//2))
