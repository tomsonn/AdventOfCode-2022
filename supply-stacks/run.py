import re
import copy

from utils.util import read_file_data


def parse_instructions(instruction_list: list) -> list:
    pattern = r'move (\d*) from (\d*) to (\d*)'
    return [re.findall(pattern, i)[0] for i in instruction_list]


def assemble_boxes(boxes: list, boxes_count: int) -> list:
    boxes_assembled = [[] for _ in range(boxes_count)]
    for row in boxes[::-1]:
        for i in range(boxes_count):
            item = row[i * 4 + 1]
            if item.isalpha():
                boxes_assembled[i].append(item)

    return boxes_assembled


def reorder_boxes(boxes: list, instructions: list, reverse: bool = True) -> str:
    for instruction in instructions:
        box_from = int(instruction[1]) - 1
        box_to = int(instruction[2]) - 1
        boxes_no = int(instruction[0])

        # 1) get boxes to move
        if reverse:
            boxes_to_move = boxes[box_from][-boxes_no:][::-1]
        else:
            boxes_to_move = boxes[box_from][-boxes_no:]

        # 2) append chosen boxes to destination box
        for b in boxes_to_move:
            boxes[box_to].append(b)

        # 3) remove boxes which were moved
        boxes[box_from] = boxes[box_from][:-boxes_no]

    return ''.join([box[-1] for box in boxes])


def main() -> None:
    content = [l.strip() for l in read_file_data()]
    instructions_raw = [i for i in content if 'move' in i]
    boxes = [c for c in content if '[' in c]
    container_count = int(
        [
            c
            for c in content
            if c not in instructions_raw and c not in boxes and c
        ][0].split('   ')[-1]
    )

    instructions = parse_instructions(instructions_raw)

    boxes_assembled = assemble_boxes(boxes, container_count)

    boxes_copy_pt1 = copy.deepcopy(boxes_assembled)
    final_items_pt1 = reorder_boxes(boxes_copy_pt1, instructions)

    boxes_copy_pt2 = copy.deepcopy(boxes_assembled)
    final_items_pt2 = reorder_boxes(boxes_copy_pt2, instructions, reverse=False)

    print(f'Creates on top of each stack in part1: {final_items_pt1}')
    print(f'Creates on top of each stack in part1: {final_items_pt2}')


if __name__ == '__main__':
    main()
