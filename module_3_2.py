def send_email(messange, recipient, *, send="university.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or send) or ("@" or (".com" or ".ru" or ".net")) not in (recipient or send):
        return print("Невозможно отправить письмо с ", "send", "на", "recipient")
    elif recipient is send:
        return print("Невозможно отправить письмо самому себе")
    elif send == "university.help@gmail.com":
        return print("Письмо успешно отправлено с адреса send на адрес recipient")
    elif send != "university.help@gmail.com":
        return print("НЕ СТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса send на  адрес recioient")
send_email("Это сообщение для проверки связи", recipient="vasyok1337@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.info@gmail.com', send='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', send='urban.teacher@mail.uk')
send_email("Вы видите это сообщение как лучший студент курса!", "university.help@gmail.com",send="urban.info@gmail.com")
