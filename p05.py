from aocd import data


class CPU:
    def __init__(self, jumps):
        self.jumps = [int(jump) for jump in jumps]

    def execute(self):
        i = 0
        steps = 0
        while i < len(self.jumps):
            steps += 1
            next_op = self.jumps[i] + i
            self.jumps[i] += 1
            i = next_op

        return steps

    def execute_long(self):
        i = 0
        steps = 0
        while i < len(self.jumps):
            steps += 1
            next_op = self.jumps[i] + i
            if self.jumps[i] >= 3:
                self.jumps[i] -= 1
            else:
                self.jumps[i] += 1

            i = next_op

        return steps


cpu = CPU(data.splitlines())
steps = cpu.execute()
print('Part 1:', steps)

cpu = CPU(data.splitlines())
steps = cpu.execute_long()
print('Part 2:', steps)
