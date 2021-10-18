from HashTable import HashTable
from Scanner import Scanner


def symbol_table_test(symbol_table):

    print(symbol_table.add(1))
    print(symbol_table.add(2))
    print(symbol_table.add(3))
    print(symbol_table.add(4))
    print(symbol_table.add(2))
    print(symbol_table.add(3))
    print(symbol_table.add("hello"))
    print(symbol_table.add("hello1"))
    print(symbol_table.add("hello2"))
    print(symbol_table.add("hello3"))

    print(symbol_table)


def main():
    scanner = Scanner()
    scanner.scan("p1.txt")
    scanner.initialize_symbol_table()
    scanner.write_symbol_table()
    symbol_table = HashTable()
    # symbol_table_test(symbol_table)


main()
