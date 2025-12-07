from __future__ import annotations


def read_file(filename) -> list[str]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines


def is_rotation_zero(s: str, starting_position: int) -> bool:
    direction = s[0]
    steps = int(s[1:])
    if direction == "R":
        final_position = (starting_position + steps) % 100
    elif direction == "L":
        intermediate_position = starting_position - steps
        if intermediate_position < 0:
            final_position = 100 + intermediate_position
        else:
            final_position = intermediate_position
    else:
        raise ValueError(f"Unknown direction: {direction}")

    if final_position == 0:
        return True
    else:
        return False

    
def part1(data: list[str]) -> int:
    """part1: Determine number of times a rotation ends on 0."""
    zero_count = 0

    for line in data:
        if line.strip() == "":
            continue
        num = int(line)
        if num == 0:
            zero_count += 1
    return zero_count


def part2(data: list[str]) -> int:
    """Example part2: count of integers in the input."""
    nums = [int(line) for line in data.splitlines() if line.strip()]
    return len(nums)


if __name__ == "__main__":
    import sys

    data = read_file(sys.argv[1])

    result1 = part1(data)
    print(f"part1: {result1}")

    result2 = part2("\n".join(data))
    print(f"part2: {result2}")