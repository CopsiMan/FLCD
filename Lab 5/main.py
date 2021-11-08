class Transition:
    def __init__(self, initial_state, trough, result):
        self.initial_state = initial_state
        self.trough = trough
        self.result = result

    def matches(self, initial, trough):
        return self.initial_state == initial and self.trough == trough

    def __str__(self):
        return "(" + self.initial_state + ", " + self.trough + ") -> " + self.result


class State:
    def __init__(self, name, initial):
        self.name = name
        self.initial = initial


def split_states(line):
    states = line.split()[2:]
    for i in range(len(states)):
        states[i] = states[i].strip("{},")
    # print(states)
    return states


class FA:
    def __init__(self):
        self.set_of_states = ""
        self.alphabet = ""
        self.transitions = ""
        self.final_states = []
        self.Transitions = []
        self.initial_state = ""

    def read_fa(self, file_name):
        lines = open(file_name, "r").read().split("\n")
        self.set_of_states = lines[1]
        self.alphabet = lines[2]
        self.initial_state = lines[3].split()[2]
        self.final_states = split_states(lines[4])
        self.transitions = lines[6:-1]
        for i in range(len(self.transitions)):
            self.transitions[i] = self.transitions[i].strip()
            transition = self.transitions[i].split()
            # print(transition)
            should_add = True
            state = transition[0][1:-1]
            result = transition[3]
            trough = transition[1][:-1]
            if self.set_of_states.find(state) == -1:
                raise RuntimeError("State " + str(state) + " is not in the set of states.")
            if self.set_of_states.find(result) == -1:
                raise RuntimeError("State " + str(result) + " is not in the set of states.")
            if self.alphabet.find(trough) == -1:
                raise RuntimeError("Symbol " + str(trough) + " is not in the alphabet.")
            for transition_duplicate in self.Transitions:
                if transition_duplicate.matches(state, trough):
                    should_add = False
            if should_add:
                self.Transitions.append(Transition(state, trough, result))

        # print(self.transitions)
        # print(self.alphabet)
        # print(self.set_of_states)
        # print(self.final_states)

    def verify_sequence(self, sequence):
        dfa = self.is_deterministic_finite_automaton()
        print("Is it a DFA ? - " + str(dfa))
        if dfa:
            return "Is it a valid sequence ? - " + str(self.verify(self.initial_state, sequence))

    def verify(self, first, sequence):
        if len(sequence) == 0:
            return first in self.final_states
        trough = sequence[0]
        for transition in self.Transitions:
            if transition.matches(first, trough):
                return self.verify(transition.result, sequence[1:])
        return False

    def is_deterministic_finite_automaton(self):
        transitions_dictionary = dict()
        for transition in self.Transitions:
            key = (transition.initial_state, transition.trough)
            if key in transitions_dictionary.keys():
                return False
            transitions_dictionary[key] = transition.result
        return True


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
            for transition in fa.Transitions:
                print(transition)
        if option == "4":
            print(fa.final_states)
        if option == "5":
            sequence = input("Sequence > ")
            print(fa.verify_sequence(sequence))


main()

# (S1, 0) -> S1
