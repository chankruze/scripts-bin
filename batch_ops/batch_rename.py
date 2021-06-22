import math
import os


# list all files
def list_files(_folder):
    return os.listdir(str(_folder))


# list all files matching the extension
def list_files_with_ext(_folder, _ext):
    _files = list()

    for _f in os.listdir(str(_folder)):
        _file_name, _file_ext = os.path.splitext(_f)
        if _file_ext == str(_ext):
            _files.append(_f)

    return _files


# rename all files following given pattern
def rename_all(_files, os_path_separator, **kwargs):
    start_index = kwargs.get('start_index', 1)
    step = kwargs.get('step', 1)
    delimiter = kwargs.get('delimiter', '_')
    padding = 1 + math.ceil(math.log10(len(_files)))

    for _index, _file in enumerate(_files):
        if os.path.exists(_file):
            # file dir
            src_file_dir = f"{os_path_separator}".join(_file.split(os_path_separator)[:-1])
            # file name
            src_file_name = _file.split(os_path_separator)[-1]
            # new file name
            _new_file_name = f"{str(start_index + (_index * step)).zfill(padding)}{delimiter}{src_file_name}"
            # rename
            os.rename(f"{src_file_dir}{os_path_separator}{src_file_name}", f"{src_file_dir}{os_path_separator}{_new_file_name}")
            # log
            print(f"✔ {src_file_name} -> {_new_file_name}")


def revert_rename_all(_files, os_path_separator, **kwargs):
    padding = 1 + math.ceil(math.log10(len(_files)))

    for _index, _file in enumerate(_files):
        if os.path.exists(_file):
            # file dir
            src_file_dir = f"{os_path_separator}".join(_file.split(os_path_separator)[:-1])
            # file name
            src_file_name = _file.split(os_path_separator)[-1]
            # new file name
            _orig_file_name = src_file_name[padding + 1:]
            # rename
            os.rename(f"{src_file_dir}{os_path_separator}{src_file_name}",
                      f"{src_file_dir}{os_path_separator}{_orig_file_name}")
            # log
            print(f"✔ {src_file_name} -> {_orig_file_name}")


if __name__ == "__main__":
    # separator
    separator = ""

    if os.name == "nt":
        separator = "\\"
    elif os.name == "posix":
        separator = "/"

    # directory
    folder = input(f"Directory: ")
    # extension
    ext = input(f"Extension: ")
    # file name contains string
    # sub_str = ""

    # list all files matching sub_str
    # files = list_files_with_sub_str(folder, sub_str)

    while True:
        # list all files matching ext
        files = list_files_with_ext(folder, ext)

        choice = input("Operation [0 = rename | 1 = revert]: ")

        if choice == '1':
            revert_rename_all([f"{os.path.realpath(folder)}{separator}{f}" for f in files], separator)
        elif choice == '0':
            rename_all([f"{os.path.realpath(folder)}{separator}{f}" for f in files], separator, start_index=1, step=1)
        else:
            exit(0)
