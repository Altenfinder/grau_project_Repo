from xml.etree import ElementTree
import os
import pandas as pd
import numpy as np
import csv
import glob
from grau_project.grau_bloomberg import functions_bloomberg
from grau_project.grau_comdinheiro import functions_comdinheiro
from grau_project.grau_comdinheiro.grau_comdinheiro import grau_comdinheiro

pd.options.mode.chained_assignment = None

class grau_portfolio_xml:
    def __init__(self, xml_path='', xml_file=''):
        print '__init__ called'
        self.xml_path = xml_path
        self.xml_file = xml_file
        self.xml_full_file = self.xml_path + self.xml_file
        self.dom = ElementTree.parse(self.xml_full_file)

    def parse_header(self, tipo=''):
        tp_isin = self.dom.findall('fundo/header/isin')
        tp_cnpj = self.dom.findall('fundo/header/cnpj')
        tp_nome = self.dom.findall('fundo/header/nome')
        tp_dtposicao = self.dom.findall('fundo/header/dtposicao')
        tp_nomeadm = self.dom.findall('fundo/header/nomeadm')
        tp_cnpjadm = self.dom.findall('fundo/header/cnpjadm')
        tp_nomegestor = self.dom.findall('fundo/header/nomegestor')
        tp_cnpjgestor = self.dom.findall('fundo/header/cnpjgestor')
        tp_nomecustodiante = self.dom.findall('fundo/header/nomecustodiante')
        tp_cnpjcustodiante = self.dom.findall('fundo/header/cnpjcustodiante')
        tp_valorcota = self.dom.findall('fundo/header/valorcota')
        tp_quantidade = self.dom.findall('fundo/header/quantidade')
        tp_patliq = self.dom.findall('fundo/header/patliq')
        tp_valorativos = self.dom.findall('fundo/header/valorativos')
        tp_valorreceber = self.dom.findall('fundo/header/valorreceber')
        tp_valorpagar = self.dom.findall('fundo/header/valorpagar')
        tp_vlcotasemitir = self.dom.findall('fundo/header/vlcotasemitir')
        tp_vlcotasresgatar = self.dom.findall('fundo/header/vlcotasresgatar')
        tp_codanbid = self.dom.findall('fundo/header/codanbid')
        tp_tipofundo = self.dom.findall('fundo/header/tipofundo')
        tp_nivelrsc = self.dom.findall('fundo/header/nivelrsc')


        ###WORKS!
        #a = [i.text for i in tp_isin]

        tp_isin = [i.text for i in tp_isin]
        tp_cnpj = [i.text for i in tp_cnpj]
        tp_nome = [i.text for i in tp_nome]
        tp_dtposicao = [i.text for i in tp_dtposicao]
        tp_nomeadm = [i.text for i in tp_nomeadm]
        tp_cnpjadm = [i.text for i in tp_cnpjadm]
        tp_nomegestor = [i.text for i in tp_nomegestor]
        tp_cnpjgestor = [i.text for i in tp_cnpjgestor]
        tp_nomecustodiante = [i.text for i in tp_nomecustodiante]
        tp_cnpjcustodiante = [i.text for i in tp_cnpjcustodiante]
        tp_valorcota = [i.text for i in tp_valorcota]
        tp_quantidade = [i.text for i in tp_quantidade]
        tp_patliq = [i.text for i in tp_patliq]
        tp_valorativos = [i.text for i in tp_valorativos]
        tp_valorreceber = [i.text for i in tp_valorreceber]
        tp_valorpagar = [i.text for i in tp_valorpagar]
        tp_vlcotasemitir = [i.text for i in tp_vlcotasemitir]
        tp_vlcotasresgatar = [i.text for i in tp_vlcotasresgatar]
        tp_codanbid = [i.text for i in tp_codanbid]
        tp_tipofundo = [i.text for i in tp_tipofundo]
        tp_nivelrsc = [i.text for i in tp_nivelrsc]

        df = pd.DataFrame({
            "isin": tp_isin,
            "cnpj": tp_cnpj,
            "nome": tp_nome,
            "dtposicao": tp_dtposicao,
            "nomeadm": tp_nomeadm,
            "cnpjadm": tp_cnpjadm,
            "nomegestor": tp_nomegestor,
            "cnpjgestor":  tp_cnpjgestor,
            "nomecustodiante": tp_nomecustodiante,
            "cnpjcustodiante": tp_cnpjcustodiante,
            "valorcota": tp_valorcota,
            "quantidade": tp_quantidade,
            "patliq": tp_patliq,
            "valorativos": tp_valorativos,
            "valorreceber": tp_valorreceber,
            "valorpagar": tp_valorpagar,
            "vlcotasemitir": tp_vlcotasemitir,
            "vlcotasresgatar": tp_vlcotasresgatar,
            "codanbid": tp_codanbid,
            "tipofundo": tp_tipofundo,
            "nivelrsc": tp_nivelrsc
        })

        if df.empty:
            return None
        else:
            if tipo == '':
                return df
            elif tipo == 'pl':
                return float(tp_patliq[0])
            elif tipo == 'nome':
                return str(tp_nome[0])
            elif tipo == 'data':
                return str(tp_dtposicao[0])

    def pl(self):
        return grau_portfolio_xml.parse_header(self, tipo='pl')

    def nome(self):
        return grau_portfolio_xml.parse_header(self, tipo='nome')

    def data(self):
        return grau_portfolio_xml.parse_header(self, tipo='nome')

    def parse_acoes(self, tipo=''):

        tp_isin = self.dom.findall('fundo/acoes/isin')
        tp_cusip = self.dom.findall('fundo/acoes/cusip')
        tp_codativo = self.dom.findall('fundo/acoes/codativo')
        tp_qtdisponivel = self.dom.findall('fundo/acoes/qtdisponivel')
        tp_qtgarantia = self.dom.findall('fundo/acoes/qtgarantia')
        tp_lote = self.dom.findall('fundo/acoes/lote')
        tp_valorfindisp = self.dom.findall('fundo/acoes/valorfindisp')
        tp_valorfinemgar = self.dom.findall('fundo/acoes/valorfinemgar')
        tp_puposicao = self.dom.findall('fundo/acoes/puposicao')
        tp_tributos = self.dom.findall('fundo/acoes/tributos')
        tp_percprovcred = self.dom.findall('fundo/acoes/percprovcred')
        tp_tpconta = self.dom.findall('fundo/acoes/tpconta')
        tp_classeoperacao = self.dom.findall('fundo/acoes/classeoperacao')
        tp_dtvencalug = self.dom.findall('fundo/acoes/dtvencalug')
        tp_txalug = self.dom.findall('fundo/acoes/txalug')
        tp_cnpjinter = self.dom.findall('fundo/acoes/cnpjinter')


        tp_isin = [i.text for i in tp_isin]
        tp_cusip = [i.text for i in tp_cusip]
        tp_codativo = [i.text for i in tp_codativo]
        tp_qtdisponivel = [i.text for i in tp_qtdisponivel]
        tp_qtgarantia = [i.text for i in tp_qtgarantia]
        tp_lote = [i.text for i in tp_lote]
        tp_valorfindisp = [i.text for i in tp_valorfindisp]
        tp_valorfinemgar = [i.text for i in tp_valorfinemgar]
        tp_puposicao = [i.text for i in tp_puposicao]
        tp_tributos = [i.text for i in tp_tributos]
        tp_percprovcred = [i.text for i in tp_percprovcred]
        tp_tpconta = [i.text for i in tp_tpconta]
        tp_classeoperacao = [i.text for i in tp_classeoperacao]
        tp_dtvencalug = [i.text for i in tp_dtvencalug]
        tp_txalug = [i.text for i in tp_txalug]
        tp_cnpjinter = [i.text for i in tp_cnpjinter]


        df = pd.DataFrame({
            "isin":tp_isin,
            "cusip":tp_cusip,
            "codativo":tp_codativo,
            "qtdisponivel":tp_qtdisponivel,
            "qtgarantia":tp_qtgarantia,
            "lote":tp_lote,
            "valorfindisp":tp_valorfindisp,
            "valorfinemgar":tp_valorfinemgar,
            "puposicao":tp_puposicao,
            "tributos":tp_tributos,
            "percprovcre":tp_percprovcred,
            "tpconta":tp_tpconta,
            "classeoperacao":tp_classeoperacao,
            "dtvencalug":tp_dtvencalug,
            "txalug":tp_txalug,
            "cnpjinter":tp_cnpjinter
        })

        if df.empty:
            return None
        elif tipo == 'sintetico':
            df_acoes_compradas = df[(df['classeoperacao'] == "C") & (df['qtdisponivel'] > 0)]
            df_acoes_compradas['valor_posicao'] = df_acoes_compradas['valorfindisp'].astype(float)
            df_acoes_compradas['peso'] = df_acoes_compradas['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df_acoes_compradas = df_acoes_compradas[['codativo', 'valor_posicao', 'isin', 'peso']]

            df_acoes_vendidas = df[(df['classeoperacao'] == "V") & (df['qtgarantia'] > 0)]
            df_acoes_vendidas['valor_posicao'] = -df_acoes_vendidas['valorfinemgar'].astype(float)
            df_acoes_vendidas['peso'] = df_acoes_vendidas['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df_acoes_vendidas = df_acoes_vendidas[['codativo', 'valor_posicao', 'isin', 'peso']]

            df = pd.concat([df_acoes_compradas,df_acoes_vendidas])

            df['tipo'] = 'acoes'

            return df.reset_index(drop=True)
        else:
            return df

    def parse_caixa(self, tipo=''):

        tp_isininstituicao = self.dom.findall('fundo/caixa/isininstituicao')
        tp_tpconta = self.dom.findall('fundo/caixa/tpconta')
        tp_saldo = self.dom.findall('fundo/caixa/saldo')
        tp_nivelrsc = self.dom.findall('fundo/caixa/nivelrsc')

        ###WORKS!
        #a = [i.text for i in tp_isin]

        tp_isininstituicao = [i.text for i in tp_isininstituicao]
        tp_tpconta = [i.text for i in tp_tpconta]
        tp_saldo = [i.text for i in tp_saldo]
        tp_nivelrsc = [i.text for i in tp_nivelrsc]

        df = pd.DataFrame({
            "isin": tp_isininstituicao,
            "tpconta": tp_tpconta,
            "saldo": tp_saldo,
            "nivelrsc": tp_nivelrsc,
        })

        if df.empty:
            return None
        elif tipo == 'sintetico':
            df['valor_posicao'] = df['saldo'].astype(float)
            df['peso'] = df['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df['tipo'] = 'caixa'
            df = df[['isin', 'valor_posicao', 'tipo', 'peso']]
            return df
        else:
            return df

    def parse_cotas(self, tipo=''):

        tp_isin= self.dom.findall('fundo/cotas/isin')
        tp_cnpjfundo = self.dom.findall('fundo/cotas/cnpjfundo')
        tp_qtdisponivel = self.dom.findall('fundo/cotas/qtdisponivel')
        tp_qtgarantia = self.dom.findall('fundo/cotas/qtgarantia')
        tp_puposicao = self.dom.findall('fundo/cotas/puposicao')
        tp_tributos = self.dom.findall('fundo/cotas/tributos')
        tp_nivelrsc = self.dom.findall('fundo/cotas/nivelrsc')

        tp_isin = [i.text for i in tp_isin]
        tp_cnpjfundo = [i.text for i in tp_cnpjfundo]
        tp_qtdisponivel = [i.text for i in tp_qtdisponivel]
        tp_qtgarantia = [i.text for i in tp_qtgarantia]
        tp_puposicao = [i.text for i in tp_puposicao]
        tp_tributos = [i.text for i in tp_tributos]
        tp_nivelrsc = [i.text for i in tp_nivelrsc]


        df = pd.DataFrame({
            "isin": tp_isin,
            "tp_cnpjfundo": tp_cnpjfundo,
            "tp_qtdisponivel": tp_qtdisponivel,
            "tp_qtgarantia": tp_qtgarantia,
            "tp_puposicao": tp_puposicao,
            "tp_tributos": tp_tributos,
            "tp_nivelrsc": tp_nivelrsc
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':

            df['valor_posicao'] = (df['tp_puposicao'].astype(float) * df['tp_qtdisponivel'].astype(float))
            df['peso'] = df['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df['tipo'] = 'cotas'
            df = df[['tipo', 'valor_posicao', 'tp_cnpjfundo', 'peso']]
            df.columns = ['tipo', 'valor_posicao', 'cnpj_fundo', 'peso']#### TESTE
            return df.reset_index(drop=True)

        else:
            return df

    def parse_debentures(self, tipo=''):

        tp_isin = self.dom.findall('fundo/debenture/isin')
        tp_coddeb = self.dom.findall('fundo/debenture/coddeb')
        tp_debconv = self.dom.findall('fundo/debenture/debconv')
        tp_debpartlucro = self.dom.findall('fundo/debenture/debpartlucro')
        tp_SPE = self.dom.findall('fundo/debenture/SPE')
        tp_cusip = self.dom.findall('fundo/debenture/cusip')
        tp_dtemissao = self.dom.findall('fundo/debenture/dtemissao')
        tp_dtoperacao = self.dom.findall('fundo/debenture/dtoperacao')
        tp_vencimento = self.dom.findall('fundo/debenture/dtvencimento')
        tp_cnpjemissor = self.dom.findall('fundo/debenture/cnpjemissor')
        tp_qtdisponivel= self.dom.findall('fundo/debenture/qtdisponivel')
        tp_qtgarantia = self.dom.findall('fundo/debenture/qtgarantia')
        tp_depgar = self.dom.findall('fundo/debenture/depgar')
        tp_pucompra = self.dom.findall('fundo/debenture/pucompra')
        tp_puvencimento = self.dom.findall('fundo/debenture/puvencimento')
        tp_puposicao = self.dom.findall('fundo/debenture/puposicao')
        tp_puemissao = self.dom.findall('fundo/debenture/puemissao')
        tp_tributos = self.dom.findall('fundo/debenture/tributos')
        tp_valorfindisp = self.dom.findall('fundo/debenture/valorfindisp')
        tp_valorfinemgar = self.dom.findall('fundo/debenture/valorfinemgar')
        tp_coupom = self.dom.findall('fundo/debenture/coupom')
        tp_indexador = self.dom.findall('fundo/debenture/indexador')
        tp_percindex = self.dom.findall('fundo/debenture/percindex')
        tp_caracteristica = self.dom.findall('fundo/debenture/caracteristica')
        tp_percprovcred = self.dom.findall('fundo/debenture/percprovcred')
        tp_classeoperacao = self.dom.findall('fundo/debenture/classeoperacao')
        tp_idinternoativo = self.dom.findall('fundo/debenture/idinternoativo')
        tp_nivelrsc = self.dom.findall('fundo/debenture/nivelrsc')

        tp_isin = [i.text for i in tp_isin]
        tp_coddeb = [i.text for i in tp_coddeb]
        tp_debconv = [i.text for i in tp_debconv]
        tp_debpartlucro = [i.text for i in tp_debpartlucro]
        tp_SPE = [i.text for i in tp_SPE]
        tp_cusip = [i.text for i in tp_cusip]
        tp_dtemissao = [i.text for i in tp_dtemissao]
        tp_dtoperacao = [i.text for i in tp_dtoperacao]
        tp_vencimento = [i.text for i in tp_vencimento]
        tp_cnpjemissor = [i.text for i in tp_cnpjemissor]
        tp_qtdisponivel = [i.text for i in tp_qtdisponivel]
        tp_qtgarantia = [i.text for i in tp_qtgarantia]
        tp_depgar = [i.text for i in tp_depgar]
        tp_pucompra = [i.text for i in tp_pucompra]
        tp_puvencimento = [i.text for i in tp_puvencimento]
        tp_puposicao = [i.text for i in tp_puposicao]
        tp_puemissao = [i.text for i in tp_puemissao]
        tp_tributos = [i.text for i in tp_tributos]
        tp_valorfindisp = [i.text for i in tp_valorfindisp]
        tp_valorfinemgar = [i.text for i in tp_valorfinemgar]
        tp_coupom = [i.text for i in tp_coupom]
        tp_indexador = [i.text for i in tp_indexador]
        tp_percindex = [i.text for i in tp_percindex]
        tp_caracteristica = [i.text for i in tp_caracteristica]
        tp_percprovcred = [i.text for i in tp_percprovcred]
        tp_classeoperacao = [i.text for i in tp_classeoperacao]
        tp_idinternoativo = [i.text for i in tp_idinternoativo]
        tp_nivelrsc = [i.text for i in tp_nivelrsc]

        df = pd.DataFrame({
        "isin": tp_isin,
        "debpartlucro": tp_debpartlucro,
        "codativo": tp_coddeb,
        "debconv": tp_debconv,
        "SPE": tp_SPE,
        "cusip": tp_cusip,
        "dtemissao": tp_dtemissao,
        "dtoperacao": tp_dtoperacao,
        "dtvencimento": tp_vencimento,
        "cnpjemissor": tp_cnpjemissor,
        "qtdisponivel": tp_qtdisponivel,
        "qtgarantia": tp_qtgarantia,
        "depgar": tp_depgar,
        "pucompra": tp_pucompra,
        "puvencimento": tp_puvencimento,
        "puposicao": tp_puposicao,
        "puemissao": tp_puemissao,
        "tributos": tp_tributos,
        "valor_posicao": tp_valorfindisp,
        #"valorfindisp": tp_valorfindisp,
        "valorfinemgar": tp_valorfinemgar,
        "coupom": tp_coupom,
        "indexador": tp_indexador,
        "percindex": tp_percindex,
        "caracteristica": tp_caracteristica,
        "percprovcred": tp_percprovcred,
        "classeoperacao": tp_classeoperacao,
        "idinternoativo": tp_idinternoativo,
        "nivelrsc": tp_nivelrsc
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df['peso'] = df['valor_posicao'].astype(float) / (grau_portfolio_xml.pl(self))
            df['tipo'] = 'debenture'
            df = df[['codativo', 'valor_posicao', 'isin', 'tipo','dtemissao', 'dtvencimento', 'peso']]
            df = df.reset_index(drop=True)
            return df

        else:
            return df

    def parse_desepesas(self, tipo=''):
        tp_txadm = self.dom.findall('fundo/despesas/txadm')
        tp_tributos = self.dom.findall('fundo/despesas/tributos')
        tp_perctaxaadm = self.dom.findall('fundo/despesas/perctaxaadm')
        tp_vltxperf = self.dom.findall('fundo/despesas/vltxperf')
        tp_perctxperf = self.dom.findall('fundo/despesas/perctxperf')
        tp_percindex = self.dom.findall('fundo/despesas/percindex')
        tp_outtax = self.dom.findall('fundo/despesas/outtax')
        tp_indexador = self.dom.findall('fundo/despesas/indexador')


        tp_txadm = [i.text for i in tp_txadm]
        tp_tributos = [i.text for i in tp_tributos]
        tp_perctaxaadm = [i.text for i in tp_perctaxaadm]
        tp_vltxperf = [i.text for i in tp_vltxperf]
        tp_perctxperf = [i.text for i in tp_perctxperf]
        tp_percindex = [i.text for i in tp_percindex]
        tp_outtax = [i.text for i in tp_outtax]
        tp_indexador = [i.text for i in tp_indexador]

        df = pd.DataFrame({
            "txadm": tp_txadm,
            "tributos": tp_tributos,
            "perctaxaadm": tp_perctaxaadm,
            "vltxperf": tp_vltxperf,
            "perctxperf": tp_perctxperf,
            "percindex": tp_percindex,
            "outtax": tp_outtax,
            "indexador": tp_indexador
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df['valor_posicao'] = -(float(df['txadm']) + float(df['vltxperf']))
            df['peso'] = df['valor_posicao'] / grau_portfolio_xml.pl(self)
            df['tipo'] = 'despesas'
            df = df[['tipo', 'valor_posicao', 'peso']]
            return df

        else:
            return df

    def parse_futuros(self, tipo=''):

        tp_isin = self.dom.findall('fundo/futuros/isin')
        tp_ativo = self.dom.findall('fundo/futuros/ativo')
        tp_cnpjcorretora = self.dom.findall('fundo/futuros/cnpjcorretora')
        tp_serie = self.dom.findall('fundo/futuros/serie')
        tp_quantidade = self.dom.findall('fundo/futuros/quantidade')
        tp_vltotalpos = self.dom.findall('fundo/futuros/vltotalpos')
        tp_tributos = self.dom.findall('fundo/futuros/tributos')
        tp_dtvencimento = self.dom.findall('fundo/futuros/dtvencimento')
        tp_classeoperacao = self.dom.findall('fundo/futuros/classeoperacao')
        tp_vlajuste = self.dom.findall('fundo/futuros/vlajuste')
        tp_hedge = self.dom.findall('fundo/futuros/hedge')
        tp_tphedge = self.dom.findall('fundo/futuros/tphedge')


        tp_isin = [i.text for i in tp_isin]
        tp_ativo = [i.text for i in tp_ativo]
        tp_cnpjcorretora = [i.text for i in tp_cnpjcorretora]
        tp_serie = [i.text for i in tp_serie]
        tp_quantidade = [i.text for i in tp_quantidade]
        tp_vltotalpos = [i.text for i in tp_vltotalpos]
        tp_tributos = [i.text for i in tp_tributos]
        tp_dtvencimento = [i.text for i in tp_dtvencimento]
        tp_classeoperacao = [i.text for i in tp_classeoperacao]
        tp_vlajuste = [i.text for i in tp_vlajuste]
        tp_hedge = [i.text for i in tp_hedge]
        tp_tphedge = [i.text for i in tp_tphedge]

        df = pd.DataFrame({
            "isin": tp_isin,
            "codativo": tp_ativo,
            "cnpjcorretora": tp_cnpjcorretora,
            "serie": tp_serie,
            "quantidade": tp_quantidade,
            "vltotalpos": tp_vltotalpos,
            "tributos": tp_tributos,
            "dtvencimento": tp_dtvencimento,
            "classeoperacao": tp_classeoperacao,
            "vlajuste": tp_vlajuste,
            "hedge": tp_hedge,
            "tphedge": tp_tphedge

        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df_futuros_comprados = df[(df['classeoperacao'] == "C") & (df['quantidade'] > 0)]
            df_futuros_comprados['valor_posicao'] = df_futuros_comprados['vltotalpos'].astype(float)
            df_futuros_comprados['peso'] = df_futuros_comprados['valor_posicao'] / (grau_portfolio_xml.pl(self))

            df_futuros_vendidos = df[(df['classeoperacao'] == "V") & (df['quantidade'] > 0)]
            df_futuros_vendidos['valor_posicao'] = -df_futuros_vendidos['vltotalpos'].astype(float)
            df_futuros_vendidos['peso'] = df_futuros_vendidos['valor_posicao'] / (grau_portfolio_xml.pl(self))

            df = pd.concat([df_futuros_comprados, df_futuros_vendidos])
            df['tipo'] = 'futuros'
            df = df[['codativo', 'valor_posicao', 'isin', 'tipo', 'dtvencimento', 'vlajuste', 'serie', 'peso']]
            df = df.reset_index(drop=True)
            return df

        else:
            return df

    def parse_opcoesacoes(self, tipo=''):

        tp_isin = self.dom.findall('fundo/opcoesacoes/isin')
        tp_cusip = self.dom.findall('fundo/opcoesacoes/cusip')
        tp_ativobase = self.dom.findall('fundo/opcoesacoes/ativobase')
        tp_qtdisponivel = self.dom.findall('fundo/opcoesacoes/qtdisponivel')
        tp_codativo = self.dom.findall('fundo/opcoesacoes/codativo')
        tp_valorfinanceiro = self.dom.findall('fundo/opcoesacoes/valorfinanceiro')
        tp_precoexercicio = self.dom.findall('fundo/opcoesacoes/precoexercicio')
        tp_dtvencimento = self.dom.findall('fundo/opcoesacoes/dtvencimento')
        tp_classeoperacao = self.dom.findall('fundo/opcoesacoes/classeoperacao')
        tp_tributos = self.dom.findall('fundo/opcoesacoes/tributos')
        tp_puposicao = self.dom.findall('fundo/opcoesacoes/puposicao')
        tp_premio = self.dom.findall('fundo/opcoesacoes/premio')
        tp_percprovcred = self.dom.findall('fundo/opcoesacoes/percprovcred')
        tp_tpconta = self.dom.findall('fundo/opcoesacoes/tpconta')
        tp_hedge = self.dom.findall('fundo/opcoesacoes/hedge')
        tp_tphedge = self.dom.findall('fundo/opcoesacoes/tphedge')

        tp_isin = [i.text for i in tp_isin]
        tp_cusip = [i.text for i in tp_cusip]
        tp_ativobase = [i.text for i in tp_ativobase]
        tp_qtdisponivel = [i.text for i in tp_qtdisponivel]
        tp_codativo = [i.text for i in tp_codativo]
        tp_valorfinanceiro = [i.text for i in tp_valorfinanceiro]
        tp_precoexercicio = [i.text for i in tp_precoexercicio]
        tp_dtvencimento = [i.text for i in tp_dtvencimento]
        tp_classeoperacao = [i.text for i in tp_classeoperacao]
        tp_tributos = [i.text for i in tp_tributos]
        tp_puposicao = [i.text for i in tp_puposicao]
        tp_premio = [i.text for i in tp_premio]
        tp_percprovcred = [i.text for i in tp_percprovcred]
        tp_tpconta = [i.text for i in tp_tpconta]
        tp_hedge = [i.text for i in tp_hedge]
        tp_tphedge = [i.text for i in tp_tphedge]

        df = pd.DataFrame({
            "isin":tp_isin,
            "cusip":tp_cusip,
            "ativobase":tp_ativobase,
            "qtdisponivel":tp_qtdisponivel,
            "codativo":tp_codativo,
            "valorfinanceiro":tp_valorfinanceiro,
            "precoexercicio":tp_precoexercicio,
            "dtvencimento":tp_dtvencimento,
            "classeoperacao":tp_classeoperacao,
            "tributos":tp_tributos,
            "puposicao":tp_puposicao,
            "premio":tp_premio,
            "percprovcred":tp_percprovcred,
            "tpconta":tp_tpconta,
            "hedge":tp_hedge,
            "tphedge":tp_tphedge
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df_opcoesacoes_compradas = df[(df['classeoperacao'] == "C") & (df['qtdisponivel'] > 0)]
            df_opcoesacoes_compradas['valor_posicao'] = df_opcoesacoes_compradas['valorfinanceiro'].astype(float)
            df_opcoesacoes_compradas['peso'] = df_opcoesacoes_compradas['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df_opcoesacoes_compradas['tipo'] = 'opcoesacoes'

            df_opcoesacoes_vendidas = df[(df['classeoperacao'] == "V") & (df['qtdisponivel'] > 0)]
            df_opcoesacoes_vendidas['valor_posicao'] = -df_opcoesacoes_vendidas['valorfinanceiro'].astype(float)
            df_opcoesacoes_vendidas['peso'] = df_opcoesacoes_vendidas['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df_opcoesacoes_vendidas['tipo'] = 'opcoesacoes'

            df = pd.concat([df_opcoesacoes_compradas, df_opcoesacoes_vendidas])
            df = df[['codativo', 'valor_posicao', 'isin', 'tipo', 'dtvencimento', 'precoexercicio', 'peso']]
            df = df.reset_index(drop=True)
            return df

        else:
            return df

    def parse_outrasdespesas(self, tipo=''):

        tp_coddesp = self.dom.findall('fundo/outrasdespesas/coddesp')
        tp_valor = self.dom.findall('fundo/outrasdespesas/valor')

        tp_coddesp = [i.text for i in tp_coddesp]
        tp_valor = [i.text for i in tp_valor]

        df = pd.DataFrame({
            "codesp": tp_coddesp,
            "valor": tp_valor,
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df['valor_posicao'] = -df['valor'].astype(float)
            df['peso'] = df['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df['tipo'] = 'outrasdespesas'
            df = df[['tipo', 'valor_posicao', 'valor']]
            return df

        else:
            return df

    def parse_provisoes(self, tipo=''):
        tp_codprov = self.dom.findall('fundo/provisao/codprov')
        tp_credeb = self.dom.findall('fundo/provisao/credeb')
        tp_dt = self.dom.findall('fundo/provisao/dt')
        tp_valor = self.dom.findall('fundo/provisao/valor')

        tp_codprov = [i.text for i in tp_codprov]
        tp_credeb = [i.text for i in tp_credeb]
        tp_dt = [i.text for i in tp_dt]
        tp_valor = [i.text for i in tp_valor]

        df = pd.DataFrame({
            "codprov": tp_codprov,
            "credeb": tp_credeb,
            "dt": tp_dt,
            "valor": tp_valor
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df_credito_provisoes = df[(df['credeb'] == "C") & (df['valor'] > 0)]
            df_credito_provisoes['valor_posicao'] = df_credito_provisoes['valor'].astype(float)
            df_credito_provisoes['peso'] = df_credito_provisoes['valor_posicao'] / (grau_portfolio_xml.pl(self))

            df_debito_provisoes = df[(df['credeb'] == "D") & (df['valor'] > 0)]
            df_debito_provisoes['valor_posicao'] = -df_debito_provisoes['valor'].astype(float)
            df_debito_provisoes['peso'] = df_debito_provisoes['valor_posicao'] / (grau_portfolio_xml.pl(self))

            df = pd.concat([df_credito_provisoes, df_debito_provisoes])
            df['tipo'] = 'provisao'
            df = df[['tipo', 'valor_posicao', 'peso']]
            df = df.reset_index(drop=True)
            return df

        else:
            return df

    def parse_titpublicos(self, tipo=''):
        tp_isin = self.dom.findall('fundo/titpublico/isin')
        tp_codativo = self.dom.findall('fundo/titpublico/codativo')
        tp_dtemissao = self.dom.findall('fundo/titpublico/dtemissao')
        tp_dtoperacao = self.dom.findall('fundo/titpublico/dtoperacao')
        tp_dtvencimento = self.dom.findall('fundo/titpublico/dtvencimento')
        tp_qtdisponivel = self.dom.findall('fundo/titpublico/qtdisponivel')
        tp_qtgarantia = self.dom.findall('fundo/titpublico/qtgarantia')
        tp_depgar = self.dom.findall('fundo/titpublico/depgar')
        tp_pucompra = self.dom.findall('fundo/titpublico/pucompra')
        tp_puvencimento = self.dom.findall('fundo/titpublico/puvencimento')
        tp_puposicao = self.dom.findall('fundo/titpublico/puposicao')
        tp_puemissao = self.dom.findall('fundo/titpublico/puemissao')
        tp_principal = self.dom.findall('fundo/titpublico/principal')
        tp_tributos = self.dom.findall('fundo/titpublico/tributos')
        tp_valorfindisp = self.dom.findall('fundo/titpublico/valorfindisp')
        tp_valorfinemgar = self.dom.findall('fundo/titpublico/valorfinemgar')
        tp_coupom = self.dom.findall('fundo/titpublico/coupom')
        tp_indexador = self.dom.findall('fundo/titpublico/indexador')
        tp_percindex = self.dom.findall('fundo/titpublico/percindex')
        tp_caracteristica = self.dom.findall('fundo/titpublico/caracteristica')
        tp_percprovcred = self.dom.findall('fundo/titpublico/percprovcred')
        tp_classeoperacao = self.dom.findall('fundo/titpublico/classeoperacao')
        tp_idinternoativo = self.dom.findall('fundo/titpublico/idinternoativo')
        tp_nivelrsc = self.dom.findall('fundo/titpublico/nivelrsc')


        tp_isin = [i.text for i in tp_isin]
        tp_codativo = [i.text for i in tp_codativo]
        tp_dtemissao = [i.text for i in tp_dtemissao]
        tp_dtoperacao = [i.text for i in tp_dtoperacao]
        tp_dtvencimento = [i.text for i in tp_dtvencimento]
        tp_qtdisponivel = [i.text for i in tp_qtdisponivel]
        tp_qtgarantia = [i.text for i in tp_qtgarantia]
        tp_depgar = [i.text for i in tp_depgar]
        tp_pucompra = [i.text for i in tp_pucompra]
        tp_puvencimento = [i.text for i in tp_puvencimento]
        tp_puposicao = [i.text for i in tp_puposicao]
        tp_puemissao = [i.text for i in tp_puemissao]
        tp_principal = [i.text for i in tp_principal]
        tp_tributos = [i.text for i in tp_tributos]
        tp_valorfindisp = [i.text for i in tp_valorfindisp]
        tp_valorfinemgar = [i.text for i in tp_valorfinemgar]
        tp_coupom = [i.text for i in tp_coupom]
        tp_indexador = [i.text for i in tp_indexador]
        tp_percindex = [i.text for i in tp_percindex]
        tp_caracteristica = [i.text for i in tp_caracteristica]
        tp_percprovcred = [i.text for i in tp_percprovcred]
        tp_classeoperacao = [i.text for i in tp_classeoperacao]
        tp_idinternoativo = [i.text for i in tp_idinternoativo]
        tp_nivelrsc = [i.text for i in tp_nivelrsc]


        df = pd.DataFrame({
        "isin":tp_isin,
        "codativo":tp_codativo,
        "dtemissao":tp_dtemissao,
        "dtoperacao": tp_dtoperacao,
        "dtvencimento":tp_dtvencimento,
        "qtdisponivel":tp_qtdisponivel,
        "qtgarantia": tp_qtgarantia,
        "depgar": tp_depgar,
        "puvencimento": tp_puvencimento,
        "puposicao": tp_puposicao,
        "puemissao":tp_puemissao,
        "principal":tp_principal,
        "tibutos":tp_tributos,
        "valorfindisp":tp_valorfindisp,
        "valorfinemgar":tp_valorfinemgar,
        "coupom":tp_coupom,
        "indexador":tp_indexador,
        "percindex":tp_percindex,
        "caracteristica":tp_caracteristica,
        "percprovcred":tp_percprovcred,
        "classeoperacao":tp_classeoperacao,
        "idinternoativo":tp_idinternoativo,
        "pucompra": tp_pucompra,
        "nivelrsc":tp_nivelrsc
        })

        if df.empty:
            return None

        elif tipo == 'sintetico':
            df['valor_posicao'] = df['valorfindisp'].astype(float)
            df['peso'] = df['valor_posicao'] / (grau_portfolio_xml.pl(self))
            df['tipo'] = 'titpublicos'
            df = df[['codativo', 'valor_posicao', 'isin', 'tipo', 'dtemissao', 'dtvencimento', 'peso']]
            return df

        else:
            return df

    def portfolio(self, tipo='', apenas_ativos_risco=False, ajustar_pesos=False, ticker_bloomberg=True,ticker_comdinheiro=True):

        if apenas_ativos_risco == True:

            df = pd.concat([grau_portfolio_xml.parse_acoes(self, tipo=tipo), grau_portfolio_xml.parse_caixa(self, tipo=tipo), grau_portfolio_xml.parse_cotas(self, tipo=tipo), grau_portfolio_xml.parse_debentures(self, tipo=tipo), grau_portfolio_xml.parse_futuros(self, tipo=tipo), grau_portfolio_xml.parse_opcoesacoes(self, tipo=tipo), grau_portfolio_xml.parse_titpublicos(self, tipo=tipo)])

            df = df.reset_index(drop=True)

            if ticker_bloomberg == True:
                df['ticker_bloomberg'] = ''
                for i, rows in enumerate(df['tipo']):
                    df['ticker_bloomberg'][i] =  functions_bloomberg.isin_bloomberg(df['isin'][i])

            if ticker_comdinheiro == True:
                df['ticker_comdinheiro'] = ''
                for i, rows in enumerate(df['tipo']):
                    df['ticker_comdinheiro'][i] =  functions_comdinheiro.isin_comdinheiro(df['isin'][i])
                    if df['tipo'][i] == 'debenture':
                        df['ticker_comdinheiro'][i] = df['codativo'][i]



            if ajustar_pesos == True:
                peso = df['peso'].sum()
                df['peso'] = df['peso'].apply(lambda x: x / peso)
                df = df[(df['valor_posicao'] != 0.0)]
                return df
            else:
                return df

        else:
            df = pd.concat([grau_portfolio_xml.parse_acoes(self, tipo=tipo), grau_portfolio_xml.parse_caixa(self, tipo=tipo), grau_portfolio_xml.parse_cotas(self, tipo=tipo), grau_portfolio_xml.parse_desepesas(self, tipo=tipo), grau_portfolio_xml.parse_debentures(self, tipo=tipo), grau_portfolio_xml.parse_futuros(self, tipo=tipo), grau_portfolio_xml.parse_opcoesacoes(self, tipo=tipo), grau_portfolio_xml.parse_outrasdespesas(self, tipo=tipo), grau_portfolio_xml.parse_provisoes(self, tipo=tipo), grau_portfolio_xml.parse_titpublicos(self, tipo=tipo)])

            df.reset_index(drop=True, inplace=True)
            return df


if __name__=='__main__':
    portfolio = grau_portfolio_xml(xml_path='/home/rafael/rafael.chow@graugestao.com.br/xml_planner/xml/atual', #xml_file='FD14298834000130_20171109_20171113093348_Grau Hedge.xml')
    xml_file='FD18716438000136_20171109_20171113093935_OMF FI Multimercado.xml')

    #print portfolio.parse_caixa()
    #print portfolio.parse_acoes()
    #print portfolio.parse_cotas()
    #print portfolio.parse_debentures()
    #print pd.concat([portfolio.parse_cotas(),portfolio.parse_debentures()])
    #print portfolio.portfolio()[['codativo','isin']]
    #print portfolio.portfolio(tipo='sintetico',apenas_ativos_risco=True,ajustar_pesos=False, ticker_bloomberg=True)['ticker_comdinheiro']
    teste = portfolio.portfolio(tipo='sintetico',apenas_ativos_risco=True,ajustar_pesos=False, ticker_bloomberg=True)['ticker_comdinheiro']
    #print functions_comdinheiro.formato_comdinheiro_lista_ativos(teste, tipo='ativos')
    #print functions_comdinheiro.formato_comdinheiro_lista_ativos(teste, tipo='')
    comdinheiro = grau_comdinheiro()
    print comdinheiro.duration(df=teste)
    #print portfolio.portfolio(tipo='sintetico')['peso'].sum()
    #print portfolio.parse_header(tipo='pl')
    #print portfolio.parse_acoes(tipo='')
    #print portfolio.parse_acoes(tipo='sintetico')
    #print portfolio.parse_titpublicos()
    #print portfolio.parse_titpublicos(tipo='sintetico')
