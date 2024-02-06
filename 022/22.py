names = ""


def sum_str(s):
    return sum([ord(char) - 64 for char in s])


with open("0022_names.txt") as names_files:
    names = names_files.read().replace('"', '').split(",")

names.sort()
inames = enumerate(names, 1)
numeric_names = [i * sum_str(name) for i, name in inames]
print(sum(numeric_names))
