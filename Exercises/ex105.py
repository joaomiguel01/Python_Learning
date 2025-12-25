def notas(*grades, sit=False):
    data = dict()
    data['maior'] = max(grades)
    data['menor'] = min(grades)
    data['total'] = len(grades)
    data['media'] = sum(grades)/data['total']

    if sit == True:
        if data['media'] < 5:
            data['situacao'] = "REPROVADO"
        elif data['media'] < 7:
            data['situacao'] = "RECUPERAÇÃO"
        else:
            data['situacao'] = "APROVADO"

    return data

resp = notas(5.5, 2.5, 1.5, sit=False)
print(resp)
    
