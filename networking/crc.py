import pandas as pd
import math


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def eval_divisor(raw: str):
    if 'x' in raw and '^' in raw:
        divisor = ""
        split_places = raw.split('+')
        coefficients = [place.strip().split('^')[-1] for place in split_places]
        max_coefficient = max(int(x) for x in filter(lambda x: x != 'x', coefficients))
        binary = [str(x) for x in range(max_coefficient, -1, -1)][:-2] + ['x', '1']

        for digit in binary:
            if digit in coefficients:
                divisor += '1'
            else:
                divisor += '0'

        return divisor

    return raw


def calc_crc(data, poly):
    dword = int(data, 2)
    divisor = eval_divisor(poly)
    len_divisor = len(divisor)

    # append 0s to dividend
    dividend = dword << (len_divisor - 1)

    # shift specifies the no. of least significant
    # bits not being XORed
    shift = math.ceil(math.log(dividend + 1, 2)) - len_divisor

    # ceil(log(dividend + 1 , 2)) is the no. of binary
    # digits in dividend
    divisor = int(divisor, 2)

    while dividend >= divisor or shift >= 0:
        # bitwise XOR the MSBs of dividend with generator
        # replace the operated MSBs from the dividend with
        # remainder generated
        rem = (dividend >> shift) ^ divisor
        dividend = (dividend & ((1 << shift) - 1)) | (rem << shift)

        # change shift variable
        shift = math.ceil(math.log(dividend + 1, 2)) - len_divisor

    # finally, AND the initial dividend with the remainder (=dividend)
    t_data = dword << (len_divisor - 1) | dividend
    return f"{bin(t_data).lstrip('-0b')}"


def calc_lrc(data) -> bin:
    data_bytes = [[int(n) for n in list(num)] for num in data.split()]
    df = pd.DataFrame(data_bytes, dtype="int64")
    lrc = "".join(['0' if num % 2 == 0 else '1' for num in list(df.sum())])
    return f"{colored(255, 255, 0, lrc)} {''.join(list(reversed(data)))}"


if __name__ == "__main__":
    lrc_msg = "11100111 11011101 00111001 10101001"
    crc_msg = "11001001"
    crc_divisor = "x^3+1"
    transmitted_data_lrc = calc_lrc(lrc_msg)
    transmitted_data_crc = calc_crc(crc_msg, crc_divisor)
    print(f"Transmitted data (LRC) = {transmitted_data_lrc}")
    print(f"Transmitted data (CRC) = {transmitted_data_crc}")
