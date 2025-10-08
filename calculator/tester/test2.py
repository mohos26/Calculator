import sys
sys.path.append("..")
from parsing import parsing


with open("test.txt") as file:
    i = 1
    while True:
        line = file.readline().strip()
        if '=' in line:
            line = line[:line.index('=')]
        line_without_space = line.replace(" ", "").replace("**", "^")
        output = " ".join(parsing(line_without_space)).replace("^", "**")
        if output != line:
            print("*"*25)
            print("line count:", i)
            print("your:", output)
            print("correct:", line)
        if not line:
            break
        i += 1
