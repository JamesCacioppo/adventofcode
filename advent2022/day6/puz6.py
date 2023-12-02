import sys

def open_file(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
    return(line)

def find_marker(line, length, num_of_distinct):
    for i in range(length):
        sus = line[i:i+num_of_distinct]
        print(f"sus is {sus}")
        duplicates = 0
        print(f"init duplicates at {duplicates}")
        for j in sus:
            print(f"looking for {j} in {sus}")
            count = sus.count(j)
            print(f"count is {count}")
            if count > 1:
                duplicates += 1
            print(f"duplicates is now {duplicates}")
        if duplicates == 0:
            return(i + num_of_distinct)

print(f"Opening file {sys.argv[1]}")
line = open_file(sys.argv[1])
length = len(line)

print(f"The SoP marker is after character {find_marker(line, length, 4)}")
print(f"The SoM marker is after character {find_marker(line, length, 14)}")