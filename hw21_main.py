import hw21_utils
from hw21_pywebio_server import username, email_address, message_lengths

def main():
    string_data = {
        'name': username,
        'string_lengths': message_lengths
    }
    mail_body = hw21_utils.create_string_info(data=string_data)

    hw21_utils.send_email(
        recipients=[email_address],
        mail_body=mail_body,
        mail_subject='Обрахування довжини стрічки',
    )

main()