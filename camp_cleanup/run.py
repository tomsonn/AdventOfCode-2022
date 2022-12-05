from utils.util import read_file_data


def main():
    content = [l.strip() for l in read_file_data()]

    overlap_full_count = 0
    overlap_semi_count = 0
    for l in content:
        elf_one, elf_two = l.split(',')
        boundary_left_one, boundary_right_one = map(int, elf_one.split('-'))
        boundary_left_two, boundary_right_two = map(int, elf_two.split('-'))
        if (boundary_left_one >= boundary_left_two and \
            boundary_right_one <= boundary_right_two) or \
           (boundary_left_two >= boundary_left_one and \
            boundary_right_two <= boundary_right_one):
            overlap_full_count += 1

        if boundary_left_two <= boundary_left_one <= boundary_right_two or \
           boundary_left_two <= boundary_right_one <= boundary_right_two or \
           boundary_left_one <= boundary_left_two <= boundary_right_one or \
           boundary_left_one <= boundary_right_two <= boundary_right_one:
            overlap_semi_count += 1

    print(f'Full overlap count: {overlap_full_count}')
    print(f'Semi overlap count: {overlap_semi_count}')


if __name__ == '__main__':
    main()
