class emulator():
    def __init__(self, code, target=None):
        if type(code) == str:
            self.code = [(op, int(val)) for op, val in map(str.split, code.splitlines())]
        else:
            raise(StopIteration)
        self.length = len(self.code)-1
        self.history = list()
        self.ptr = 0
        self.acc = 0
    def step(self):
        op, arg = self.code[self.ptr]
        self.history.append((len(self.history), self.ptr, self.acc, op, arg))
        if self.ptr in (h[1] for h in self.history[:-1]):
            # print("loop detected:", self.history[-2:])
            return(-1) # LOOP_DETECTED
        if self.ptr==self.length:
            # print("end of execution:", self.history[-1])
            return(1) # END_OF_EXECUTION
        if op == "nop":
            self.ptr += 1
        elif op == "acc":
            self.ptr += 1
            self.acc += arg
        elif op == "jmp":
            self.ptr += arg
        return(0) # RUNNING

code = open("input.txt").read()
emu = emulator(code)
while not emu.step():
    continue

print("part1:", emu.acc, emu.history[-1], '\n')

breakpoints = [h[1] for h in emu.history if h[3] in ["jmp", "nop"]][::-1]
for i, bp in enumerate(breakpoints):
    emu = emulator(code)
    op, arg = emu.code[bp]
    emu.code[bp] = ("jmp" if op=="nop" else "nop", arg)
    print(f"try#{i}: emu.code[{bp}] = {op,arg} --> {emu.code[bp]}")
    status = 0
    while not status:
        status = emu.step()
    if status == 1:
        print("part2:", emu.acc, emu.history[-1], '\n')
        break
