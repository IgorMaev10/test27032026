import math # Це для обрахування кількості автобусів
from pywebio.input import input as input_pw, NUMBER, slider, select
from pywebio.output import put_success, put_error, put_warning

students_quantity = input_pw(label='Введіть кількість учнів', type=NUMBER, required=True)
if students_quantity == 0:
    put_error("Помилка")

teachers_quantity = input_pw(label='Введіть кількість вчителів', type=NUMBER, required=True)

transport = select(label='Оберіть тип транспорту', options=['Автобус \U0001F68C', 'Поїзд \U0001F6F2',])
if students_quantity > 40 and 'Автобус \U0001F68C' in transport:
    put_warning("потрібно кілька автобусів")

days = slider(label='На скільки днів ви залишаєтесь', min_value=0, max_value=10, value=5)
if days == 0:
    put_warning("без проживання")

total_visitors_quantity = students_quantity + teachers_quantity
put_success(f"Кількість відвідувачів: {total_visitors_quantity}")

if 'Автобус \U0001F68C' in transport:
    buses_quantity = math.ceil(total_visitors_quantity / 40)
    put_success(f"Потрібно {buses_quantity} автобусів")
    transport_price = 5000 * buses_quantity
if 'Поїзд \U0001F6F2' in transport:
    transport_price = 300 * total_visitors_quantity
put_success(f"Вартість транспорту: {transport_price}грн")
living_cost = total_visitors_quantity * days * 400
put_success(f"Вартість проживання: {living_cost}грн")
total_price = living_cost + transport_price
put_success(f"Загальна вартість поїздки: {total_price}грн")

if total_visitors_quantity > 30:
    put_success(f"Вартість поїздки зі знижкою: {total_price*0.9}грн")