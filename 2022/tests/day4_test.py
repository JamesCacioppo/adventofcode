from advent2022.day4 import puz4

def test_elf_pair_class(day_four_file):
    elf_pairs = list()

    for line in day_four_file:
        elf_pairs.append(puz4.ElfPair(line))

    assert elf_pairs[0].elf_pair_assigned_sections == ["2-4", "6-8"]
    assert elf_pairs[1].elf_pair_assigned_sections == ["2-3", "4-5"]
    assert elf_pairs[2].elf_pair_assigned_sections == ["5-7", "7-9"]
    assert elf_pairs[3].elf_pair_assigned_sections == ["2-8", "3-7"]
    assert elf_pairs[4].elf_pair_assigned_sections == ["6-6", "4-6"]
    assert elf_pairs[5].elf_pair_assigned_sections == ["2-6", "4-8"]

    assert elf_pairs[0].elf_a_assigned_sections == [2, 3, 4]
    assert elf_pairs[0].elf_b_assigned_sections == [6, 7, 8]