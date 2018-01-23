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
    def grau_tratamento_pesc(initial_folder, temp_folder, final_folder, data=''):
        date = datetime.now()
        date = str(date.year) + '-' + str(date.month) + '-' +  str(date.day)


        if data == '':
            date = datetime.now()
            date_pesc = str(date.year) + str(date.month) + str(date.day)
            date = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)


        elif data != '':
            date_pesc = data.replace('-','')
            date = data


        folder = initial_folder

        new_rows_list = []
        for file in os.listdir(folder):
            if file[:file.find('_')] == date and (file.endswith(".txt") or file.endswith(".TXT") or file.endswith(".Txt")):
                print file

                full_file = folder + file


                teste = open(full_file, 'rb')
                reader = open(full_file, 'rb')
                row_counter = open(full_file, 'rb')
                row_count = sum(1 for row in row_counter)

                reader = csv.reader(reader, delimiter=' ', quotechar='|')

                reader = itertools.islice(csv.reader(teste, delimiter=' ', quotechar='|'), 1, row_count-1)

                for row in reader:
                    row = [r.replace('"', '') for r in row]
                    new_rows_list.append(row)

                    final_filename = final_folder + date + '_pesc.txt'

                    cabecalho = itertools.islice(csv.reader(teste, delimiter=' ', quotechar='|'), 0, 1)
                    rodape = itertools.islice(csv.reader(teste, delimiter=' ', quotechar='|'), row_count-2, row_count-1)


                writer = open(final_filename, 'w')
                writer = csv.writer(writer, delimiter=' ', quotechar='|')

                writer.writerow(['00PESC0129CBLC','', '0129' + date_pesc + date_pesc])
                writer.writerows(new_rows_list)
                writer.writerow(['99ESCS0129CBLC','','0129' + date_pesc + '000000000'])
    '''
    def grau_tratamento_pesc(initial_folder, temp_folder, final_folder, data=''):
        date = datetime.now()
        date = str(date.year) + '-' + str(date.month) + '-' +  str(date.day)


        if data == '':
            date = datetime.now()
            date_pesc = str(date.year) + str(date.month) + str(date.day)
            date = str(date.year) + '-' + str(date.month) +  '-' + str(date.day)


        elif data != '':
            date_pesc = data.replace('-','')
            date = data

        folder = initial_folder

        pesc_final = pd.DataFrame()
        for file in os.listdir(folder):
            if (file[:file.find('_')] == date) and (file.endswith(".txt") or file.endswith(".TXT") or file.endswith(".Txt")):
                print 'aqui1'
                print file
                print 'aqui1'
                full_file = folder + file

                pesc = pd.read_csv(full_file, sep='\t', skiprows=1, error_bad_lines=False, index_col=False)
                pesc.loc[pesc.shape[0]+1]=''
                pesc = pesc.shift()
                pesc.loc[0] = pesc.columns
                pesc.iloc[0] = pesc.iloc[0].str.replace('Unnamed.*', '')

                pesc.columns = [i for i in range(pesc.shape[1])]
                pesc = pesc[1:-1]
                pesc_final = pd.concat([pesc_final, pesc])

                pesc_final = pesc_final.reset_index(drop=True)

                temp_filename = 'temp_' + file
                print 'temp_filename', temp_filename


        cabecalho = pd.DataFrame(columns = pesc_final.columns)
        cabecalho.loc[0,0] = '00PESC0129CBLC'
        cabecalho.loc[0,2] = '0129' + date_pesc + date_pesc

        rodape = pd.DataFrame(columns = pesc_final.columns)
        rodape.loc[0,0] = '99ESCS0129CBLC'
        rodape.loc[0,2] = '0129' + date_pesc + '000000000'


        pesc_final = pd.concat([cabecalho, pesc_final, rodape])
        pesc_final = pesc_final.replace('""','')


        temp_filename = temp_folder + temp_filename
        pesc_final.to_csv(temp_filename, sep=' ',index=False, header=False, doublequote=False, quoting=0, escapechar='\\')

        reader = open(temp_filename, 'rb')
        reader = csv.reader(reader, delimiter=' ', quotechar='|')
        new_rows_list = []

        for row in reader:
            row = [r.replace('"', '') for r in row]
            new_rows_list.append(row)

        print 'comeco'
        print temp_filename
        print 'fim'

        final_filename = final_folder + date + '_pesc.txt'

        writer = open(final_filename, 'w')
        writer = csv.writer(writer, delimiter=' ', quotechar='|')
        writer.writerows(new_rows_list)
        '''


print grau_tratamento_pesc.grau_tratamento_pesc(initial_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/downloaded/', temp_folder ='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/temp/', final_folder='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/', data='2018-1-18')
#
# print filecmp.cmp('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/2018-1-15_pesc.txt', '/home/servidor/Desktop/PESC_planner (1).TXT')
# print filecmp.cmp('/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/pesc/final/2018-1-12_pesc.txt', '/home/servidor/Desktop/PESC_planner.TXT')
