from dataclasses import dataclass, field
from dataclasses import asdict


@dataclass
class Card:
    """
    할일을 관리해주는 application 에서 사용되는 기본 데이터 구조입니다. 

    Attributes:
        summary (str): 작업에 대한 간단한 설명입니다.
        owner (str): 이 작업 카드를 담당하는 사람의 이름입니다.
        state (str): 카드의 현재 상태입니다. 일반적인 값은 다음과 같습니다:
            - "todo": 아직 시작되지 않은 상태
            - "in prog": 진행 중
            - "done": 완료됨 
        id (int): 카드의 고유 식별자입니다. 객체의 동등성 비교에 이용해서는 안됩니다.
    """
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    def to_dict(self):
        return asdict(self)
