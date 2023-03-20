from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return (
        "ченж" in getCommand(event)
        or "чендж" in getCommand(event)
        or "ченж" in getCommand(event)
        or "чанж" in getCommand(event)
        or "чандж" in getCommand(event)
        or "chan" in getCommand(event)
        or "chen" in getCommand(event)
    ) and (
        "ланг" in getCommand(event)
        or "лонг" in getCommand(event)
        or "lang" in getCommand(event)
        or "язык" in getCommand(event)
        or "езык" in getCommand(event)
    )


chooseLanguage = {"getResponse": getResponse, "isTriggered": isTriggered}
