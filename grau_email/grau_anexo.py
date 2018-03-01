from grau_project.grau_email.grau_leitor_email import grau_leitor_email
from grau_project.grau_utilities.grau_utilities import grau_utilities
import os
import time

class grau_anexo:
    @staticmethod
    def download_anexos_separacao():
        email = grau_leitor_email()
        anexo = ['pesc','PESC', 'Pesc', 'papt', 'PAPT', 'Papt', 'PROD','Prod','prod','.xml','.zip']

        attachments_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_email'
        full_attachments_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_email/attachments/'

        xml_downloaded_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_portfolio/temp/xml_planner/'
        pesc_downloaded_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/downloaded'
        papt_downloaded_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/papt/temp/downloaded'
        prod_downloaded_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/prod/temp/downloaded'
        #negs_downloaded_path = '/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/negs/downloaded/'

        # Baixo os arquivos
        try:
            print grau_leitor_email.download_all_attachemnts(dir_path=attachments_path, dir_name='attachments', str_contains_anexo=anexo)
        except:
            print 'not able to download all attachments'

        time.sleep(5)

        # Unzip
        for file in os.listdir(full_attachments_path):
            full_file = os.path.join(full_attachments_path, file)
            if file.endswith('.zip') or file.endswith('.zip?='):
                try:
                    print grau_utilities.zipfile(folder=full_file, destination_folder=full_attachments_path, password='planner1')
                except:
                    print 'Nao foi possivel extrair ', full_file



        time.sleep(6)
        # Move os subfiles para o folder principal
        for folder in os.listdir(full_attachments_path):
            full_folder = full_attachments_path + folder
            if os.path.isdir(full_folder):
                for f in os.listdir(full_folder):
                    if (f != None) and (full_folder != None):
                        try:
                            os.rename(os.path.join(full_folder, f), os.path.join(full_attachments_path , f))
                        except:
                            pass


        time.sleep(5)
        # Deleta folders vazios
        for folder in os.listdir(full_attachments_path):
            f = os.path.join(full_attachments_path, folder)
            if os.path.isdir(f):
                if not os.listdir(f):
                    print 'FOLDER VAZIO', f
                    os.rmdir(f)


        # XML
        print grau_utilities.separador_arquivos(full_attachments_path, final_path=xml_downloaded_path, keywords=['.xml'])

        # PESC
        print grau_utilities.separador_arquivos(full_attachments_path, final_path=pesc_downloaded_path, keywords=['pesc','PESC','Pesc'])

        # PAPT
        print grau_utilities.separador_arquivos(full_attachments_path, final_path=papt_downloaded_path, keywords=['papt','PAPT','Papt'])

        # PROD
        print grau_utilities.separador_arquivos(full_attachments_path, final_path=prod_downloaded_path, keywords=['prod','PROD','Prod'])

        # NEGS
        # print grau_utilities.separador_arquivos(full_attachments_path, final_path=negs_downloaded_path, keywords=['negs','NEGS','negs'])

if __name__=='__main__':
    grau_anexo.download_anexos_separacao()
