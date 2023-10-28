import psutil
import platform
import os
import json
import xml.etree.ElementTree as ET
import zipfile

# Задача 1: Работа с информацией о логических дисках
def convert_bytes(bytes):
    gigabytes = bytes / (1024 ** 3)
    return "{:.2f} GB".format(gigabytes)

def display_logical_drives_info():
    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print("Устройство:", partition.device)
            print("Точка монтирования:", partition.mountpoint)
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                print("Метка тома:", partition.device)
                print("Общий размер:", convert_bytes(partition_usage.total))

                # Получаю тип файловой системы в зависимости от операционной системы
                if platform.system() == "Windows":
                    # Для винды
                    import ctypes
                    drive_type = ctypes.windll.kernel32.GetDriveTypeW(partition.device)
                    if drive_type == 3:
                        print("Тип файловой системы: NTFS")
                    elif drive_type == 5:
                        print("Тип файловой системы: exFAT")
                    else:
                        print("Тип файловой системы: Неизвестно")
                else:
                    # Для других систем (линукс или макос)
                    fs_type = psutil.disk_partitions(all=False)[partitions.index(partition)].fstype
                    print("Тип файловой системы:", fs_type)
            except PermissionError:
                print("Не удалось получить информацию о диске.")
                continue
            print("\n")
    except Exception as e:
        print(f"Произошла ошибка в задаче 1: {e}")




# Задача 2: Работа с файлами

def create_file(file_path):
    try:
        with open(file_path, 'w'):
            pass
        print(f"Файл создан: {file_path}")
    except Exception as e:
        print(f"Ошибка создания файла: {str(e)}")


def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print("Файл заполнен")
    except Exception as e:
        print(f"Ошибка заполнения файла: {str(e)}")


def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Содержание файла: {content}")
    except Exception as e:
        print(f"Ошибка чтения файла: {str(e)}")


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Файд удален: {file_path}")
    except Exception as e:
        print(f"Ошибка удаления файла: {str(e)}")




# Задача 3: Работа с форматом JSON

def create_json_file(jsonchik):
    try:
        with open(jsonchik, 'w') as file:
            json.dump({}, file)
        print(f"Файл формата JSON создан: {jsonchik}")
    except Exception as e:
        print(f"Ошибка создания файла формата JSON: {str(e)}")


def serialize_to_json_and_write(jsonchik, data):
    try:
        with open(jsonchik, 'w') as file:
            json.dump(data, file)
        print("Данные сериализованы и файл заполнен")
    except Exception as e:
        print(f"Ошибка заполнения JSON файла: {str(e)}")


def read_json_file(jsonchik):
    try:
        with open(jsonchik, 'r') as file:
            data = json.load(file)
            print("Содержание JSON файла:")
            print(json.dumps(data, indent=4))
    except Exception as e:
        print(f"Ошибка чтения JSON файла: {str(e)}")


def delete_json_file(jsonchik):
    try:
        os.remove(jsonchik)
        print(f"JSON файл удален: {jsonchik}")
    except Exception as e:
        print(f"Ошибка удаления JSON файла: {str(e)}")



# Задача 4: Работа с форматом XML

def create_xml_file(xml_name):
    try:
        root = ET.Element("data")
        tree = ET.ElementTree(root)
        with open(xml_name, 'wb') as file:
            tree.write(file)
        print(f"XML файл создан: {xml_name}")
    except Exception as e:
        print(f"Ошибка создания XML файла: {str(e)}")


def write_to_xml_file(xml_name, data):
    try:
        tree = ET.ElementTree(file=xml_name)
        root = tree.getroot()
        for key, value in data.items():
            ET.SubElement(root, key).text = str(value)
        tree.write(xml_name)
        print("XML файл заполнен")
    except Exception as e:
        print(f"Ошибка заполнения XML файла: {str(e)}")


def read_xml_file(xml_name):
    try:
        tree = ET.ElementTree(file=xml_name)
        root = tree.getroot()
        data = {}
        for element in root:
            data[element.tag] = element.text
        print("Содержание XML файла:")
        print(data)
    except Exception as e:
        print(f"Ошибка чтения XML файла: {str(e)}")


