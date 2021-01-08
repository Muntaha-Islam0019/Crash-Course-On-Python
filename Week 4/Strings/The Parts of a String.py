def first_and_last(message):
    return (message[0] is message[-1]) if len(message) > 0 else True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))