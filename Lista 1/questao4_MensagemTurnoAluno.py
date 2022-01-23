turno = str(input("Informe em qual turno você estuda!\nDigite:\nM para matutino,\nV para vespertino,\nN para noturno:\n"))

if (turno == "M"):
    print("Bom Dia!")

elif (turno == "V"):
    print("Boa Tarde!")

elif (turno == "N"):
    print("Boa Noite!")

else:
    print("Valor inválido!")