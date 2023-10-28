import hashlib
import itertools
import time
import multiprocessing


# Генерим все возможные комбинации 5-буквенных паролей
def generate_passwords():
    alph = "abcdefghijklmnopqrstuvwxyz"
    return (''.join(p) for p in itertools.product(alph, repeat=5))


# Вычисление хэша SHA-256
def calculate_sha256(pswd):
    return hashlib.sha256(pswd.encode()).hexdigest()


# Проверка хэша
def check_password(pswd, fin_hash):
    return calculate_sha256(pswd) == fin_hash


# Перебор паролей
def bruteforce(fin_hash, thread_num=1):
    pswds = generate_passwords()

    if thread_num > 1:
        pool = multiprocessing.Pool(thread_num)
        result = pool.starmap(check_password, ((pswd, fin_hash) for pswd in pswds))
        pool.close()
        pool.join()
    else:
        result = (check_password(pswd, fin_hash) for pswd in pswds)

    for password, is_match in zip(pswds, result):
        if is_match:
            return password


if __name__ == '__main__':
    filename = input("\nВведите имя файла для хэшей (или создания нового файла): ")

    try:
        with open(filename, 'r') as file:
            fin_hashes = [line.strip() for line in file]
            if not fin_hashes:
                print(f"\nФайл {filename} пуст. Хотите ввести собственные хэши в файл? (да/нет): ")
                user_choice = input()
                if user_choice.lower() == "да":
                    num_hashes = int(input("\nВведите количество хэшей, которые хотите добавить: "))
                    fin_hashes = []
                    for _ in range(num_hashes):
                        new_hash = input("\nВведите хэш: ")
                        fin_hashes.append(new_hash)

                    with open(filename, 'w') as file:
                        for hash_value in fin_hashes:
                            file.write(hash_value + '\n')
                else:
                    print("Выход из программы.")
                    exit(0)
    except FileNotFoundError:
        with open(filename, 'w') as file:
            print(f"Файл {filename} не найден. Создан пустой файл.")
            fin_hashes = []

    while True:
        try:
            choice = input('Введите 1 для продолжения работы программы \nИли введите 0 для выхода из программы: ')
            if choice == "0":
                print('Выход из программы.')
                break

            elif choice == "1":
                thread_num = int(
                    input("Введите количество потоков (1 для однопоточного режима, 0 для завершения программы): "))
                if thread_num == 0:
                    print('Выход из программы.')
                    break

                print("Старт работы")

                for fin_hash in fin_hashes:
                    start_time = time.time()
                    password = bruteforce(fin_hash, thread_num)
                    end_time = time.time()

                    if password:
                        print(f"Найден пароль для хэша {fin_hash}: {password}")
                    else:
                        print(f"Пароль для хэша {fin_hash} не найден.")

                    print(f"Время, затраченное на подбор: {end_time - start_time} секунд")

                print("Работа завершена.")
            else:
                print("Некорректный выбор, попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка при работе: {e}")
