# detects floating bytes

with open("week2.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)