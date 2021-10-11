from HashTable import HashTable


def main():
    symbol_table = HashTable()
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


main()
