from grau_project.grau_email.grau_anexo import grau_anexo
from grau_project.grau_middleoffice.papt.grau_papt import grau_papt
from grau_project.grau_middleoffice.prod.grau_prod import grau_prod
from grau_project.grau_middleoffice.pesc.grau_pesc import grau_pesc

if __name__=='__main__':
    grau_papt.loop_grau_papt(dias_retrocedidos=7)
    grau_prod.loop_grau_prod(dias_retrocedidos=7)
    grau_pesc.loop_grau_pesc(dias_retrocedidos=7)