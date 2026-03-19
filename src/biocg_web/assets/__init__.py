from pathlib import Path


def get_path(name: str) -> Path:
    return (Path(__file__) / ".." / name).resolve()


def get_content(name: str) -> str:
    with open(get_path(name), "r") as fp:
        content = fp.read()
    return content
