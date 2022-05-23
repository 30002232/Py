import model

def createDatabase():
    return [0]

def regConsultant(database, firstName, lastName, nif):
    if len(database) == 1:
        database.append([firstName, lastName, nif, []])
        return True
    else:
        for element in database[1::]:
            if element[2] == nif:
                return False
            else:
                database.append([firstName, lastName, nif, []])
                return True

def regEstate(database, consultantNIF, estateLocation, estateArea, estateTopology, estateYear, estateValue, estateComission):    
    consultantPosition = 1
    for element in database[1::]:
        if element[2] == consultantNIF:
            database[0] += 1
            database[consultantPosition][3].append([database[0], estateValue, estateComission, estateLocation, estateArea, estateYear])
            return True
        else:
            consultantPosition += 1

def deleteEstate(database, consultantNIF, estateID):
    availableEstates = []
    #Get list of consultant's estates
    for element in database[1::]:
        #Get individual estates
        for estate in element[3]:
            availableEstates.append(estate[0])
    if estateID > database[0] or estateID not in availableEstates:
        return 1
    else:
        consultantIndex = 1
        for consultant in database[1::]:
            estateIndex = 0
            for estate in consultant[3]:
                if consultant[2] == consultantNIF and estate[0] == estateID:
                    database[consultantIndex][3].pop(estateIndex)
                    return 0
                else:
                    estateIndex += 1
            consultantIndex += 1                 
    return 2
