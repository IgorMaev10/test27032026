from messages import MSG_INPUT_NAME, MSG_INPUT_AGE, MSG_INPUT_PHONE, MSG_NAME_OK, MSG_AGE_OK, MSG_PHONE_OK, MSG_FINISH

name = input(MSG_INPUT_NAME)
name = name.strip()
if name.isalpha():
    correct_name = MSG_NAME_OK.format(name=name).title()
    print(correct_name)

age = input(MSG_INPUT_AGE)
age = age.strip(" 0")
if age.isdigit():
    correct_age = MSG_AGE_OK.format(age=age)
    print(correct_age)

phone = input(MSG_INPUT_PHONE)
phone = phone.strip()
if phone.isdigit():
    correct_phone = MSG_PHONE_OK.format(phone=phone)
    print(correct_phone)

print(MSG_FINISH)