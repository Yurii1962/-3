#ДЗ по уроку "Способы вызова функций"
#
def send_email(message = "сообщение", recipient = "Получатель",  * , sender = ("university.help@gmail.com") ):
    # Строка  recipient и sender содержит "@" ?
    if (recipient.count("@") and (sender.count("@"))):    #1-ый if
        # Строка recipient содержит (.com) ИЛИ (.ru) ИЛИ (.net) ?
        if (recipient.count(".com") or recipient.count(".ru") or recipient.count(".net")) and (sender.count(".com") or sender.count(".ru") or sender.count(".net")):  #2-ой if
            #Строка recipient == sender?
            if recipient == sender:     #3-ий if
                print(f"Невозможно отправить письмо самому себе")
            elif sender == "university.help@gmail.com":     #4-ый if
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            else:   #К 4-му IF
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        else:   # К 3-му IF
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    return

send_email("Это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email("Вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru", sender="urban.info@gmail.com")
send_email("Пожалуйста, исправьте задание", 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email("Напоминаю самому себе о вебинаре", 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')