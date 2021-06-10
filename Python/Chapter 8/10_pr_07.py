def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Harry is a good      "
n = remove_and_strip(this, "Harry")
print(n)
# print(this)
# print(this.strip())
