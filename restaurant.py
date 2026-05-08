from pywebio.input import input as input_pw, NUMBER, slider, checkbox, select
from pywebio.output import put_markdown, put_success, put_error, put_warning, put_text, put_column, put_row, put_image
import msg
import images
import prices

guest_name = input_pw(msg.MSG_WELCOME_GUEST, required=True)
put_success(msg.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_error(msg.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_warning(msg.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))

put_markdown("## Меню")

put_row(
    [
        put_column([put_image(images.PIZZA_IMAGE, width='300px', height='200px'), put_text(f'Піцца {prices.PIZZA_PRICE}')]),
        put_column([put_image(images.BURGER_IMAGE, width='300px', height='200px'), put_text(f'Бургер {prices.BURGER_PRICE}')]),
    ]
)
put_row(
    [
        put_column([put_image(images.COLA_IMAGE, width='300px', height='200px'), put_text(f'Кола {prices.COLA_PRICE}')]),
        put_column([put_image(images.CAUSE_IMAGE, width='300px', height='200px'), put_text(f'Соуси {prices.CAUSE_PRICE}')]),
    ]
)
pizza_quantity = input_pw(label='Pizza', type=NUMBER, value=1)
burger_quantity = slider(label='Burger', min_value=0, max_value=10, value=2)
causes = checkbox(label='Causes', options=['майонез', 'кетчуп', 'гірчиця'])
causes_quantity = len(causes)

cola = select(label="Cola", options=['-', 'класична', 'light'])
cola_quantity = 0
if cola != '-':
    cola_quantity = 1

#prices
total_cost_pizza = pizza_quantity * prices.PIZZA_PRICE
total_cost_burger = burger_quantity * prices.BURGER_PRICE
total_cost_cola = cola_quantity * prices.COLA_PRICE
total_cost_causes = causes_quantity * prices.CAUSE_PRICE

total_cost = total_cost_cola + total_cost_burger + total_cost_pizza + total_cost_causes


put_warning()
