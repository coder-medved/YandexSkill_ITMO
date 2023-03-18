from utils.responseHelper import getGlobalState, getLanguage
from utils.triggerHelper import haveGlobalState
config = {
    "ru-RU": {
        "message": """
            ты выбрал русский
            """,
        "tts": """
            ты выбрал русский
        """,
        "buttons": [
            "Новости",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Расписание сессии",
            "Иностранному студенту",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Задать вопрос",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "КАТАЛОГ",
            "description": """
                so english text :3
            """,
        },
    },
    "en-US": {
        "message": """
            you chose english
            """,
        "tts": """
            you chose english
        """,
        "buttons": [
            "News",
            "Студенческий офис",
            "Первокурсникам",
            "Расписание занятий",
            "Расписание сессии",
            "Иностранному студенту",
            "Общеуниверситетские модули в бакалавриате",
            "Общеуниверситетские модули в магистратуре",
            "Библиотека",
            "Учебные и методические издания",
            "Стипендии",
            "Задать вопрос",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "937455/40f0536e426907808499",
            "title": "КАТАЛОГ",
            "description": """
                so english text :3
            """,
        },
    }
}

session_state = {"branch": "russianMenu"}

import copy
def getConfig(event):
    
    lang = getLanguage(event)
    
    return copy.deepcopy({
        "message": config[lang]["message"],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    })