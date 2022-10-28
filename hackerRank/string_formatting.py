
def print_formatted(number):

    for x in range(1,number+1):
        spacing = number.bit_length()

        dec = str(x).rjust(spacing)
        octs = str(oct(x)[2:]).rjust(spacing)
        hexa = str(hex(x)[2:]).rjust(spacing).upper()
        binary = str(bin(x)[2:].rjust(spacing))

        print(f'{dec} {octs} {hexa} {binary}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)