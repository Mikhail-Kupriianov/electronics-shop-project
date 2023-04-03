import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "В файле csv повреждены данные"


class Item:
    """
    Класс для представления товара в магазине.
    """
    OPERATION_DIR = os.path.abspath(os.path.dirname(__file__))
    csv_file_name = 'items.csv'

    pay_rate = 1.0
    all = []

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @property
    def name(self):
        """ Возвращает имя товара"""
        return self.__name

    @name.setter
    def name(self, name):
        """Устанавливает новое имя товара"""
        self.__name = name if len(name) < 11 else print('Exception: Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """ Класс-метод, инициализирующий экземпляры класса `Item` данными из файла src/items.csv"""
        csv_file = os.path.join(cls.OPERATION_DIR, cls.csv_file_name)
        cls.all.clear()
        try:
            with open(csv_file, encoding='windows-1251') as csvfile:
                load_data = csv.DictReader(csvfile)
                for line in load_data:
                    if len(line) != 3 or None in line.values():
                        raise InstantiateCSVError
        except InstantiateCSVError:
            print(f'InstantiateCSVError: Файл {cls.csv_file_name} поврежден')
        except FileNotFoundError:
            print(f'FileNotFoundError: Отсутствует файл {cls.csv_file_name}')

        else:
            with open(csv_file, encoding='windows-1251') as csvfile:
                load_data = csv.DictReader(csvfile)
                for line in load_data:
                    cls(line["name"], line["price"], line["quantity"])

    @staticmethod
    def string_to_number(dig_str: str) -> int:
        return int(float(dig_str))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
