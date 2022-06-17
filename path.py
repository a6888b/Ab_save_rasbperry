from pathlib import Path


def path_exists(path: str):
    return Path(path).exists()


def get_name(file: str | Path):
    return Path(file).name


def is_file(path: str | Path):
    return Path(path).is_file()


def is_folder(path: str | Path):
    return Path(path).is_dir()


def get_content_folder(path: str):
    return Path(path).iterdir()


def get_content(file: str):
    return Path(file).read_text()
