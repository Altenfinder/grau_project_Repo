import datetime
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import calendar
from dateutil import parser

'''
Criar funcao para fechar o programa caso seja fds ou feriado.
'''

feriados_ambima = '/usr/lib/python2.7/dist-packages/grau_project/grau_datas/feriados_nacionais.xls'
def dias_uteis_restantes_mes(ano,mes,dia):#colocar data atual para calcular quantos dias uteis restam para o final do mes.
    dias_sem_feriado=0

    dias_do_mes = calendar.monthrange(ano,mes)
    for i in range(1, dia+1):
        data = parser.parse(str(ano)+'-'+str(mes)+'-'+str(i))
        dias_sem_feriado -= contador_sem_feriado(data)

    fds=0
    fds += len([1 for i in calendar.monthcalendar(ano,mes) if i[5] != 0])
    fds += len([1 for i in calendar.monthcalendar(ano,mes) if i[6] != 0])

    for i in range(1,dias_do_mes[1]+1):
        data = parser.parse(str(ano)+'-'+str(mes)+'-'+str(i))
        dias_sem_feriado += contador_sem_feriado(data)
    dias_restantes=dias_sem_feriado
    return dias_restantes


def dias_uteis_mes(ano,mes,dia):#para descobrir quantos dias uteis tem um mes.
    dias_sem_feriado=0
    dias_do_mes = calendar.monthrange(ano,mes)
    for i in range(1, dia+1):
        data = parser.parse(str(ano)+'-'+str(mes)+'-'+str(i))
        dias_sem_feriado += contador_sem_feriado(data)

    fds=0
    fds += len([1 for i in calendar.monthcalendar(ano,mes) if i[5] != 0])
    fds += len([1 for i in calendar.monthcalendar(ano,mes) if i[6] != 0])
    dias_uteis=dias_sem_feriado-fds
    return dias_uteis


def parse_date(date):
    hora = date.split('_')[1]
    date = date.split('_')[0].split('-')

    year = date[0]
    month = date[1]
    day = date[2]

    if month[0] == '0':
        month = month[1]
    if day[0] == '0':
        day = day[1]

    final_date = year + '-' + month + '-' + day + '_' + hora
    return final_date


def contador_sem_feriado(date=''):
    df = pd.read_excel(feriados_ambima).set_index('Data')

    if date in df.index:
        return 0
    else:
        return 1





def data_papt_prod(delta_days=0, data=''):
    '''
    Para avancar o numero de dias, colocar delta_days > 0.
    Para retroceder o numero de dias, colocar delta_days < 0.
    :param delta_days: dias a serem descontados
    :return: data no formato dd/mm/aaaa
    '''
    if data == '':
        now = datetime.now()
        day = (now + timedelta(days=delta_days)).day
        month = (now + timedelta(days=delta_days)).month
        year = (now + timedelta(days=delta_days)).year

    else:
        if isinstance(data, str):
            data = data.split('-')
            year = data[0]
            month = data[1]
            day = data[2]
        else:
            day = data.day
            month = data.month
            year = data.year

    day = str(day)
    month = str(month)
    year = str(year)

    if int(day) < 10:
        day = '0' + day

    if int(month) < 10:
        month = '0' + month

    date =  day + month + year[-2:]
    return date

def feriado_check():
    df = pd.read_excel(feriados_ambima).set_index('Data')
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    if today in df.index:
        return sys.exit() #Exception('Feriado')
    else:
        return 'Nao eh feriado'

def numero_feriados(data_vencimento):
    '''
    Precisa ter o calendario Ambima adapatado para funcionar
    :param data_vencimento:
    :return: numero de feriados ate a data de vencimento
    '''
    path = feriados_ambima
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    i = 1
    y = 1

    now = datetime.now()
    ini_year = now.year
    ini_month = now.month
    ini_day = now.day

    if ini_month < 10:
        ini_month = '0' + str(ini_month)

    if ini_day < 10:
        ini_day = '0' + str(ini_day)
    today = str(ini_year) + str(ini_month) + str(ini_day)
    today = int(today)

    date = 20010101

    while date < today:
        y += 1

        year = xlrd.xldate_as_tuple(ws.cell_value(y, 0), wb.datemode)[0]
        month = xlrd.xldate_as_tuple(ws.cell_value(y, 0), wb.datemode)[1]
        day = xlrd.xldate_as_tuple(ws.cell_value(y, 0), wb.datemode)[2]

        if month < 10:
            month = '0' + str(month)

        if day < 10:
            day = '0' + str(day)

        date = str(year) + str(month) + str(day)
        date = int(date)

    date = 20010101

    while date < data_vencimento:

        year = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)[0]
        month = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)[1]
        day = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)[2]

        if month < 10:
            month = '0' + str(month)

        if day < 10:
            day = '0' + str(day)

        date = str(year) + str(month) + str(day)
        date = float(date)

        i += 1

    if data_vencimento == date:
        return (i - y)
    else:
        return (i - y - 1)

