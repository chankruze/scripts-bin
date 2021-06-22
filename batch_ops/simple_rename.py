import os


def rename(src, new_file_name):
    if os.path.exists(src):
        separator = ""
        # sys.platform.startswith("win")
        if os.name == "nt":
            separator = "\\"
        # sys.platform == "linux"
        elif os.name == "posix":
            separator = "/"

        # file dir
        src_file_dir = f"{separator}".join(os.path.realpath(src).split(separator)[:-1])
        # file name
        src_file_name = os.path.realpath(src).split(separator)[-1]

        os.rename(f"{src_file_dir}{separator}{src_file_name}", f"{src_file_dir}{separator}{new_file_name}")
        print("done!")


if __name__ == "__main__":
    rename(str(input(f"File name(path): ")), str(input(f"New name: ")))
