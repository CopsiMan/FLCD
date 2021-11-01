class Transition:
    def __init__(self, initial_state, trough, result):
        self.initial_state = initial_state
        self.trough = trough
        self.result = result

    def matches(self, initial, trough):
        return self.initial_state == initial and self.trough == trough


class State:
    def __init__(self, name, initial):
        self.name = name
        self.initial = initial


class FA:
    def __init__(self):
        self.set_of_states = ""
        self.alphabet = ""
        self.transitions = ""
        self.final_states = ""
        self.Transitions = []
        self.initial_state = ""

    def read_fa(self, file_name):
        lines = open(file_name, "r").read().split("\n")
        self.set_of_states = lines[1]
        self.alphabet = lines[2]
        self.initial_state = lines[3].split()[2]
        self.final_states = lines[4]
        self.transitions = lines[6:-1]
        for i in range(len(self.transitions)):
            self.transitions[i] = self.transitions[i].strip()
            transition = self.transitions[i].split()
            print(transition)
            self.Transitions.append(Transition(transition[0][1:-1], transition[1][:-1], transition[3]))

        # print(self.transitions)
        # print(self.alphabet)
        # print(self.set_of_states)
        # print(self.final_states)

    def verify_sequence(self, sequence):
        return self.verify(self.initial_state, sequence)

    def verify(self, first, sequence):
        if len(sequence) == 0:
            return True
        trough = sequence[0]
        for transition in self.Transitions:
            if transition.matches(first, trough):
                return self.verify(transition.result, sequence[1:])
        return False


def print_menu():
    print()
    print("0. Exit: ")
    print("1. Set of states: ")
    print("2. Alphabet: ")
    print("3. All transitions: ")
    print("4. Set of final states: ")
    print("5. Verify sequence: ")


def main():
    fa = FA()
    fa.read_fa("FA.in")
    # fa.verify_sequence("101")
    while True:
        print_menu()
        option = input("Option > ")
        if option == "0":
            break
        if option == "1":
            print(fa.set_of_states)
        if option == "2":
            print(fa.alphabet)
        if option == "3":
            # print(fa.transitions)
            for transition in fa.transitions:
                print(transition)
        if option == "4":
            print(fa.final_states)
        if option == "5":
            sequence = input("Sequence > ")
            print(fa.verify_sequence(sequence))


main()
