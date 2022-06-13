from pathlib import Path


def path_exists(path: str):
    return Path(path).exists()


def is_file(path: str):
    return Path(path).is_file()


def is_folder(path: str):
    return Path(path).is_dir()


def get_content_folder(path: str):
    return Path(path).glob('**')