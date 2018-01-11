import pandas as pd
from grau_project.grau_agente_fiduciario_site.agente_fiduciario_site import grau_agente_fiduciario_site
from grau_project.grau_britech_site.grau_britech_site import grau_britech_site


class grau_backoffice:
    def __init__(self, debenture=''):
        self.britech_site = grau_britech_site()
        if debenture != '':
            self.agente_fiduciario_site = agente_fiduciario_site(debenture)

    #def importacao_pu_debentures(self):




if __name__=='__main__':
    grau_backoffice = grau_backoffice()
    print grau_backoffice.importacao_pu_debentures('MTEL15')
    site = grau_agente_fiduciario_site('MTEL15')
    df_debenture = site.pu_debenture(return_float=True)
