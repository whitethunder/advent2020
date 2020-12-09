import pathlib
from dataclasses import dataclass


@dataclass
class Validator:
    data: list
    preamble_len: int
    buffer: set

    def run(self):
        for index, total in enumerate(data[preamble_len:]):
            if not self.valid(total):
                return(total)
            else:
                self.adjust_buffer(index)


    def valid(self, total):
        for first in self.buffer:
            if (total - first) in self.buffer:
                return True

        return False


    def adjust_buffer(self, index):
        self.buffer.remove(data[index])
        self.buffer.add(data[index + preamble_len])


@dataclass
class EncryptionWeaknessFinder:
    data: list
    invalid_num: int

    def run(self):
        for start_index in range(0, len(data)):
            end_index = start_index + 1

            while sum(data[start_index: end_index]) < invalid_num:
                end_index += 1

            if sum(data[start_index: end_index]) == invalid_num:
                return(min(data[start_index : end_index]) + max(data[start_index : end_index]))



with open(pathlib.Path(__file__).parent / 'input.txt') as file:
    data = file.read().splitlines()
    data = list(map(int, data))

preamble_len = 25

buffer = set(data[:preamble_len])
validator = Validator(data, preamble_len, buffer)
invalid_num = validator.run()
print(invalid_num)
#138879426

weakness = EncryptionWeaknessFinder(data, invalid_num).run()
print(weakness)
# 23761694
