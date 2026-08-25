# Задача: BankAccount с property
# Сделай в классе BankAccount property balance, сеттер которого
# НЕ тихо исправляет отрицательное значение, а кидает ValueError.
#
# Чем это отличается от подхода с max(0, value)?


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        # TODO: верни self._balance
        pass

    @balance.setter
    def balance(self, value):
        # TODO: если value < 0 - подними ValueError, иначе сохрани
        pass


acc = BankAccount(100)
acc.balance = 50
print(acc.balance)  # 50

try:
    acc.balance = -10
except ValueError as e:
    print("Поймали:", e)
