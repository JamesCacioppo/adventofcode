def main():
    print("Hello from advent2025!")
from pathlib import Path

from advent2025.day1 import solve


def main() -> None:
    input_path = Path(__file__).parent / "inputs" / "day1_input.txt"
    part1, part2 = solve(input_path)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
