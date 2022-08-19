
class Account:
    # TODO-0: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO-1: добавьте проверку паспорта и телефона(в конструкторе) на соответствие заданным форматам
    #  В случае несоответствия выбрасываем исключение ValueError("Неверный формат телефона/паспорта")
    #  Проверка информации на корректность - валидация
    #  Готовые валидаторы можете взять в директории helpers

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance

        try:
            self.check_passport()
        except ValueError:
            print(f'Некорректный формат паспорта, {name}')

        try:
            self.check_phone()
        except ValueError:
            print(f'Некорректный формат телефона, {name}')


    def check_passport(self):
        import re

        pattern = r"\d{4} \d{6}"

        if not re.match(pattern, self.passport):
            raise ValueError("Неверный формат телефона/паспорта")

    def check_phone(self):
        import re

        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

        if not re.match(pattern, self.phone_number):
            raise ValueError("Неверный формат телефона/паспорта")

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    # TODO: совместно с преподавателем реализуйте getter для просмотра баланса
    #  Можете попробовать самостоятельно: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/
    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount:
            raise ValueError("У Вас не достаточно средств...")

        self.__balance -= amount

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """

        self.withdraw(amount)

        target_account.deposit(amount)

account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)  # аккаунт с корректными данными
account2 = Account("Алексей", "+7-901-744-22-99", "323 456124", 200)  # номер паспорта задан не верно
account3 = Account("Петр", "+7-904-745-47", "3232 456124", 200)  # номер телефона задан не верно
