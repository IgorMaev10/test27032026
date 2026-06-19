from pywebio.input import input as input_pw

username = input_pw(label='Введіть ваше ім`я', required=True).strip()
email_address = input_pw(label='Введіть вашу електронну пошту', required=True).strip()
message = input_pw(label='Введіть повідомлення, яке хочете відправити', required=True).strip()

message_lengths = len(message)
