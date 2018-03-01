from zipfile import ZipFile
import sys
import os
import glob
from subprocess import Popen, PIPE

class grau_utilities:
    @staticmethod
    def zipfile(folder, destination_folder, password='', delete_zip=True):
        zip_ref = ZipFile(folder, 'r')
        try:
            try:
                zip_ref.extractall(destination_folder)
            except:
                zip_ref.extractall(destination_folder, pwd=password)
        except:
            print 'Nao foi possivel extrair ', folder

        zip_ref.close()

        if delete_zip == True:
            os.remove(folder)

    @staticmethod
    def separador_arquivos(path, final_path, keywords='', endswith=''):
        for file in os.listdir(path):
            full_file = os.path.join(path, file)
            if endswith != '':
                if file.endswith(endswith):
                    os.rename(full_file, os.path.join(final_path, file))

            if keywords != '':
                for k in keywords:
                    if k in file:
                        os.rename(full_file, os.path.join(final_path, file))

    @staticmethod
    def keypress(sequence):
        control_f4_sequence = '''key Alternate_L key F4'''
        p = Popen(['xte'], stdin=PIPE)
        p.communicate(input=sequence)



    @staticmethod
    def delete_empty_subfolders(folder):
        full_attachments_path = folder
        for folder in os.listdir(full_attachments_path):
            f = os.path.join(full_attachments_path, folder)
            if os.path.isdir(f):
                if not os.listdir(f):
                    os.rmdir(f)

    @staticmethod
    def move_subfiles_to_main_folder(folder):
        full_attachments_path = folder
        for folder in os.listdir(full_attachments_path):
            full_folder = full_attachments_path + folder
            if os.path.isdir(full_folder):
                for f in os.listdir(full_folder):
                    if (f != None) and (full_folder != None):
                        try:
                            os.rename(os.path.join(full_folder, f), os.path.join(full_attachments_path , f))
                        except:
                            pass

    @staticmethod
    def remove_files_by_extension(folder, extension):
        for file in os.listdir(folder):
            if file.endswith(extension):
                os.remove(file)

    @staticmethod
    def find_most_recent_file(folder_path):
        if folder_path[-1] == '/':
            folder_path = folder_path + '*'
        else:
            folder_path = folder_path + '/*'

        list_of_files = glob.glob(folder_path) # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file


if __name__=='__main__':
    path = '/home/servidor/Desktop/attachments/'
    for file in os.listdir(path):
        full_file = path + file
        if file.endswith('.zip'):
            print grau_utilities.zipfile(folder=full_file, destination_folder='/home/servidor/Desktop/unzip/')
