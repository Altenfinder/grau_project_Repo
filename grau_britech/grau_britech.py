import pandas as pd
import pyodbc
from grau_project.grau_datas import grau_datas
from datetime import datetime, date, timedelta
import numpy as np

class grau_britech:
    def __init__(self):
        self.dsn = 'sqlserver'
        self.user = 'usr_grau_remote'
        self.password = 'Key@grau!'
        self.database = 'FIN_GRAU'
        self.con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s' % (self.dsn, self.user, self.password, self.database)
        self.cnx = pyodbc.connect(self.con_string)


    def df_to_query_britech(self, dataframe, parenteses=False):
        '''
        :param dataframe: coluna que tem os IdCarteira(s) (referencia da britech
        :return: a coluna com os IDs com os NaNs eliminados, no mesmo formato que se utiliza
        para fazer a query.
        '''
        lista = list(dataframe)
        lista_query = ''
        i = 0
        while i < len(lista):
            if str(lista[i]) == 'NaN' or str(lista[i]) == 'nan':
                i = i + 1

            elemento = int(lista[i])
            lista_query = lista_query + ', ' + str(elemento)

            i = i + 1
        lista_query = lista_query[2:]

        if parenteses == True:
            lista_query = '(' + lista_query + ')'
            return lista_query
        else:
            return lista_query


    def query(self, query):
        '''
        Modelo para leitura de uma query da britech como um
        Dataframe
        '''
        df = pd.read_sql(query, con=self.cnx)
        return df


    def indice(self, indice='cdi', intervalo='', data_especifica='',data_especifica_inicial='', data_especifica_final='', tipo_retorno='', acumular_retorno=False):
        '''
        :param
        indice:
            Especificacao do indice desejado

        intervalo:
            Caso vazio, ira retornar toda a serie historica.
            Caso intervalo == 'dia', ira retornar o dado mais recente.
            Caso intervalo == 'mes', ira retornar os dados do mes corrente.
            Caso intervalo == 'ano', ira retornar os dados do ano corrente.
            Caso desja-se indicar quantos meses deseja-se voltar para fazer a busca, inputar o 'n' de meses.
            Caso desja-se indicar quantos meses deseja-se voltar para fazer a busca, inputar o 'n' de meses.

        tipo_retorno:
            Caso vazio, ira retornar a taxa anual.
            Caso tipo_retorno == 'fator_diario', ira retornar o fator diario.
            Caso tipo_retorno == 'taxa_diaria', ira retornar a taxa diaria.

        acumular_retorno
            Caso False, ira retornar a serie historica de dados.
            Caso True, ira retornar a taxa acumulada
        :return: retorna a serie historica do CDI.
        '''
        if intervalo != '':
            if isinstance(intervalo, (int, long)):
                intervalo = str(intervalo)

        if indice == '1' or indice == 'cdi' or indice == 'CDI':
            indice = '1'

        elif indice == '70' or indice == 'ibov' or indice =='IBOV' or indice == 'ibovespa' or indice == 'Ibovespa':
            indice = '70'


        if intervalo == '':
            df_query = pd.read_sql("select data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where idindice like '" + str(indice) + "';", con=self.cnx).set_index("data")

        elif intervalo == 'dia' and indice == 1:
            df_query = pd.read_sql("select top 1 data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where idindice like '" + str(indice) + "' "
                                     "and data like GETDATE();", con=self.cnx).set_index("data")

        elif intervalo == 'dia' and indice != 1:
            df_query = pd.read_sql("select top 2 data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where idindice like '" + str(indice) + "' "
                                     "order by data desc;", con=self.cnx).set_index("data").sort_index()

        elif intervalo == 'mes':
            df_query = pd.read_sql("select data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where (data between '" + str(grau_datas.retroceder_mes()) +"' "
                                     "and GETDATE()) and idindice like '" + indice + "';", con=self.cnx).set_index("data")

        elif intervalo == 'ano':
            df_query = pd.read_sql("select data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where (data between '" + str(grau_datas.retroceder_ano()) + "' "
                                     "and GETDATE()) and idindice like '" + indice + "';", con=self.cnx).set_index("data")


        elif intervalo == 'data_especifica':

            if data_especifica == 'dia':

                #data_especifica_final = datetime.strptime(str(data_especifica_final), '%Y-%m-%d')
                if indice == '1':
                    df_query = pd.read_sql("select data, valor from fin_grau.dbo.cotacaoindice where data between '" + str(data_especifica_inicial) + "' and '" + str(data_especifica_final) + "' and idindice like " + indice + ";", con=self.cnx).set_index("data")

                elif indice != '1':
                    data_especifica_inicial = data_especifica_final + timedelta(days=-1)

                    df_query = pd.read_sql("select data, valor from fin_grau.dbo.cotacaoindice where data between '" + str(data_especifica_inicial) + "' and '" + str(data_especifica_final) + "' and idindice like " + indice + ";", con=self.cnx).set_index("data")

            if data_especifica == 'mes':
                data = grau_datas.retroceder_mes(data=data_especifica_final, complemento=True)
                df_query = pd.read_sql("select data, valor from fin_grau.dbo.cotacaoindice where data between '" + str(data) + "' and '" + str(data_especifica_final) + "' and idindice like " + indice + ";", con=self.cnx).set_index("data")

            elif data_especifica == 'ano':
                data = grau_datas.retroceder_ano(data=data_especifica_final, complemento=True)
                df_query = pd.read_sql("select data, valor from fin_grau.dbo.cotacaoindice where data between '" + str(data) + "' and '" + str(data_especifica_final) + "' and idindice like " + indice + ";", con=self.cnx).set_index("data")


            elif data_especifica_inicial != '' and data_especifica_final != '':
                df_query = pd.read_sql("select data, valor from fin_grau.dbo.cotacaoindice where data between '" + str(data_especifica_inicial) + "' and '" + str(data_especifica_final) + "' and idindice like " + indice + ";", con=self.cnx).set_index("data")

            else:
                df_query = pd.read_sql("select data, valor "
                                         "from fin_grau.dbo.cotacaoindice "
                                         "where (data between '" + str(data_especifica) + "' "
                                         "and GETDATE()) and idindice like '" + indice + "';", con=self.cnx).set_index("data")


        else:
            df_query = pd.read_sql("select data, valor "
                                     "from fin_grau.dbo.cotacaoindice "
                                     "where Data >= DATEADD (month,-" + str(intervalo) + ",GETDATE()) "
                                     "and idindice like '" + indice + "';", con=self.cnx).set_index("data")



        if indice == '1':
            if tipo_retorno == '':
                df_cdi = df_query
                return df_cdi

            elif tipo_retorno == 'fator':
                df_cdi_fator_diario = (1.0 + df_query['valor'] / 100.0) ** (1.0/252.0)

                if acumular_retorno == False:
                    return df_cdi_fator_diario
                else:
                    return df_cdi_fator_diario.prod(axis=0)

            elif tipo_retorno == 'taxa':
                df_cdi_fator_diario = (1.0 + df_query['valor'] / 100.0) ** (1.0 / 252.0)
                df_cdi_taxa_diaria = df_cdi_fator_diario - 1.0

                if acumular_retorno == False:
                    return df_cdi_taxa_diaria
                else:
                    return df_cdi_fator_diario.prod(axis=0) - 1.0

        elif indice != '1':

            if tipo_retorno == '':
                df_indice = df_query
                return df_indice

            elif tipo_retorno == 'fator':
                df_indice_fator_diario = df_query.pct_change() + 1.0

                if acumular_retorno == False:
                    return df_indice_fator_diario.dropna
                else:
                    return df_indice_fator_diario.prod(axis=0)[0]

            elif tipo_retorno == 'taxa':
                df_indice_taxa_diaria = df_query.pct_change().dropna()

                if acumular_retorno == False:
                    return df_indice_taxa_diaria
                else:
                    return ((1.0 + df_indice_taxa_diaria).prod(axis=0))[0] - 1



    def carteiras(self, cpf_cnpj='', id_britech='', intervalo='',  data_especifica='',data_especifica_inicial='', data_especifica_final='', tipo_retorno='', acumular_retorno=False, data_ultima_atualizacao=False, pl=False):
        '''
        :param cnpj:
        :param id_britech:
        :param intervalo:
        :param tipo_retorno:
        :param acumular_retorno:
        :return:
        '''
        if id_britech != '':
            if isinstance(id_britech, (int, long)):
                id_britech = str(id_britech)

        if cpf_cnpj != '':
            cpf_cnpj = pd.read_sql('select idpessoa, cpfcnpj as cpf_cnpj '
                                     'from fin_grau.dbo.pessoa '
                                     'where cpfcnpj in (' + cpf_cnpj + ');', con=self.cnx).set_index('cpf_cnpj')

            if isinstance(cpf_cnpj, pd.DataFrame):
                id_britech = str(cpf_cnpj.loc[0][0])

            else:
                id_britech = str(cpf_cnpj[0])

        if intervalo == '' or intervalo == 'desde_inicio' or intervalo == 'Desde_inicio' or intervalo == 'inicial':
            df_query = pd.read_sql("select data, cotafechamento, idcarteira "
                                     "from fin_grau.dbo.historicocota "
                                     "where idcarteira in (" + id_britech + ") "
                                     "order by idcarteira asc, data asc;", con=self.cnx).set_index("data")

        elif intervalo == 'dia' and tipo_retorno == 'taxa':
            df_query = pd.read_sql("select top 2 data, cotafechamento "
                                   "from fin_grau.dbo.historicocota "
                                   "where idcarteira in (" + id_britech + ") "
                                   "order by data desc;", con=self.cnx).set_index('data').sort_index()

            df_query = df_query.pct_change().dropna()
            df_query.reset_index(inplace=True)
            return df_query['cotafechamento'][0]

        elif intervalo == 'dia':
            if pl == True:
                df_query = pd.read_sql("select top 1 data, idcarteira, plfechamento "
                                       "from fin_grau.dbo.historicocota "
                                       "where idcarteira in (" + id_britech + ") "
                                       "order by data desc;", con=self.cnx).set_index('idcarteira')

                return df_query

            elif data_ultima_atualizacao == True:
                df_query = pd.read_sql("select top 1 data, idcarteira "
                                       "from fin_grau.dbo.historicocota "
                                       "where idcarteira in (" + id_britech + ") "
                                       "order by data desc;",con=self.cnx).set_index('idcarteira')

                return df_query

            else:
                df_query = pd.read_sql("select top 1 data, cotafechamento, idcarteira "
                                         "from fin_grau.dbo.historicocota "
                                         "where idcarteira in (" + id_britech + ") "
                                         "order by idcarteira asc, data asc;", con=self.cnx).set_index("data")


        elif intervalo == 'mes' or intervalo == 'Mes':
            df_query = pd.read_sql("select data, cotafechamento, idcarteira "
                                     "from fin_grau.dbo.historicocota "
                                     "where (data between '" + str(grau_datas.retroceder_mes()) + "' "
                                     "and GETDATE()) and idcarteira in (" + id_britech + ") "
                                     "order by idcarteira asc, data asc;", con=self.cnx).set_index("data")


        elif intervalo == 'ano' or intervalo == 'Ano':
            df_query = pd.read_sql("select data, cotafechamento, idcarteira "
                                     "from fin_grau.dbo.historicocota "
                                     "where (data between '" + str(grau_datas.retroceder_ano())+ "' and GETDATE()) "
                                     "and idcarteira in (" + id_britech + ") "
                                     "order by idcarteira asc, data asc;", con=self.cnx).set_index("data")


        elif intervalo == 'data_especifica':

            if data_especifica == 'dia':
                data_especifica_final = datetime.strptime(data_especifica_final, '%Y-%m-%d')
                data_especifica_inicial = data_especifica_final + timedelta(days=-1)

                df_query = pd.read_sql("select data, cotafechamento, idcarteira from fin_grau.dbo.historicocota where data between '" + str(data_especifica_inicial) + "' and '" + str(data_especifica_final) + "' and idcarteira like " + id_britech + ";", con=self.cnx).set_index("data")

            if data_especifica == 'mes':
                data = grau_datas.retroceder_mes(data=data_especifica_final, complemento=True)

                df_query = pd.read_sql("select data, cotafechamento, idcarteira from fin_grau.dbo.historicocota where data between '" + str(data) + "' and '" + str(data_especifica_final) + "' and idcarteira like " + id_britech + ";", con=self.cnx).set_index("data")

            elif data_especifica == 'ano':
                data = grau_datas.retroceder_ano(data=data_especifica_final, complemento=True)
                df_query = pd.read_sql("select data, cotafechamento, idcarteira from fin_grau.dbo.historicocota where data between '" + str(data) + "' and '" + str(data_especifica_final) + "' and idcarteira like " + id_britech + ";", con=self.cnx).set_index("data")


            elif data_especifica_inicial != '' and data_especifica_final != '':
                df_query = pd.read_sql("select data, cotafechamento, idcarteira from fin_grau.dbo.historicocota where data between '" + str(data_especifica_inicial) + "' and '" + str(data_especifica_final) + "' and idcarteira like " + id_britech + ";", con=self.cnx).set_index("data")



        elif isinstance(intervalo, (int, long)):
            df_query = pd.read_sql("select data, cotafechamento, idcarteira "
                                     "from fin_grau.dbo.historicocota "
                                     "where Data >= DATEADD (month,-" + str(intervalo) + ",GETDATE()) "
                                     "and idindice in (" + id_britech + ") "
                                     "order by idcarteira asc, data asc;", con=self.cnx).set_index("data")

        if tipo_retorno == '':
            return df_query

        elif tipo_retorno == 'fator':
            df_query = df_query.pct_change().dropna() + 1.0

            if acumular_retorno == False:
                return df_query
            else:
                return df_query.prod(axis=0)

        elif tipo_retorno == 'taxa':
            df_query = df_query.pct_change().dropna()

            if acumular_retorno == False:
                return df_query
            else:
                return (1.0 + df_query).prod(axis=0) - 1.0



    def base_grau(self, id_clientes=''):
        if id_clientes == '':
            return pd.read_sql('select idcarteira, nome, datainiciocota, statusativo, tipocota,'
                                 ' idagentegestor, perfilrisco, idindicebenchmark'
                                 ' from fin_grau.dbo.carteira where idagentegestor like 129', con=self.cnx).set_index('idcarteira')
        else:
            return pd.read_sql('select idcarteira, nome, datainiciocota, statusativo, tipocota, '
                                 'idagentegestor, perfilrisco, idindicebenchmark '
                                 'from fin_grau.dbo.carteira where idcarteira in (' + id_clientes + ');', con=self.cnx).set_index('idcarteira')



    def debentures(self, ativo='', intervalo='', data_especifica='',data_especifica_inicial='', data_especifica_final='', tipo_retorno='', acumular_retorno=False):

        df_query = pd.read_sql('''select * from FIN_GRAU.dbo.HistoricoCota where Data >= DATEADD (month,-4,GETDATE()) and idCarteira
            in (''' + lista_query + ''');''', con=self.cnx).set_index('data')

    def conta_corrente(self):
        df_query = pd.read_sql('''select
                               a.IdCliente
                             , a.Apelido
                             , b.SaldoFechamento
                            from
                                Cliente a
                              , SaldoCaixa b
                            where
                              a.IdCliente = b.IdCliente
                              and convert(varchar(10), b.Data, 103) = convert(varchar(10), '21/09/2017',103)
                              and a.IdCliente < 100
                              and a.StatusAtivo = 1
                              and b.IdConta not in (189, 190, 195, 204, 205, 209, 224, 233, 234, 245, 251, 256, 255, 263, 264)
                              -- and b.SaldoFechamento <> 0
                              and a.IdCliente not in (2, 4, 18, 16, 67, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 96, 97, 99,43,32,47,46,31,59,63,66,53,68,29,3)
                            Order by
                              a.Apelido

                              ''', con=self.cnx).set_index('IdCliente')
        return df_query
#

    def taxa_adm(self):
        df_query = pd.read_sql('''select distinct
                                   a.IdCliente
                                 , a.Apelido
                                 , b.Descricao
                                 , b.Valor
                                 , c.PlFechamento
                                from
                                  Cliente a
                                , LiquidacaoHistorico b
                                , HistoricoCota c
                                where
                                	 a.IdCliente = b.IdCliente
                                 and a.IdCliente = c.IdCarteira
                                 and b.Origem in (801, 802, 810)
                                 and a.IdCliente < 100
                                 and a.IdCliente not in (4, 18, 16,30, 40, 62, 67, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 96, 97, 99)
                                 and a.StatusAtivo = 1
                                 and convert(varchar(10), b.DataLancamento, 103) = convert(varchar(10), '31/05/2017',103)
                                 and b.DataLancamento = c.Data
                                Order by b.Descricao)''', con=self.cnx)

        return df_query

    def indice_wealth(self):
        pass

if __name__=='__main__':
    britech = grau_britech()
    print britech.conta_corrente()
    #print britech.taxa_adm()
