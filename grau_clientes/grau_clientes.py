import pandas as pd

class grau_clientes:
    @staticmethod
    def tabela_id():
        df_cliente = pd.read_csv('/usr/lib/python2.7/dist-packages/grau_project/grau_clientes/codigos_clientes.csv', dtype={'id_britech':str, 'id_planner':str, 'id_xp':str,'id_genial':str}).set_index('id_britech')

        return df_cliente

    @staticmethod
    def conversor_id(id, id_in='britech', id_out='planner'):
        df_clientes = grau_clientes.tabela_id()

        if id_in =='britech' and id_out=='planner':
            return df_clientes['id_planner'][id]

        elif id_in =='planner' and id_out=='britech':
            df_clientes['id_britech'] = df_clientes.index
            df_clientes = df_clientes.set_index('id_planner')
            return df_clientes['id_britech'][id]

if __name__=='__main__':
    a = grau_clientes()
    print grau_clientes.conversor_id('51')
    print grau_clientes.conversor_id(id='38203-5', id_in='planner', id_out='britech')
    print grau_clientes.conversor_id(id='38222-1', id_in='planner', id_out='britech')
