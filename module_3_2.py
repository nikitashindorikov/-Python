def send_email(message, recipient, *, send="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and any(domain in email for domain in [".com", ".ru", ".net", ".uk"])

    if not is_valid_email(recipient) or not is_valid_email(send):
        return print(f"Невозможно отправить письмо с {send} на {recipient}")
    elif recipient == send:
        return print("Невозможно отправить письмо самому себе")
    elif send == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {send} на адрес {recipient}")
    else:
        return print(f"НЕ СТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {send} на адрес {recipient}")

# Тестирование
send_email("Это сообщение для проверки связи", recipient="vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.info@gmail.com', send='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', send='urban.teacher@mail.uk')
send_email("Вы видите это сообщение как лучший студент курса!", "university.help@gmail.com", send="urban.info@gmail.com")
