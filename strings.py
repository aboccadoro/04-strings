import argparse


def print_strings(file_obj, encoding, min_len):
    if encoding == 's':
        while True:
            string = ""
            byte = file_obj.read(1).decode("UTF-8", errors="replace")
            if len(byte) == 0: break
            while ord(byte) > 31 and ord(byte) < 127:
                string += byte
                byte = file_obj.read(1).decode("UTF-8", errors="replace")
                if len(byte) == 0: break
            if len(string) >= min_len: print(string)
    elif encoding == 'b':
        while True:
            string = ""
            byte = file_obj.read(2).decode("UTF-16BE", errors="replace")
            if len(byte) == 0: break
            while ord(byte) > 31 and ord(byte) < 127:
                string += byte
                byte = file_obj.read(2).decode("UTF-16BE", errors="replace")
                if len(byte) == 0: break
            if len(string) >= min_len: print(string)
    elif encoding == 'l':
        while True:
            string = ""
            byte = file_obj.read(2).decode("UTF-16LE", errors="replace")
            if len(byte) == 0: break
            while ord(byte) > 31 and ord(byte) < 127:
                string += byte
                byte = file_obj.read(2).decode("UTF-16LE", errors="replace")
                if len(byte) == 0: break
            if len(string) >= min_len: print(string)
            


def main():
    parser = argparse.ArgumentParser(description='Print the printable strings from a file.')
    parser.add_argument('filename')
    parser.add_argument('-n', metavar='min-len', type=int, default=4,
                        help='Print sequences of characters that are at least min-len characters long')
    parser.add_argument('-e', metavar='encoding', choices=('s', 'l', 'b'), default='s',
                        help='Select the character encoding of the strings that are to be found. ' +
                             'Possible values for encoding are: s = UTF-8, b = big-endian UTF-16, ' +
                             'l = little endian UTF-16.')
    args = parser.parse_args()

    with open(args.filename, 'rb') as f:
        print_strings(f, args.e, args.n)

if __name__ == '__main__':
    main()