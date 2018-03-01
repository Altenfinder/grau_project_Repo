#encoding: latin-1
import pandas as pd

print '/home/grau/Gestao/GRAU GESTÃO - OPERAÇÕES/GRAU GESTÃO - CONTROLE DE OPERAÇÕES - RENDA FIXA.xlsx'

planilha_rf_path = '/home/grau/Gestao/GRAU GESTÃO - OPERAÇÕES/GRAU GESTÃO - CONTROLE DE OPERAÇÕES - RENDA FIXA.xlsx'
planilha_rf_path = '/home/servidor/Desktop/GRAU GESTÃO - CONTROLE DE OPERAÇÕES - RENDA FIXA.xlsx'

print pd.read_excel(planilha_rf_path)
