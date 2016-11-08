def safe_input():
    n = input("Please enter a command '\n'"
              "> ")
    if n == "^C":
        raise KeyboardInterrupt("None")
    elif n == "^D":
        raise EOFError("None")

safe_input()






