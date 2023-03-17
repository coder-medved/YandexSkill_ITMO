import copy
from .responseHelper import createResponse


def updateBranchToResponse(event, response, firstBranchName):
    newEvent = copy.deepcopy(event)
    newResponse = copy.deepcopy(response)

    if 'dontUpdateBranches' in response:
        return response

    if not 'branch' in newEvent['state']['session']:
        newResponse['session_state']['branch'] = [firstBranchName]
        return newResponse

    elif not newResponse['session_state']['branch']:
        newResponse['session_state']['branch'] = newEvent['state']['session']['branch']
        return newResponse

    else:
        eventBranch = newEvent['state']['session']['branch']
        responseState = newResponse['session_state']['branch']

        # если диалог не имел брэнча
        if not responseState:
            newResponse['session_state']['branch'] = eventBranch
            return newResponse

        # сработает, если eventbranch.index(...) найдет новый брэнч в брэнчах
        try:
            index = eventBranch.index(responseState)
            eventBranch = eventBranch[0:index + 1]
            newResponse['session_state']['branch'] = eventBranch
            return newResponse

        # в случае, если в брэнчах нету нового бренча
        except:
            eventBranch.append(responseState)
            newResponse['session_state']['branch'] = eventBranch
            return newResponse


def getDialogResponseFromEnd(event, dialogNumber, dialogs):
    branchList = event["state"]["session"]["branch"]
    if dialogNumber > len(branchList):
        return dialogs[branchList[0]]['getResponse'](event, None)
    return dialogs[branchList[-dialogNumber]]['getResponse'](event, None)
