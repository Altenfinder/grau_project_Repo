from zipfile import ZipFile
import sys
import os
import glob

class grau_utilities:
    def __init__(self):
        pass

    @staticmethod
    def zipfile(folder, destination_folder, password=''):
        zip_ref = ZipFile(folder, 'r')
        if password != '':
            try:
                zip_ref.extractall(destination_folder, pwd=password)
        else:
            try:
                zip_ref.extractall(destination_folder)

        zip_ref.close()

    @staticmethod
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

if __name__=='__main__':
    path = '/home/servidor/Desktop/attachments/'
    for file in os.listdir(path):
        full_file = path + file
        if file.endswith('.zip'):
            print grau_utilities.zipfile(folder=full_file, destination_folder='/home/servidor/Desktop/unzip/')
