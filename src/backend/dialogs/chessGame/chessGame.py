from .event_move import event_move
from .event_color import event_color
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs):
    def getReponseFunc(event, allDialogs):
        try:
            orientation = getState(event, 'orientation')
        except KeyError:
            orientation = None
            print('Orientation = 0 KAK SUDA POPALO?')

        if orientation:  # т.е. играет и есть цвет
            return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
        else:
            config = event_color(event)
        return createResponse(event, config)

    try:
        orientation = getState(event, 'orientation')
    except KeyError:
        orientation = None
    if orientation:  # т.е. играет и есть цвет
        return createTimeoutResponse(event, allDialogs, getReponseFunc, 'chessGameTimeout')
    else:
        config = event_color(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInContext(event, 'chessGame')


chessGame = {'getResponse': getResponse, 'isTriggered': isTriggered}