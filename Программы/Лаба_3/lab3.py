from pathlib import Path
import csv


def count_obj():  # функция подсчета объектов в определенной директории
    folder_name = input("Enter folder name: ")
    folder = Path(folder_name)
    if folder.is_dir():
        folder_count = len([1 for file in folder.iterdir()])

    print(f"In folder {folder_name} there {folder_count} objects.")


def write_csv(all_data):  # функция записи новый строки в файл
    key_inp = input('Enter key: ')
    date_inp = input('Enter date: ')
    price_inp = input('Enter price: ')
    name_inp = input('Enter name: ')
    all_data[key_inp] = [date_inp, price_inp, name_inp]
    with open('data.csv', 'w') as f:
        for elem in all_data:
            f.write(elem + "," + all_data[elem][0] + "," + all_data[elem][1] + "," + all_data[elem][2] + "\n")
    f.close()


def write_to_dict(all_data):  # функция чтения данных из файла и их занесения их в словарь
    with open("data.csv", "r") as f:
        # reader = csv.DictReader(f)
        reader = csv.reader(f)
        for line in reader:
            all_data[line[0]] = line[1:]


def sort_num_field(all_data):  # функция Сортировки словаря по числовому полю
    print("Сортировка словаря по цене:")
    for elem in sorted(all_data.items(), key=lambda para: int(para[1][1])):
        print(elem[0], *elem[1])
    print("")


def sort_str_field(all_data):  # функция сортировки словаря по строковому полю
    print("Сортировка словаря по названию товара:")
    for elem in sorted(all_data.items(), key=lambda para: para[1][2]):
        print(elem[0], *elem[1])
    print("")


def inference_by_criterion(all_data):  # функция вывода строк словаря в которых наименование товара = 'pizza'
    print("Строки, в которых имя товара 'pizza': ")
    for elem in all_data:
        if all_data[elem][2] == 'pizza':
            print(elem, *all_data[elem])


def main():
    all_data = {}
    count_obj()
    write_to_dict(all_data)

    print("ID, Date, Price, Product Name")
    for elem in all_data:
        print(elem, *all_data[elem])
    print("\n")

    sort_num_field(all_data)
    sort_str_field(all_data)
    inference_by_criterion(all_data)
    print("")

    check = input('Add newline to file? Enter y/n: ')
    if check == 'y':
        write_csv(all_data)
        print("Данные успешно сохранены!")
    else:
        print("Программа остановлена")


if __name__ == "__main__":
    main()
