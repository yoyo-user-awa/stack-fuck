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
# 4b 69 6d 69 e8 84 91 | e6 8a bd | e6 8b 9b e7 ac 91
code_ = '''
push, 4b
flow, buf, 1
put
push, 69
flow, buf, 1
put
push, 6d
flow, buf, 1
put
push, 69
flow, buf, 1
put
push, 91
push, 84
push, e8
flow, buf, 3
put
push, bd
push, 8a
push, e6
flow, buf, 3
put
push, 9b
push, 8b
push, e6
flow, buf, 3
put
push, 91
push, ac
push, e7
flow, buf, 3
put
'''
interpreter = Interpreter()
interpreter.interpret(code_)