def dias_uteis(data_vencimento, data_inicial=''):
    '''
    :param data_vencimento:
    :return: o numero de dias uteis ate a data de vencimento.
    '''
    #try:
        ## INITIAL DATE = TODAY
    if data_inicial == '':
        now = datetime.now()
        ini_year = now.year
        ini_month = now.month
        ini_day = now.day

    else:
        ini_year = data_inicial.year
        ini_month = data_inicial.month
        ini_day = data_inicial.day

    if ini_month < 10:
        ini_month = '0' + str(ini_month)

    if ini_day < 10:
        ini_day = '0' + str(ini_day)

    today = date(int(ini_year), int(ini_month), int(ini_day))

    ## FINAL DATE = DATA VENCIMENTO
    fin_date = str(data_vencimento)
    fin_year = str(fin_date[0:4])
    fin_month = fin_date[4:6]
    fin_day = fin_date[6:8]

    if fin_month < 10:
        fin_month = '0' + str(fin_month)

    if fin_day < 10:
        fin_day = '0' + str(fin_day)

        #    final_date = (str(fin_year) + str(fin_month) + str(fin_day))
    fin_month = int(fin_month)
    fin_day = int(fin_day)
    print fin_day
    final_date = date(int(fin_year), int(fin_month), int(fin_day))


    pm = np.busday_count(today, final_date)
    numero_feriados = holidays(data_vencimento)

    if (pm - numero_feriados) > 0:
        return pm - numero_feriados
    elif (pm - numero_feriados) < 0:
        return 0
    else:
        return 'nan'

    #except Exception as e:
        #print e.args

def data_log(delta_days=0, data=''):
    '''
    Para avancar o numero de dias, colocar delta_days > 0.
    Para retroceder o numero de dias, colocar delta_days < 0.
    :param delta_days: dias a serem descontados
    :return: data no formato dd/mm/aaaa
    '''
    if data == '':
        now = datetime.now()
        day = (now + timedelta(days=delta_days)).day
        month = (now + timedelta(days=delta_days)).month
        year = (now + timedelta(days=delta_days)).year

    else:
        if isinstance(data, str):
            data = data.split('-')
            year = data[0]
            month = data[1]
            day = data[2]
        else:
            day = data.day
            month = data.month
            year = data.year

    day = str(day)
    month = str(month)
    year = str(year)

    if int(day) < 10:
        day = '0' + day

    if int(month) < 10:
        month = '0' + month

    date =  year + '-' + month + '-' + day
    return date

def data_pesc(delta_days=0, data=''):
    '''
    Para avancar o numero de dias, colocar delta_days > 0.
    Para retroceder o numero de dias, colocar delta_days < 0.
    :param delta_days: dias a serem descontados
    :return: data no formato dd/mm/aaaa
    '''
    if data == '':
        now = datetime.now()
        day = (now + timedelta(days=delta_days)).day
        month = (now + timedelta(days=delta_days)).month
        year = (now + timedelta(days=delta_days)).year

    else:
        if isinstance(data, str):
            data = data.split('-')
            year = data[0]
            month = data[1]
            day = data[2]
        else:
            day = data.day
            month = data.month
            year = data.year

    day = str(day)
    month = str(month)
    year = str(year)

    if int(day) < 10:
        day = '0' + day

    if int(month) < 10:
        month = '0' + month

    date =  year + month + day
    return date

def padrao_brasileiro_datas(delta_days=0, data=''):
    '''
    Para avancar o numero de dias, colocar delta_days > 0.
    Para retroceder o numero de dias, colocar delta_days < 0.
    :param delta_days: dias a serem descontados
    :return: data no formato dd/mm/aaaa
    '''
    if data == '':
        now = datetime.now()
        day = (now + timedelta(days=delta_days)).day
        month = (now + timedelta(days=delta_days)).month
        year = (now + timedelta(days=delta_days)).year

    else:
        day = data.day
        month = data.month
        year = data.year

    day = str(day)
    month = str(month)
    year = str(year)

    if int(day) < 10:
        day = '0' + day

    if int(month) < 10:
        month = '0' + month

    date = day + '/' + month + '/' + year
    return date

def delta_n_meses(numero_meses):
    '''
    Caso deseje-se voltar n meses, explicitar o '-'
    :return: data de fechamento do ano anterior
    '''
    delta = (datetime.now() + relativedelta(months=numero_meses)).replace(hour=0, minute=0, second=0, microsecond=0)
    return delta

def retroceder_mes(data='', complemento=True):
    '''
    :return: data de fechamento do mes anterior
    '''
    if data == '':
        data = datetime.now().replace(day=1)
    else:
        data = data.replace(day=1)

    lastMonth = data - timedelta(days=1)
    lastMonth = lastMonth.replace(hour=0, minute=0, second=0, microsecond=0)

    if complemento == True:
        return lastMonth
    elif complemento == False:
        lastMonth = str(lastMonth.year) + "-" + str(lastMonth.month) + "-" + str(lastMonth.day)
        return lastMonth

def retroceder_ano(data='', complemento=True):
    '''
    :param:
        data = data especifica a partir da qual deseja-se calcular.
    :return: data de fechamento do ano anterior
    '''
    if data == '':
        data = datetime.now().replace(day=1).replace(month=1)
    else:
        data = data.replace(day=1).replace(month=1)

    lastYear = data - timedelta(days=1)
    lastYear = lastYear.replace(hour=0, minute=0, second=0, microsecond=0)

    if complemento == True:
        return lastYear
    elif complemento == False:
        lastYear = str(lastYear.year) + "-" + str(lastYear.month) + "-" + str(lastYear.day)
        return lastYear

def data_britech(delta_days=0, data=''):
    '''
    Para avancar o numero de dias, colocar delta_days > 0.
    Para retroceder o numero de dias, colocar delta_days < 0.
    :param delta_days: dias a serem descontados
    :return: data no formato dd/mm/aaaa
    '''
    if data == '':
        now = datetime.now()
        day = (now + timedelta(days=delta_days)).day
        month = (now + timedelta(days=delta_days)).month
        year = (now + timedelta(days=delta_days)).year

    else:
        day = data.day
        month = data.month
        year = data.year

    day = str(day)
    month = str(month)
    year = str(year)

    if int(day) < 10:
        day = '0' + day

    if int(month) < 10:
        month = '0' + month

    date = month + '/' + day + '/' + year
    return date
