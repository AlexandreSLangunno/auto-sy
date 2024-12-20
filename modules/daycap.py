from datetime import datetime, timedelta


def print_days():
    print(
    """
1 - Segunda
2 - Terça
3 - Quarta
4 - Quinta
5 - Sexta
6 - Sábado
7 - Domingo
    """)


def cap_description_day():
    print_days()
    day=int(input("")) - 1
    hoje = datetime.now()
    dia_da_semana = hoje.weekday()
    diferenca = day - dia_da_semana

    if diferenca <= 0:
        diferenca += 7


    dia_feira = hoje + timedelta(days=diferenca)
    data_formatada = dia_feira.strftime("%d/%m/%Y")

    return data_formatada


def cap_calendar_day():
    print_days()
    day=int(input("")) - 1
    hoje = datetime.now()
    dia_da_semana = hoje.weekday()
    diferenca = day - dia_da_semana

    if diferenca <= 0:
        diferenca += 7


    dia_feira = hoje + timedelta(days=diferenca)
    data_formatada = dia_feira.strftime("%d").lstrip("0")

    return data_formatada