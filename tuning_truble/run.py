from utils.util import read_file_data


def get_starting_index(buffer: str, indentation: int) -> int:
    for i in range(len(buffer) - indentation):
        substring = buffer[i:i+indentation]
        if len(substring) == len(set(substring)):
            return i + indentation

    return -1


def main():
    buffer = [l.strip() for l in read_file_data()][0]
    starting_packet_index = get_starting_index(buffer, 4)
    starting_message_index = get_starting_index(buffer, 14)
    if starting_packet_index == -1:
        sys.exit("Couldn't find starting packet index in provided buffer.")

    if starting_packet_index == -1:
        sys.exit("Couldn't find starting message index  in provided buffer.")

    print(f'Start of packet marker is detected at index {starting_packet_index}.')
    print(f'Start of message marker is detected at index {starting_message_index}.')


if __name__ == '__main__':
    main()
