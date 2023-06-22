import os

# @return tuple(directory path, file name.extension)
def split_abspath(file_path):
    if file_path is not None and file_path != '':
        return os.path.split(os.path.abspath(file_path))
    else:
        return ('','')

## Gets file name from path. Normalize path.
def basename_abspath(file_path):
    return os.path.basename(os.path.abspath(file_path))
