message = \
    """
    Вы направились в категорию "Библиотека"
    
    Библиотека ИТМО — это научно-образовательный центр, предоставляющий все возможности для вашего профессионального роста и развития:
    знакомьтесь с лучшими коллекциями ведущих отечественных и зарубежных издательств по всем отраслям научного знания
    бронируйте необходимую литературу через личный кабинет
    работайте в современных пространствах, организовывайте мероприятия и важные переговоры.
    
    Зарегистрируйте кампусную карту у библиотекаря или администратора коворкинга в качестве читательского билета и пользуйтесь всеми возможностями!
    """

tts = \
    """
    Вы направились в категорию "Библиотека".
    Библиотека ИТМО — это научно-образовательный центр, предоставляющий все возможности для вашего профессионального роста и развития:
    знакомьтесь с лучшими коллекциями ведущих отечественных и зарубежных издательств по всем отраслям научного знания,
    бронируйте необходимую литературу через личный кабинет,
    работайте в современных пространствах, организовывайте мероприятия и важные переговоры.
    Зарегистрируйте кампусную карту у библиотекаря или администратора коворкинга в качестве читательского билета и пользуйтесь всеми возможностями!
    """

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'БИБЛИОТЕКА',
    'description': \
        """
        Зарегистрируйте кампусную карту у библиотекаря или администратора коворкинга в качестве читательского билета и пользуйтесь всеми возможностями!
        """
}

session_state = {
    "branch": "library"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
