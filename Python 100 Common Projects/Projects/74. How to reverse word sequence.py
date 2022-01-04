def string_rev(str):
    str = str.split()
    str.reverse()
    return ' '.join(str)

print(string_rev(input("Insert some strings: ")))