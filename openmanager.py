from typing import Any

def _open(path:str, mode:str, text: str = "") -> (Any | None):
    try:
        with open(path, mode) as f:
            if "r" in mode:
                return f.read()
            else:
                f.write(text)
                return None
    except FileNotFoundError:
        with open(path, "w") as f:
            f.write(text)
            return None