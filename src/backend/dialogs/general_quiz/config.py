import json
import copy
import random
from utils.responseHelper import *

with open("questions.json") as file:
    questions = json.loads(file.read())

buttons = [
    "Повторить ещё раз",
    "Что ты умеешь?",
    "Помощь",
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "start_quiz"
}


def getConfig(event):
    message = questions["questions"][getState(event, "questions_list")[-1]]
    correct_answer = questions["answers"][getState(event, "questions_list")[-1]]
    answers = copy.deepcopy(questions["uncorrect_answers"][getState(event, "questions_list")[-1]])
    answers[random.randint(0, len(answers) - 1)] = correct_answer
    buttons_response = answers + buttons
    states = {
        "count_questions": event["state"]["session"]["count_questions"],
        "count_correct_response": event["state"]["session"]["count_correct_response"],
        "questions_list": event['state']['session']['questions_list']
    }

    states.update(session_state)

    return {
        'message': message,
        'tts': message,
        'buttons': buttons_response,
        'session_state': states
    }


def getFinishConfig(event):
    buttonsResponse = copy.deepcopy(buttons)
    buttonsResponse.append('меню')
    return {
        'message': "Ваш результат: " + str(getState(event, "count_correct_response")) + "/" + str(
            getState(event, "count_questions")),
        'tts': "Ваш результат:" + str(getState(event, "count_correct_response")) + "из" + str(
            getState(event, "count_questions")),
        'buttons': buttonsResponse,
        'session_state': {
            "branch": "mainMenu"
        }
    }


def check_answer(event):
    questions_list = getState(event, "questions_list")

    if len(questions_list) != 0:
        if questions["answers"][questions_list[-1]].lower() in getCommand(event):
            setStateInEvent(event, "count_correct_response", getState(event, "count_correct_response") + 1)
            print('+1')

    setStateInEvent(event, "count_questions", getState(event, "count_questions") + 1)

    track_question = random.randint(0, len(questions['questions']) - 1)
    while track_question in questions_list:
        track_question = random.randint(0, len(questions['questions']) - 1)

    questions_list.append(track_question)

    setStateInEvent(event, "questions_list", questions_list)
