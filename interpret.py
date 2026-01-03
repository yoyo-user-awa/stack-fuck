from lib import stack
from re import split as rsplit


class Interpreter:
    def __init__(self):
        self.buffer = bytearray()
        self.stack = stack.StackList(12)

    def interpret(self, code):
        lines = code.strip().splitlines()
        pos = 0
        while pos < len(lines):
            line = lines[pos]
            parts = rsplit(r',\s?', line)
            match parts:
                case ['push',value]:
                    self.stack.push(int(value,16))
                case ['throw']:
                    self.stack.pop()
                case ['flow',targ,count]:
                    if targ == 'buf':
                        bytearr = bytearray()
                        for _ in range(int(count,16)):
                            bytearr.append(self.stack.pop())
                        self.__flow('buf',bytearr)
                case ['put']:
                    print(self.buffer.decode('utf-8',errors='replace')[0],end='')
                case ['clear']:
                    self.buffer.clear()

            pos += 1

    def __flow(self, targ, value):
        if targ == 'buf':
            self.buffer = value