class Account:
    def __init__(self, balance):
        self.balance = balance

    def transfer_to(self, target, amount):
        if self.balance < amount:
            raise ValueError("예금 부족")
        self.balance -= amount
        target.balance += amount

# 간단한 계좌 이체 함수를 pytest와 함께 AAA 패턴으로 작성해본다

