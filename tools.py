def parse(path):
    res = []
    f = open(path, "r")
    f.readline()
    for line in f:
        res.append(line[:-1].split(" ")[2:])
    f.close()
    return res

path = "data/a_example.txt"
print(parse(path))
