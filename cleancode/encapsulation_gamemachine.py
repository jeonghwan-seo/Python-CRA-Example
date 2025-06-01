class GameMachine:
    def __init__(self):
        self._coin = 0

    def input_coin(self, count):
        if count > 5:
            raise ValueError("최대 5개까지만 가능합니다")
        if self._coin + count > 10:
            raise ValueError("총 코인은 10개를 초과할 수 없습니다")

        self._coin += count

    def show_coin(self):
        print(f"현재 coin은 {self._coin}개 있습니다")

    def play(self):
        if self._coin <= 0:
            raise ValueError("코인이 부족합니다")

        self._coin -= 1

        print("게임 시작!")

