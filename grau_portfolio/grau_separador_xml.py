from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project import grau_utilities
import os
# print grau_leitor_email.download_all_attachemnts(dir_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/', dir_name='attachments',str_contains_anexo=['.XML','.xml'], str_contains_assunto=['PLANNER','XML'])

# print grau_leitor_email.download_all_attachemnts(dir_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/', dir_name='attachments',str_contains_assunto=['PLANNER','XML'])
grau_utilities = grau_utilities()

anexo = ['.xml','.zip']
assunto = ['[XMLs Fundos]', '[PLANNER]']

print grau_leitor_email.download_all_attachemnts(dir_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/', dir_name='attachments', str_contains_assunto=assunto, str_contains_anexo=anexo)

path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/'
unzip_folder = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/unzip/'
xml_folder = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_planner/'

for file in os.listdir(path):
    full_file = path + file
    if file.endswith('.zip'):
        print grau_utilities.zipfile(folder=full_file, destination_folder=unzip_folder)

print grau_utilities.separador_arquivos(path=unzip, final_path=xml_folder, endswith='.xml')
