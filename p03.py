from itertools import cycle

from aocd import data


class Memory:
    def __init__(self):
        self.stream = 0j
        self.address = 1
        self.step = 1
        self.data = {0j: 1}

    def _move_right(self):
        self.stream += 1
        self.address += 1

    def _move_up(self):
        self.stream += 1j
        self.address += 1

    def _move_left(self):
        self.stream -= 1
        self.address += 1

    def _move_down(self):
        self.stream -= 1j
        self.address += 1

    def _increment_step(self):
        self.step += 1

    def _traverse_memory(self):
        instructions = [
            self._move_right,
            self._move_up,
            self._increment_step,
            self._move_left,
            self._move_down,
            self._increment_step,
        ]
        for instruction in cycle(instructions):
            if instruction == self._increment_step:
                instruction()
                continue
            for _ in range(self.step):
                instruction()
                yield

    def reset_to_access_point(self):
        self.stream = 0j
        self.address = 1
        self.step = 1

    def stress_test(self, target):
        for _ in self._traverse_memory():
            address_value = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # neighboring addresses
                    n_address = complex(self.stream.real + i,
                                        self.stream.imag + j)
                    address_value += self.data.get(n_address, 0)

            if address_value > target:
                return address_value
            else:
                self.data[self.stream] = address_value

    def find_address(self, target):
        for _ in self._traverse_memory():
            if self.address == target:
                return self.stream


memory = Memory()
address = memory.find_address(int(data))
steps = int(abs(address.real) + abs(address.imag))
print('Part 1:', steps)

memory.reset_to_access_point()
value = memory.stress_test(int(data))
print('Part 2:', value)
