import random


def read_image(path):
    with open(path, "rb") as image:
        f = image.read()
        return bytearray(f)


def sum_of_str_chars(string):
    return sum([ord(s) for s in string])


def mask(path, key):
    image = read_image(path)

    for i, values in enumerate(image):
        image[i] = values ^ key

    with open(path, 'wb') as enc_file:
        enc_file.write(image)

    print("Done!")


if __name__ == "__main__":
    image_path = input("Enter file path: ")
    # the encryption key
    _KEY = int(input(f"Enter Key: "))
    mask(image_path, _KEY)
