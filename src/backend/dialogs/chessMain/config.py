message = tts = \
    """
Шахматы! Правила просты: называешь клетку откуда и клетку куда, а потом я делаю ход.
Скажи "Да" или "Играть", чтобы начать, или "Правила", чтобы прочитать правила.

Важное замечание. Все операции не входят в лимит времени навыков Алисы, поэтому после сообщения о загрузке нужно подождать пару секунд и потом сказать что-угодно.
"""

buttons = [
    "Играть",
    "Правила",
    "Назад",
    "Помощь",
    "Выйти"
]

rules = rules_tts = \
    """
Шахматные правила.
1. Соблюдаются все правила шахмат.
2. Ходы надо говорить в стиле "клетка-клетка", "cNcN", где c - буква, N - номер. Например, e2e4, e-2-e-4, e2-e4 и так далее.
3. Для рокировки надо сказать начальную и конечную клетки.
Скажи "Да" или "Играть", чтобы начать играть.
    """

session_state = {
    "branch": "chessMain",
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }


def getHelpConfig():
    return {
        'message': rules,
        'tts': rules_tts,
        'buttons': buttons,
        'session_state': session_state
    }
