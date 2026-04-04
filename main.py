from src.aeroplanes import Aeroplane
from src.api import AeroplanesAPI
from src.saver import JSONSaver

def user_interaction():
    """
    Функция для реализации основного функционала работы и взаимодействия с пользователем.
    """
    try:
        country = input("Введите название страны: ")

        api = AeroplanesAPI()
        saver = JSONSaver()

        aeroplanes = api.get_aeroplanes(country)
        aeroplanes_country = Aeroplane.cast_to_object_list(aeroplanes)

        # Фильтрация по стране регистрации
        if input("Необходимо ли фильтрация по стране регистрации? y/n ").lower() == "y":
            filter_country = input("Введите названия страны для фильтрации по стране регистрации: ")
            countries = [c.strip() for c in filter_country.split(",")]
            filtered_by_country = []
            for country_name in countries:
                filtered_by_country.extend(Aeroplane.filter_country(country_name, aeroplanes_country))
            aeroplanes_country = filtered_by_country

        # Фильтрация по высоте полёта
        if input("Необходимо ли фильтрация по высоте полёта? y/n ").lower() == "y":
            try:
                altitude_range = int(input("Введите минимальную высоту полёта (м): "))
                aeroplanes_country = Aeroplane.filter_altitude_range(altitude_range, aeroplanes_country)
            except ValueError:
                print("Некорректное значение высоты. Пропускаем фильтрацию.")

        # Топ N самолётов
        if input("Необходимо ли составить топ самолётов? y/n ").lower() == "y":
            try:
                top_n = int(input("Введите количество самолётов для вывода в топ N: "))
                if top_n > len(aeroplanes_country):
                    top_n = len(aeroplanes_country)
                aeroplanes_country = Aeroplane.top_aeroplanes(top_n, aeroplanes_country)
            except ValueError:
                print("Некорректное число для топа.")

        # Сохранение в файл
        if aeroplanes_country:
            saver.add_aeroplane(aeroplanes_country)

            # Вывод результатов
            print("\nРезультаты:")
            for item in aeroplanes_country:
                print(item)
        else:
            print("Нет данных для отображения.")

    except Exception as e:
        print(f"Ошибка: {e}")



if __name__ == "__main__":
    user_interaction()
