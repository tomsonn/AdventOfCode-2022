#!/usr/bin/env python3

from utils.util import read_file_data


def split_calories(calories_list: list) -> list:
    chunk = []
    for calorie in calories_list:
        if calorie == '':
            yield chunk
            chunk = []
        else:
            chunk.append(int(calorie))

    yield chunk


def main() -> None:
    content = [value.strip() for value in read_file_data()]
    calories_split = split_calories(content)
    calories_sum_by_elf = [sum(chunk) for chunk in calories_split]

    # Day 1 #
    calorie_max = max(calories_sum_by_elf)
    print(f'Max calories count: {calorie_max}')

    # Day 2 #
    top_three_calories_sum = sum(sorted(calories_sum_by_elf)[-3:])
    print(f'Sum of top three calories holders: {top_three_calories_sum}')


if __name__ == '__main__':
    main()
