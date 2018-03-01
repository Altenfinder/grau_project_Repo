# encoding: 'latin-1'

#Nome: Felipe Altenfelder
#Data: 06/02/2018
#Proposito: parse de pdf

from grau_relatorios_pdf import grau_relatorio_pdf
import os
import re
def teste():
    os.system("pdftotext -layout /home/felipe/Desktop/attachments/teste/2018-1-31_16:35:53_CMD\ GLOBAL\ FIM_Carteira_Diaria_30012018.pdf")
    os.system(" lowriter --invisible --convert-to doc /home/felipe/Desktop/attachments/teste/2018-1-31_16:35:53_CMD GLOBAL FIM_Carteira_Diaria_30012018.txt" )
#    grau_relatorio_pdf.relatorio_parse(end_file)
print teste()
