def change_instruction(index):
    instruction = instructions[index]
    if instruction[:3] == 'jmp':
        instructions[index] = instruction.replace('jmp', 'nop')
    elif instruction[:3] == 'nop':
        instructions[index] = instruction.replace('nop', 'jmp')


def run(instructions, pointer, accum, seen):
    while True:
        if pointer in seen:
            return accum, False
        else:
            seen.add(pointer)

        instruction, value = instructions[pointer].split()
        value = int(value)

        if instruction == 'acc':
            accum += value
            pointer += 1
        elif instruction == 'jmp':
            pointer += value
        elif instruction == 'nop':
            pointer += 1

        if pointer >= len(instructions):
            return accum, True


with open('input.txt') as instructions:
    instructions = instructions.readlines()

print(run(instructions, 0, 0, set())[0])

for index, instruction in enumerate(instructions):
    if instructions[index][:3] in ('jmp', 'nop'):
        old_instruction = instructions[index]
        change_instruction(index)
        accum, terminated = run(instructions, 0, 0, set())
        if terminated:
            print(accum)
            break
        else:
            instructions[index] = old_instruction

# 1200
# 1023
