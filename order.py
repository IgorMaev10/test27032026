from letter import LETTER_TEMPLATE

name = input("Введіть ваше ім'я та прізвище: ").strip().title()
date = input("Введіть дату поїздки: ").strip()
persons = int(input("Введіть кількість людей (цілим числом): ").strip())

price_per_person = 15000
total_price = price_per_person * persons

if int(persons) > 5:
    discount = int(0.05 * float(total_price))
    final_price = total_price - discount
else:
    discount = 0
    final_price = total_price

letter=(LETTER_TEMPLATE.format(name=name, date=date, persons=persons, price_per_person=price_per_person, total_price=total_price,
                             final_price=final_price, discount=discount))
print(letter)
