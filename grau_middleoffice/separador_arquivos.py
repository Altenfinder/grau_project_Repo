from zipfile import ZipFile
import sys
import os
import glob

def separador_arquivos(path, final_path, keywords='', endswith=''):
    for file in os.listdir(path):
        full_file = path + '/' + file
        if endswith != '':
            if file.endswith(endswith):
                if final_path[-1] != '/':
                    final_path = final_path + '/'

                os.rename(full_file, (final_path + file))

        if keywords != '':
            for k in keywords:
                if k in file:
                    os.rename(full_file, (final_path + file))

def zipfile(path, password=''):
    for file in os.listdir(path):
        # print 'FILE', path + file
        full_file = path + file
        if full_file.endswith('.zip'):
            with ZipFile(full_file) as zf:
                if password != '':
                    zf.extractall(pwd=password)
                else: zf.extractall()


#print separador_arquivos('/home/servidor/Documents/attachments', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml', endswith='.xml')

#print separador_arquivos('/home/servidor/Documents/attachments', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/', keywords=['pesc','PESC','Pesc'])

#print separador_arquivos('/home/servidor/Documents/attachments', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/papt/', keywords=['papt','PAPT','Papt'])

#print separador_arquivos('/home/servidor/Documents/attachments', final_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/prod/', keywords=['prod','PROD','Prod'])

#print zipfile('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/papt/', password='planner1')
