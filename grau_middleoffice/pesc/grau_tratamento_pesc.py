from grau_project.grau_datas import grau_datas
import pandas as pd
import os
import sys
import glob
from datetime import datetime
import numpy as np
import csv
import time
import filecmp
import itertools

class grau_tratamento_pesc:
    @staticmethod
    def grau_tratamento_pesc(initial_folder, final_folder, data=''):


        if data == '':
            date = datetime.now()
            date = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)


        elif data != '':
            date = data

        date_pesc = grau_datas.data_pesc(data=data)

        folder = initial_folder

        new_rows_list = []
        cabecalho_list = []
        rodape_list = []
        final_filename = final_folder + date + '_pesc.txt'

        for file in os.listdir(folder):
            if (file[:file.find('_')] == date) and (file.endswith(".txt") or file.endswith(".TXT") or file.endswith(".Txt")):

                full_file = folder + file

                teste = open(full_file, 'rb')
                cabecalho = open(full_file, 'rb')
                rodape = open(full_file, 'rb')
                reader = open(full_file, 'rb')

                row_counter = open(full_file, 'rb')
                row_count = sum(1 for row in row_counter)

                reader = csv.reader(reader, delimiter=' ', quotechar='|')

                reader = itertools.islice(csv.reader(teste, delimiter=' ', quotechar='|'), 1, row_count-1)
                cabecalho = itertools.islice(csv.reader(cabecalho, delimiter=' ', quotechar='|'), 0, 1)
                rodape = itertools.islice(csv.reader(rodape, delimiter=' ', quotechar='|'), row_count-1, row_count-0)

                for row in reader:
                    row = [r.replace('"', '') for r in row]
                    new_rows_list.append(row)

                for c in cabecalho:
                    row = [r.replace('"', '') for r in c]
                    cabecalho_list.append(row)

                for lin in rodape:
                    row = [r.replace('"', '') for r in lin]
                    rodape_list.append(row)

                writer = open(final_filename, 'w')
                writer = csv.writer(writer, delimiter=' ', quotechar=' ')

        final = []

        if len(cabecalho_list) != 1:
            b = False
            i = 0
            while b == False:
                if 'CBLC' in cabecalho_list[i][0]:
                    cabecalho_list = cabecalho_list[i]
                    b = True

                i = i + 1

        final.append(new_rows_list)

        if len(rodape_list) != 1:
            b = False
            i = 0
            while b == False:
                if 'CBLC' in rodape_list[i][0]:
                    rodape_list = rodape_list[i]
                    b = True

                i = i + 1


        for row in final:
            writer.writerow(cabecalho_list)
            for r in row:
                writer.writerow(r)

            writer.writerow(rodape_list)


if __name__=='__main__':
    print grau_tratamento_pesc.grau_tratamento_pesc(initial_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/downloaded/',  final_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/pesc/temp/final/', data='2018-1-29')
#
# print filecmp.cmp('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/2018-1-15_pesc.txt', '/home/servidor/Desktop/PESC_planner (1).TXT')
# print filecmp.cmp('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/2018-1-12_pesc.txt', '/home/servidor/Desktop/PESC_planner.TXT')
