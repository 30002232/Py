from curses import noqiflush
import controller

def cli():
    database = controller.createDatabase()
    while True:
        try:
            command = input().split(" ")
        except EOFError:
            return
        match command[0]:
            case "RC":
                if len(command) != 4:
                    print("Por favor verifique se todas as informações foram introduzidas.")
                elif controller.regConsultant(database, command[1], command[2], command[3]):
                    print("Consultor registado com sucesso.")
                else:
                    print("Não é possivel realizar o registo, consultor já registado.")
            case "RI":
                if len(command) != 8:
                    print("Por favor verifique se todas as informações foram introduzidas.")
                else:
                    nifs = []
                    for element in database[1::]:
                        nifs.append(element[2])
                    #Test
                    #print(f"NIFS: {nifs}")
                    #print(f"Current: {command[1]}")
                    if command[1] not in nifs:
                        print("Não é possivel realizar o registo do imóvel, NIF inválido.")
                    elif controller.regEstate(database, command[1], command[2], command[3], command[4], command[5], command[6], command[7]):
                        print(f"Imóvel com {database[0]} registado com sucesso.")
                        #Test
                        #print(database)
                    #else:
                        #print(f"Last Else: {database}")
            case "LI":
                    nifs = []
                    for element in database[1::]:
                        nifs.append(element[2])
                    if command[1] not in nifs:
                        print("O NIF indicado não pertence a nenhum consultor registado.")
                    elif database[0] == 0:
                        print("Não existem imóveis registados.")
                    else:
                        for element in database[1::]:
                            if element[2] == command[1]:
                                for estateList in element[3]:
                                    print(f"{estateList[0]} {' '.join(estateList[1:3])}")
            case "EI":
                result = controller.deleteEstate(database, command[1], int(command[2]))
                if result == 1:
                    print("O ID indicado é inválido.")
                elif result == 2:
                    print(f"O imóvel {command[2]} não pertence ao consultor indicado.")
                else:
                    print("Imóvel eliminado com sucesso.")
            case "EC":
                allEstate = []
                for i in range(1, len(database[1::])):
                    if database[i][2] == command[1]:
                        for estate in database[i][3]:
                            allEstate.append(str(estate[0]))
                        database.pop(i)
                        print("Consultor eliminado com sucesso.")
                        print(f"Os imóveis {' '.join(allEstate)} também foram eliminados.")   
            case '':
                break
            case default:
                pass
