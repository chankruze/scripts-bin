import os


# list all files
def list_files(folder):
    return os.listdir(str(folder))


# list all files matching the extension
def list_files_with_ext(folder, ext):
    _files = list()

    for _f in os.listdir(str(folder)):
        _file_name, _file_ext = os.path.splitext(_f)
        if _file_ext == str(ext):
            _files.append(_f)

    return _files
