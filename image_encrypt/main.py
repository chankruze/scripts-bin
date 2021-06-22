import io
import struct
import time
from PIL import Image
from PIL import UnidentifiedImageError


def current_milli_time():
    return round(time.time() * 1000)


def read_image(path):
    with open(path, "rb") as image:
        f = image.read()
        return bytearray(f)


def sum_of_str_chars(string):
    return sum([ord(s) for s in string])


# version 1 (int -> int)
def enc_v1(val, key):
    # key = str, val = int
    if type(val) is int and type(key) is str:
        # calculate int value of key
        enc_key = sum_of_str_chars(key)
        xor_val = val ^ enc_key
        # TODO convert xor_val to char in v2
        return xor_val


# version 2 (int -> char)
def enc_v2(val, key):
    return


if __name__ == "__main__":
    image_file = "3.jpg"
    orig_bytes = read_image(f"jpgs/{image_file}")

    # encryption
    # the encryption key
    _KEY = input(f"Enter Key: ")
    # encrypted byte values
    enc_values = [enc_v1(b, _KEY) for b in orig_bytes]
    # list length of encrypted byte values
    len_enc_values = len(enc_values)
    # struct pack the encrypted values
    packed = struct.pack(f'{len_enc_values}i', *enc_values)
    # print(pack)
    # write to disk
    with open(f"{image_file}.dat", 'wb') as enc_file:
        enc_file.write(packed)

    #
    # decryption
    #

    # read encrypted file

    unpacked = ''
    with open(f"{image_file}.dat", 'rb') as data_file:
        unpacked = struct.unpack(f'{len_enc_values}i', data_file.read())

    list_unpack = [x for x in unpacked]

    # check
    print(len(enc_values), enc_values[:4])
    print(len(list_unpack), list_unpack[:4])

    # check
    # if len(enc_values) == len(list_pack) and len(enc_values) == sum(
    #         [1 for i, j in zip(enc_values, list_pack) if i == j]):
    #     print("The lists are identical")
    # else:
    #     print("The lists are not identical")

    # enc_bytes = b''.join([enc_v1(b, XOR_KEY) for b in orig_bytes])

    # print(orig_bytes)
    # print(enc_bytes)
    # print([enc_v1(x, 'test') for x in orig_bytes])

    # check encryption
    # try:
    #     enc_image = Image.open(io.BytesIO(enc_bytes))
    #     enc_image.show()
    # except UnidentifiedImageError:
    #     print('Encryption success!')

    # check decryption

    # orig_image = Image.open(io.BytesIO(original_bytes))
    # orig_image.show()

    # image.save("bytes.png")
