from grau_project.grau_email.grau_leitor_email import grau_leitor_email

email = grau_leitor_email()
anexo = ['pesc','PESC', 'Pesc', 'negs', 'papt', 'PAPT', 'Papt', 'PROD','Prod','prod','.xml']
#print grau_leitor_email.download_all_attachemnts(dir_path='/usr/lib/python2.7/dist-packages/grau_project/grau_middleoffice/temp/', dir_name='attachments', str_contains_anexo=anexo)
print grau_leitor_email.download_all_attachemnts(dir_path='/home/servidor/Documents/', dir_name='attachments', str_contains_anexo=anexo)
