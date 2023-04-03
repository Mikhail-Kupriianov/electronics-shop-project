from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.csv_file_name = 'items_b.csv'
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.csv_file_name = 'items_bad.csv'
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
