from lexer import tokenize

while True:
    try:
        source = input("    > ")
        if (source == "" or source == "exit"):
            break

        tokens = tokenize(source)
        for t in tokens:
            print(t)

    except Exception as e:
        print("Error:", e)