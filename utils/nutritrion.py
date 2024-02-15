import random

milks_derivatives = [
    ('1 taza de leche descremada', 10),
    ('1 yogurt diet o Light', 10),
    ('1 Taza de te', 0),
    ('1 taza de café', 0)
]

breads_cookies = [
    ('1 rebanada de pan molde integral', 15),
    ('1 galleta de agua', 5),
    ('1 galleta integral', 5),
    ('1 pampita', 15),
    ('1 pan hallulla pequeña (50g)', 30),
    ('1 diente de pan francés', 30),
    ('3 cucharadas de avena', 15)
]

aggregates = [
    ('1 trozo quesillo (tamaño cajafosforo)', 5),
    ('1 cucharada de palta', 2),
    ('1 trozo jamon de pavo cocido (40g)', 0),
    ('1 cucharada mermelaa diet', 3),
    ('1 huevo', 0),
]

THRESHOLD = 50


def generate_breakfast():
    response = []
    sum = 0
    while sum < THRESHOLD:
        random_milk = random.randint(0, len(milks_derivatives) - 1)
        random_breads = random.randint(0, len(breads_cookies) - 1)
        random_aggregates = random.randint(0, len(aggregates) - 1)

        response.append(aggregates[random_aggregates])
        sum += aggregates[random_aggregates][1]
        response.append(milks_derivatives[random_milk])
        sum += milks_derivatives[random_milk][1]
        response.append(breads_cookies[random_breads])
        sum += breads_cookies[random_breads][1]

    return ' | '.join([f'{item[0]} - {item[1]}' for item in response])


print(generate_breakfast())
