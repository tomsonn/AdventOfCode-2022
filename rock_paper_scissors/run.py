from utils.util import read_file_data


OPPONENT = 'ABC'
ME = 'XYZ'


def get_points_from_match_pt1(match: tuple) -> int:
    opponent_index = OPPONENT.index(match[0])
    mine_index = ME.index(match[1])
    if ME[opponent_index - 1] == match[1]:
        # Lost
        return 0 + mine_index + 1
    elif ME[opponent_index] == match[1]:
        # Tie
        return 3 + mine_index + 1
    else:
        # Won
        return 6 + mine_index + 1


def get_points_from_match_pt2(match: tuple) -> int:
    opponent_index = OPPONENT.index(match[0])
    mine_index = ME.index(match[1])
    base_score = mine_index * 3

    # desired_index can be in range <-2; 0>
    if mine_index == 0:
        desired_index = opponent_index - 1
    elif mine_index == 2:
        desired_index = opponent_index - 2
    else:
        desired_index = opponent_index

    # positive_index is in range as we usually use it <0; 2>
    positive_index = ME.index(ME[desired_index])

    return base_score + positive_index + 1


def main() -> None:
    content = [tuple(pair.strip().split(' ')) for pair in read_file_data()]

    points_total_pt1 = sum([get_points_from_match_pt1(match) for match in content])
    print(f'Total points from all matches pt.1: {points_total_pt1}')

    points_total_pt2 = sum([get_points_from_match_pt2(match) for match in content])
    print(f'Total points from all matches pt.2: {points_total_pt2}')


if __name__ == '__main__':
    main()
