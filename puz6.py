def open_file(filename):
    with open(filename, 'r') as f:
        line = f.read().strip()
    return(line)

def find_marker(line, length):
    for i in range(length):
        sus = line[i:i+4]
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
            return(i + 4)

line = open_file("input6.txt")
length = len(line)

print(f"The marker is after character {find_marker(line, length)}")