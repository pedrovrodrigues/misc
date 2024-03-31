
if __name__ == "__main__":
    dictionary = {}
    learning = True
    while True:
        try:
            line = input()
            if len(line) == 0:
                learning = False
            elif learning:
                english, dialect = line.split(" ")[:2]
                dictionary[dialect] = english
            else:
                print(dictionary.get(line, "eh"))
        except EOFError:
            break
    