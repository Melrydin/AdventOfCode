"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range,

and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate,

another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations.

A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead,
almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

Your puzzle answer was 16076.

--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

Your puzzle answer was 2797.
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return ["123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
                "NOT x -> h",
                "NOT y -> i"]
    else:
        return inputDocument("2015/07/input.txt")

def formatDocument(document: list[str]) -> list[str]:
    instructions = []
    for line in document:
        line = line.split(" ")
        line.remove("->")
        instructions.append(line)
    return instructions


def filterVariables(document: list[list[str]]) -> dict[str]:
    variables = {}
    gaters = {"NOT", "AND", "OR", "LSHIFT", "RSHIFT"}

    for instruction in document:
        for token in instruction:
            if token.isalpha() and token not in gaters:
                variables[token] = -1
            elif token.isdecimal():
                variables[token] = int(token)

    return variables


def runInstructions(instructions: list[list[str]], variables: dict[str]) -> dict[str]:
    while 0 < len(instructions):
        for instraction in instructions:

            if len(instraction) == 2:   # Allocation: [src, dest]
                if instraction[0] in variables:
                    if variables[instraction[0]] != -1:
                        variables[instraction[1]] = int(variables[instraction[0]])
                        instructions.remove(instraction)
                        break
                else:
                    variables[instraction[1]] = int(variables[instraction[0]])
                    instructions.remove(instraction)

            elif len(instraction) == 3:     # NOT-Operation: [NOT, src, dest]
                if variables[instraction[1]] != -1:
                    variables[instraction[2]] = (~variables[instraction[1]]) & ((1 << 16) - 1)
                    instructions.remove(instraction)

            elif len(instraction) == 4:     # Two-argument operations: [src1, OP, src2, dest]
                if instraction[1] == "LSHIFT":
                    if variables[instraction[0]] != -1:
                        variables[instraction[3]] = int(variables[instraction[0]]) << int(instraction[2])
                        instructions.remove(instraction)
                elif instraction[1] == "RSHIFT":
                    if variables[instraction[0]]!= -1:
                        variables[instraction[3]] = int(variables[instraction[0]]) >> int(instraction[2])
                        instructions.remove(instraction)
                elif instraction[1] == "AND":
                    if variables[instraction[0]]!= -1 and variables[instraction[2]]!= -1:
                        variables[instraction[3]] = int(variables[instraction[0]]) & int(variables[instraction[2]])
                        instructions.remove(instraction)
                elif instraction[1] == "OR":
                    if variables[instraction[0]]!= -1 and variables[instraction[2]]!= -1:
                        variables[instraction[3]] = int(variables[instraction[0]]) | int(variables[instraction[2]])
                        instructions.remove(instraction)
    return variables




if __name__ == "__main__":
    document = testCase(1)
    instructions = formatDocument(document)
    variables = filterVariables(instructions)
    variables = runInstructions(instructions.copy(), variables)
    print(f"Part 1: {variables['a']}")
    saveA = variables['a']
    variables = filterVariables(instructions)
    variables['b'] = saveA
    instructions = [inst for inst in instructions if not (inst[0].isdecimal() and inst[1] == "b" and len(inst) == 2)]
    variables = runInstructions(instructions.copy(), variables)
    print(f"Part 2: {variables['a']}")
