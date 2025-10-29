import openpyxl

workbook = openpyxl.Workbook()

workbook.active.title = "Cadastro_Pessoas"

workbook.active['A1'] = "Nome"
workbook.active['B1'] = "Idade"
workbook.active['C1'] = "Data Nascimento"
workbook.active['D1'] = "Comida"


with open("pessoas.txt", "r", encoding="utf-8") as arq:
    for line in arq:
        line_parts = line.replace("\n", "").split(";")
        workbook.active.append([line_parts[0], line_parts[1],
                                line_parts[2], line_parts[3]])

workbook.save("Pessoas.xlsx")