from pathlib import Path


class SimpleDB:
    def __init__(self, dir_path: Path):
        self.file = dir_path / "data.txt"
        self.file.touch(exist_ok=True)

    def add(self, line: str):
        with self.file.open("a", encoding="utf-8") as f:
            f.write(line + "\n")

    def get_all(self):
        return self.file.read_text(encoding="utf-8").splitlines()

    def clear(self):
        self.file.write_text("", encoding="utf-8")



