from pathlib import Path
import csv


class DataCollection:
    def __init__(self):
        self.data = {}  # Инициализация пустого словаря для хранения данных

    def count_objects(self):
        folder_name = input("Enter folder name: ")  # Запрос имени директории
        folder = Path(folder_name)
        if folder.is_dir():
            folder_count = len([1 for file in folder.iterdir()])  # Подсчет количества объектов в директории

        print(f"In folder {folder_name} there are {folder_count} objects.")

    def write_to_csv(self):
        key_inp = input('Enter key: ')
        date_inp = input('Enter date: ')
        price_inp = input('Enter price: ')
        name_inp = input('Enter name: ')
        self.data[key_inp] = [date_inp, price_inp, name_inp]  # Добавление новой записи в словарь
        with open('data.csv', 'w') as f:
            for elem in self.data:
                f.write(elem + "," + self.data[elem][0] + "," + self.data[elem][1] + "," + self.data[elem][
                    2] + "\n")  # Запись данных в CSV-файл

    def read_from_csv(self):
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            for line in reader:
                self.data[line[0]] = line[1:]  # Чтение данных из CSV-файла и добавление их в словарь

    def sort_by_numeric_field(self):
        print("Sorting the dictionary by price:")
        for elem in sorted(self.data.items(), key=lambda para: int(para[1][1])):
            print(elem[0], *elem[1])  # Сортировка словаря по числовому полю и вывод отсортированных элементов
        print("")

    def sort_by_string_field(self):
        print("Sorting the dictionary by product name:")
        for elem in sorted(self.data.items(), key=lambda para: para[1][2]):
            print(elem[0], *elem[1])  # Сортировка словаря по строковому полю и вывод отсортированных элементов
        print("")

    def inference_by_criterion(self):
        print("Rows with product name 'pizza':")
        for elem in self.data:
            if self.data[elem][2] == 'pizza':
                print(elem, *self.data[elem])  # Вывод строк словаря, в которых наименование товара равно 'pizza'

    def add_newline_to_file(self):
        check = input('Add newline to file? Enter y/n: ')
        if check == 'y':
            self.write_to_csv()  # Запись новой строки в файл, если выбрано 'y'
            print("Data successfully saved!")
        else:
            print("Program stopped.")

    def __repr__(self):
        return repr(self.data)  # Представление объекта в виде строки (repr)

    def __setattr__(self, name, value):
        if name != 'data':
            raise AttributeError(
                "Cannot set attributes directly. Use 'data' attribute instead.")  # Запрет прямого изменения атрибутов, использование 'data' атрибута
        else:
            super().__setattr__(name, value)

    def __getitem__(self, key):
        return self.data[key]  # Возможность доступа к элементам коллекции по индексу (__getitem__)

    @staticmethod
    def static_method():
        # Implement static method logic here
        pass

    @classmethod
    def class_method(cls):
        # Implement class method logic here
        pass

    def __iter__(self):
        return iter(self.data)  # Реализация итератора (__iter__)


def main():
    collection = DataCollection()
    collection.count_objects()
    collection.read_from_csv()

    print("ID, Date, Price, Product Name")
    for elem in collection:
        print(elem, *collection[elem])  # Вывод данных из коллекции
    print("\n")

    collection.sort_by_numeric_field()
    collection.sort_by_string_field()
    collection.inference_by_criterion()
    print("")

    collection.add_newline_to_file()


if __name__ == "__main__":
    main()
