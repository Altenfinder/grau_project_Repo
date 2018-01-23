from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project.grau_britech_site.grau_britech_site import grau_britech_site
from grau_tratamento_pesc import grau_tratamento_pesc
from grau_project.grau_datas import grau_datas
from datetime import datetime
import separador_arquivos

print grau_datas.feriado_check()

email = grau_leitor_email()
anexo = ['pesc','PESC', 'Pesc', 'negs', 'papt', 'PAPT', 'Papt', 'PROD','Prod','prod','.xml','.zip']

date = datetime.now()
data = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)

arquivo_upload = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/' + data + '_pesc.txt'

print grau_leitor_email.download_all_attachemnts(dir_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/', dir_name='attachments', str_contains_anexo=anexo)

print separador_arquivos.separador_arquivos('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/attachments/', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/downloaded/', keywords=['pesc','PESC','Pesc'])

print separador_arquivos.separador_arquivos('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/attachments/', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/papt/downloaded/', keywords=['papt','PAPT','Papt'])

print separador_arquivos.separador_arquivos('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/attachments/', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/prod/downloaded/', keywords=['prod','PROD','Prod'])

print grau_tratamento_pesc.grau_tratamento_pesc(initial_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/downloaded/', temp_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/temp/', final_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/')

grau_britech_site = grau_britech_site()
print grau_britech_site.upload_importacao_operacoes(tipo_upload='pesc', file_path=arquivo_upload)
