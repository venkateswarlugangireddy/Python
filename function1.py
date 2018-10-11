def string_length(word):
    if type(word) is str:
        return len(word)
    elif type(word) is int:
        print("this is number")
    else:
        print("this is float length function")


print(string_length(34.9))