def delete_xml_file(xml_name):
    try:
        os.remove(xml_name)
        print(f"XML файл удален: {xml_name}")
    except Exception as e:
        print(f"Ошибка удаления XML файла: {str(e)}")




# Задача 5: Создание ZIP-архива, добавление файла, извлечение информации о размере архива

def create_zip_archive(zipka):
    try:
        with zipfile.ZipFile(zipka, 'w', zipfile.ZIP_DEFLATED) as archive:
            pass
        print(f"ZIP архив создан: {zipka}")
    except Exception as e:
        print(f"Ошибка создания ZIP архива: {str(e)}")


def add_file_to_zip(zipka, file_path):
    try:
        with zipfile.ZipFile(zipka, 'a', zipfile.ZIP_DEFLATED) as archive:
            archive.write(file_path, os.path.basename(file_path))
        print(f"Файл заархивирован: {file_path}")
    except Exception as e:
        print(f"Ошибка архивации файла: {str(e)}")


def unzip_and_display_info(zipka, extract_path):
    try:
        with zipfile.ZipFile(zipka, 'r') as archive:
            archive.extractall(extract_path)
            print(f"Файл разархивирован: {extract_path}")
    except Exception as e:
        print(f"Error extracting from ZIP archive: {str(e)}")


def delete_zip_archive(archive_path):
    try:
        os.remove(zipka)
        print(f"ZIP архив удален: {zipka}")
    except Exception as e:
        print(f"Ошибка удаления ZIP архива: {str(e)}")

def wanna_delete(file,flag):
    flag = input(f"Удаляем файл(ы)'{file}'? (да/нет): ").strip().lower()
    if flag == "да":
        print(f"Удаляю файл '{file}'.")
        flag = 1
    else:
        print(f"Не удаляю файл '{file}'.")
        flag = 0


if __name__ == "__main__":
    while True:
            f = input('Выберите, с чем работать:'
                            '\n 1 - Вывести информацию о системе'
                            '\n 2 - Работа с файлами'
                            '\n 3 - Работа с форматом JSON'
                            '\n 4 - Работа с форматом XML'
                            '\n 5 - Работа с ZIP-архивом'
                            '\n 0 - Выход'
                            '\nВведите выбранный номер: ')
            if f == '1':
                print('\nЗадание 1')
                display_logical_drives_info()
            elif f == '2':
                print('\nЗадание 2')
                file_name = "task2.txt"
                create_file(file_name)
                write_to_file(file_name, "Пишу шото в файлик")
                read_from_file(file_name)
                flag = 0
                wanna_delete(file_name,flag)
                if flag == 1:
                    delete_file(file_name)
                else:
                    continue

            elif f == '3':
                print('\nЗадание 3')
                jsonchik = "task3.json"
                create_json_file(jsonchik)
                data_to_serialize = {"name": "sveta", "group": "biso-01-19"}
                serialize_to_json_and_write(jsonchik, data_to_serialize)
                read_json_file(jsonchik)
                wanna_delete(jsonchik, flag)
                if flag == 1:
                    delete_file(jsonchik)
                else:
                    continue
                delete_json_file(jsonchik)
            elif f == '4':
                print('\nЗадание 4')
                # Пример использования
                xml_name = "data.xml"
                create_xml_file(xml_name)
                data_to_write = {"name": "sveta", "group": "biso-01-19"}
                write_to_xml_file(xml_name, data_to_write)
                read_xml_file(xml_name)
                wanna_delete(xml_name, flag)
                if flag == 1:
                    delete_file(xml_name)
                else:
                    continue
                delete_xml_file(xml_name)

            elif f == '5':
                print('\nЗадание 5')
                zipka = "zipka.zip"
                file_to_add = "zipka.txt"
                create_zip_archive(zipka)
                add_file_to_zip(zipka, file_to_add)
                unzip_and_display_info(zipka, "extracted_files")
                wanna_delete(zipka, flag)
                if flag == 1:
                    delete_file(zipka)
                else:
                    continue
                delete_zip_archive(zipka)
            elif f == '0':
                print('Выход из программы.')
                break
            else:
                print('Задачи с таким номером нет. Пожалуйста, выберите другой номер.')
