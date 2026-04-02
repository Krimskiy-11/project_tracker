from src.aeroplanes import Aeroplane
from src.api import AeroplanesAPI
from src.saver import JSONSaver

def user_interaction():
    try:
        country = input("Введите название страны: ")
        api = AeroplanesAPI()
        aeroplanes = api.get_aeroplanes(country)
        aeroplanes_country = Aeroplane.cast_to_object_list(aeroplanes)

        if input("Фильтрация по стране? y/n ").lower() == "y":
            filter_country = input("Страна для фильтрации: ")
            aeroplanes_country = Aeroplane.filter_country(filter_country, aeroplanes_country)

        if input("Фильтрация по высоте? y/n ").lower() == "y":
            altitude_range = int(input("Диапазон высот: "))
            aeroplanes_country = Aeroplane.filter_altitude_range(altitude_range, aeroplanes_country)

        if input("Топ N самолётов? y/n ").lower() == "y":
            top_n = int(input("Количество для топа: "))
            aeroplanes_country = Aeroplane.top_aeroplanes(top_n, aeroplanes_country)

        JSONSaver.add_aeroplane(aeroplanes_country)
        for item in aeroplanes_country:
            print(item)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    user_interaction()
