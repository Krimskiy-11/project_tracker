from src.aeroplanes import Aeroplane
from src.api import AeroplanesAPI
from src.saver import JSONSaver


def user_interaction():
    """
    Функция для реализации основного функционала работы и взаимодействия с пользователем.
    """
    country = input("Введите название страны: ")

    api = AeroplanesAPI()
    aeroplanes = api.get_aeroplanes(country)
    aeroplanes_country = Aeroplane.cast_to_object_list(aeroplanes)

    is_filter_country = input("Необходимо ли фильтрация по стране регистрации? y/n")
    if is_filter_country.lower() == "y":
        filter_country = input("Введите названия стран для фильтрации по стране регистрации: ")
        x = Aeroplane.filter_country(filter_country, aeroplanes_country)
        # print(x)

        is_altitude_range = input("Необходимо ли фильтрация по высоте полета? y/n")
        if is_altitude_range.lower() == "y":
            altitude_range = int(input("Введите диапазон высот полета: "))
            y = Aeroplane.filter_altitude_range(altitude_range, x)
            # print(y)

            is_top = input("Необходимо ли составить топ самолетов? y/n")
            if is_top.lower() == "y":
                top_n = int(input("Введите количество самолетов для вывода в топ N: "))
                z = Aeroplane.top_aeroplanes(top_n, y)

                JSONSaver.add_aeroplane(z)
                for item in z:
                    print(item)
            else:
                JSONSaver.add_aeroplane(y)
                for item in y:
                    print(item)
        else:
            is_top = input("Необходимо ли составить топ самолетов? y/n")
            if is_top.lower() == "y":
                top_n = int(input("Введите количество самолетов для вывода в топ N: "))
                z = Aeroplane.top_aeroplanes(top_n, x)

                JSONSaver.add_aeroplane(z)
                for item in z:
                    print(item)
            else:
                JSONSaver.add_aeroplane(x)
                for item in x:
                    print(item)
    else:
        is_altitude_range = input("Необходимо ли фильтрация по высоте полета? y/n")
        if is_altitude_range.lower() == "y":
            altitude_range = int(input("Введите диапазон высот полета: "))
            y = Aeroplane.filter_altitude_range(altitude_range, aeroplanes_country)
            # print(y)

            is_top = input("Необходимо ли составить топ самолетов? y/n")
            if is_top.lower() == "y":
                top_n = int(input("Введите количество самолетов для вывода в топ N: "))
                z = Aeroplane.top_aeroplanes(top_n, y)

                JSONSaver.add_aeroplane(z)
                for item in z:
                    print(item)
            else:
                JSONSaver.add_aeroplane(y)
                for item in y:
                    print(item)
        else:
            is_top = input("Необходимо ли составить топ самолетов? y/n")
            if is_top.lower() == "y":
                top_n = int(input("Введите количество самолетов для вывода в топ N: "))
                z = Aeroplane.top_aeroplanes(top_n, aeroplanes_country)

                JSONSaver.add_aeroplane(z)
                for item in z:
                    print(item)
            else:
                JSONSaver.add_aeroplane(aeroplanes_country)
                for item in aeroplanes_country:
                    print(item)


if __name__ == "__main__":
    user_interaction()
