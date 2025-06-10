my_file = "../test_data/sample.txt"

print("Line\tChars\tUppercase\t% Upper")

with open(my_file, 'r') as f:
    for i, line in enumerate(f, start=1):
        stripped_line = line.strip()
        total = len(stripped_line)
        upper = sum(1 for c in stripped_line if c.isupper())
        p = (upper / total * 100) if total != 0 else 0
        print(f"{i}\t{total}\t{upper}\t{round(p, 2)}%")

