class Automaton(object):

    def __init__(self):
        self.states = []
        self.state = 1

    def read_commands(self, commands):
        self.state == 1
        for ch in commands:
            if self.state == 1:
                if ch == '1':
                    self.state = 2
            elif self.state == 2:
                if ch == '0':
                    self.state = 3
            elif self.state == 3:
                if (ch == '0') or (ch == '1'):
                    self.state = 2
        return True if self.state == 2 else False

my_automaton = Automaton()

print(my_automaton.read_commands(["1"]))
print(my_automaton.read_commands(["1", "0", "0", "1"]))