import openpyxl
from PIL import Image, ImageDraw, ImageFont

# Carregar dados da planilha
workbook = openpyxl.load_workbook('planilha_alunos.xlsx')
students_page = workbook['Sheet1']

for index, row in enumerate(students_page.iter_rows(min_row=2, max_row=11)):
    # Pegar dados da planillha (curso, nome, tipo, data inicio, data fim, carga horária,
    # data emissão do certifiado)
    course_name = row[0].value
    student_name = row[1].value
    participation = row[2].value
    start_date = row[3].value
    final_date = row[4].value
    workload = row[5].value
    issue_date = row[6].value

    # Transferir os dados da planilha para a imagem do certificado
    # Definindo a fonte
    font_normal = ImageFont.truetype('./tahomabd.ttf', size=90)
    font_date = ImageFont.truetype('./tahoma.ttf', size=55)

    image = Image.open('certificado_padrao.jpg')

    drawned = ImageDraw.Draw(image)

    drawned.text((1030, 825), student_name, fill='black', font=font_normal)
    drawned.text((1085, 945), course_name, fill='black', font=font_normal)
    drawned.text((1455, 1055), participation, fill='black', font=font_normal)
    drawned.text((1500, 1180), str(workload), fill='black', font=font_normal)
    drawned.text((755, 1780), start_date, fill='red', font=font_date)
    drawned.text((755, 1930), final_date, fill='red', font=font_date)
    drawned.text((2225, 1930), issue_date, fill='red', font=font_date)

    image.save(f"./{index}_{student_name}_certificado.png")
