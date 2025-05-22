from dataclasses import dataclass, field
from dataclasses import asdict

@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    def to_dict(self):
        return asdict(self)
