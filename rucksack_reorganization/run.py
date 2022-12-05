import string

from utils.util import read_file_data


def main():
    content = [l.strip() for l in read_file_data()]

    alphabet = string.ascii_letters
    points = 0
    for items in content:
        items_count = int(len(items) / 2)
        compartment_one = items[:items_count]
        compartment_two = items[items_count:]

        common_item = list(set(compartment_one).intersection(compartment_two))
        points += alphabet.index(common_item[0]) + 1

    print(f'Sum of items: {points}')

    points_part_two = 0
    for i in range(len(content) // 3):
        compartment_one = content[i*3]
        compartment_two = content[i*3+1]
        compartment_three = content[i*3+2]

        common_item = [
            i
            for i in compartment_one
            for j in compartment_two
            for k in compartment_three
            if i == j == k
        ]
        points_part_two += alphabet.index(common_item[0]) + 1

    print(f'Sum of items part two: {points_part_two}')


if __name__ == '__main__':
    main()
