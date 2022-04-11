'''
- расстояния до пункта назначения:
    - более 30 км: +300 рублей к доставке;
    - до 30 км: +200 рублей к доставке;
    - до 10 км: +100 рублей к доставке;
    - до 2 км: +50 рублей к доставке;
- габаритов груза:
    - большие габариты: +200 рублей к доставке;
    - маленькие габариты: +100 рублей к доставке;
- хрупкости груза. Если груз хрупкий — +300 рублей к доставке. Хрупкие грузы нельзя возить на расстояние более 30 км;
- загруженности службы доставки. Стоимость умножается на коэффициент доставки:
    - очень высокая загруженность — 1.6;
    - высокая загруженность — 1.4;
    - повышенная загруженность — 1.2;
    - во всех остальных случаях коэффициент равен 1.

Минимальная сумма доставки — 400 рублей. Если сумма доставки меньше минимальной, выводится минимальная сумма.

Мысли:
1. Так как я считаю, что условия неполные, то в случае ошибочных данных будем считать, что на выходе будет None.
2. Лучшим вариантом будет выброс исключений с помощью команды raise,
             для написания реального софта, именно так бы я и делал. Но исходя из условия 1, можно упростить себе задачу
'''
import math


def create_dict_of_distance():
    value_to = [50, 100, 200, 300]

    key_to = [
        [*range(0, 2)],
        [*range(2, 10)],
        [*range(10, 30)],
        [*range(30, 200)],
    ]

    distance_to_sum = {key: value_to[0] for key in key_to[0]}
    distance_to_sum_100 = {key: value_to[1] for key in key_to[1]}
    distance_to_sum_200 = {key: value_to[2] for key in key_to[2]}
    distance_to_sum_300 = {key: value_to[3] for key in key_to[3]}

    distance_to_sum.update(distance_to_sum_100)
    distance_to_sum.update(distance_to_sum_200)
    distance_to_sum.update(distance_to_sum_300)

    return distance_to_sum


def count_on_distance(distance):
    distance = math.ceil(distance)

    if distance >= 200:
        return None
    distance_to_sum = create_dict_of_distance()

    return distance_to_sum[distance]


def count_on_profile(profile):
    profile = profile.lower()

    if profile == "большие габариты":
        return 200
    elif profile == "маленькие габариты":
        return 100
    else:
        return None


def count_on_fragility(fragility, distance):
    if fragility == 1 and distance < 30:
        return 300
    elif fragility != 1:
        return 0
    else:
        return None


def stress_of_delivery(level_of_stress):
    level_of_stress = level_of_stress.lower()

    dict_of_levels = {
        'очень высокая загруженность': 1.6,
        'высокая загруженность': 1.4,
        'повышенная загруженность': 1.2,
        'default': 1
    }

    try:
        return dict_of_levels[level_of_stress]
    except KeyError:
        return None


def count_of_delivery(distance, profile, fragility, level_of_stress="default"):
    """
    :param distance: int выраженный в километрах.метрах
    :param profile:  string либо большие габариты либо маленькие габариты
    :param fragility: boolean 1 или 0
    :param level_of_stress: очень высокая загруженность, высокая загруженность, повышенная загруженность, либо ничего
    :return: int в рублях
    """
    sum_on_fragility = count_on_fragility(fragility, distance)
    sum_on_distance = count_on_distance(distance)
    sum_on_profile = count_on_profile(profile)
    sum_on_stress = stress_of_delivery(level_of_stress)
    try:
        sum_of_delivery = sum_on_fragility + sum_on_distance + sum_on_profile + sum_on_stress
    except Exception:
        return None

    if sum_of_delivery < 400:
        return 400
    else:
        return sum_of_delivery
