import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email import Encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email import message_from_string
from dateutil import parser
from grau_project.grau_datas import grau_datas

import getpass
import imaplib
import sys
import os
import email.utils
import time
import datetime

class grau_leitor_email:
    @staticmethod
    def leitor_email():
        email = 'rafael.chow@graugestao.com.br'
        password    = "007J@mes"
        smtp_server = "imap.gmail.com"
        smtp_port   = 993

        mail = imaplib.IMAP4_SSL(smtp_server)
        mail.login(email,password)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
                typ, data = mail.fetch(i, '(RFC822)' )
                #typ, data = mail.uid('search', None, 'HEADER Subject "C/C CARTEIRAS"' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = message_from_string(response_part[1])

                        #print msg
                        email_subject = msg['subject'].decode('utf-8')
                        email_from = msg['from']
                        email_att = msg['attachment']

                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n'

                        if email_att == None:
                            pass
                        else:
                            print 'Attachment : ' + email_att + '\n'

                    '''
                    if isinstance(response_part, tuple):
                        #print data
                        print response_part.find('')
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n'

                    '''


    @staticmethod
    def download_all_attachemnts(dir_path='', dir_name='attachments',str_contains_anexo='', str_contains_assunto=''):
        detach_dir = dir_path

        monthDict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

        if dir_name not in os.listdir(detach_dir):
            os.mkdir('attachments')

        userName = 'rafael.chow@graugestao.com.br'
        passwd = '007J@mes'

        try:
            imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
            typ, accountDetails = imapSession.login(userName, passwd)
            if typ != 'OK':
                print 'Not able to sign in!'
                raise

            #imapSession.select('[Gmail]/All Mail')
            imapSession.select('inbox')
            typ, data = imapSession.search(None, 'ALL')
            if typ != 'OK':
                print 'Error searching Inbox.'
                raise

            mailId =[]
            messagePartsId = []

            # Iterating over all emails
            for msgId in reversed(data[0].split()):
                if len(mailId) <= 100:
                    typ, messageParts = imapSession.fetch(msgId , '(RFC822)')
                    messagePartsId = messagePartsId + [messageParts]
                    mailId  = mailId + [msgId]



                    if typ != 'OK':
                        print 'Error fetching mail.'
                        raise

            email_dictionary = dict(zip(mailId, messagePartsId))

            for i in mailId[::-1]:
                emailBody = email_dictionary[i][0][1]
                mail = message_from_string(emailBody)
                print 'ID', i
                date = mail['date']
                parsed_date = parser.parse(date)

                data = str(parsed_date)[0:19].replace(' ','_')
                data = grau_datas.parse_date(data)
                print data


                subject = mail['subject'].decode('iso-8859-1')
                print subject
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    fileName = part.get_filename()
                    if bool(fileName):
                        try:
                            if str_contains_anexo != '':
                                if isinstance(str_contains_anexo, list):
                                    for str_cont in str_contains_anexo:
                                        if str_cont in fileName:

                                            fileName = data + '_' + fileName

                                            filePath = os.path.join(detach_dir, 'attachments', fileName)

                                            if not os.path.isfile(filePath):
                                                fp = open(filePath, 'wb')
                                                fp.write(part.get_payload(decode=True))
                                                fp.close()

                            elif str_contains_assunto != '':
                                if isinstance(str_contains_assunto, list):
                                    for subj in str_contains_assunto:
                                        if subj in subject:
                                            fileName = data + '_' + fileName

                                            filePath = os.path.join(detach_dir, 'attachments', fileName)

                                            if not os.path.isfile(filePath):
                                                fp = open(filePath, 'wb')
                                                fp.write(part.get_payload(decode=True))
                                                fp.close()

                            elif str_contains_assunto != '' and str_contains_anexo != '':
                                for str_cont in str_contains_anexo:
                                    for subj in str_contains_assunto:
                                        if (subj in subject):
                                            if (str_cont in fileName):
                                                print subj
                                                fileName = data + '_' + fileName

                                                filePath = os.path.join(detach_dir, 'attachments', fileName)

                                                if not os.path.isfile(filePath):
                                                    fp = open(filePath, 'wb')
                                                    fp.write(part.get_payload(decode=True))
                                                    fp.close()
                        except Exception as e:
                            print e

            imapSession.close()
            imapSession.logout()

        except Exception, e:
            print e


    @staticmethod
    def download_teste(dir_path='', dir_name='attachments',str_contains_anexo='', str_contains_assunto=''):
        detach_dir = dir_path

        monthDict = {'Jan':'1', 'Feb':'2', 'Mar':'3', 'Apr':'4', 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

        if dir_name not in os.listdir(detach_dir):
            os.mkdir('attachments')

        userName = 'rafael.chow@graugestao.com.br'
        passwd = '007J@mes'

        try:
            imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
            typ, accountDetails = imapSession.login(userName, passwd)
            if typ != 'OK':
                print 'Not able to sign in!'
                raise

            #imapSession.select('[Gmail]/All Mail')
            imapSession.select('inbox')
            typ, data = imapSession.search(None, 'ALL')
            if typ != 'OK':
                print 'Error searching Inbox.'
                raise

            mailId =[]
            messagePartsId = []
            # Iterating over all emails
            data = data[0].split()
            for msgId in data[len(data)-50:len(data):-1]:
                    typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
                    messagePartsId = messagePartsId + [messageParts]
                    mailId  = mailId + [msgId]

                    print mailId
                    if typ != 'OK':
                        print 'Error fetching mail.'
                        raise

            email_dictionary = dict(zip(mailId, messagePartsId))

            for i in mailId[::-1]:
                emailBody = email_dictionary[i][0][1]
                mail = message_from_string(emailBody)
                print 'ID', i
                date = mail['date']
                date = date.split(' ')
                data =  date[3] + '-' + monthDict[date[2]] + '-' + date[1] + '_' +  date[4]
                subject = mail['subject'].decode('iso-8859-1')
                print subject
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue

                    fileName = part.get_filename()
                    if bool(fileName):
                        try:
                            if str_contains_anexo != '':
                                if isinstance(str_contains_anexo, list):
                                    for str_cont in str_contains_anexo:
                                        if str_cont in fileName:

                                            fileName = data + '_' + fileName

                                            filePath = os.path.join(detach_dir, 'attachments', fileName)

                                            if not os.path.isfile(filePath):
                                                fp = open(filePath, 'wb')
                                                fp.write(part.get_payload(decode=True))
                                                fp.close()

                            elif str_contains_assunto != '':
                                if isinstance(str_contains_assunto, list):
                                    for subj in str_contains_assunto:
                                        if subj in subject:
                                            fileName = data + '_' + fileName

                                            filePath = os.path.join(detach_dir, 'attachments', fileName)

                                            if not os.path.isfile(filePath):
                                                fp = open(filePath, 'wb')
                                                fp.write(part.get_payload(decode=True))
                                                fp.close()

                            elif str_contains_assunto != '' and str_contains_anexo != '':
                                for str_cont in str_contains_anexo:
                                    for subj in str_contains_assunto:
                                        if (subj in subject):
                                            if (str_cont in fileName):
                                                print subj
                                                fileName = data + '_' + fileName

                                                filePath = os.path.join(detach_dir, 'attachments', fileName)

                                                if not os.path.isfile(filePath):
                                                    fp = open(filePath, 'wb')
                                                    fp.write(part.get_payload(decode=True))
                                                    fp.close()
                        except Exception as e:
                            print e

            imapSession.close()
            imapSession.logout()

        except :
            print 'Not able to download all attachments.'


if __name__=='__main__':
    email = grau_leitor_email()


    anexo = ['pesc','PESC', 'Pesc', 'negs', 'papt', 'PAPT', 'Papt', 'PROD','Prod','prod','.xml','.zip','.pdf']
    anexo = ['CMD']
    #assunto = ['[XMLs Fundos]', '[PLANNER]']
    #print grau_leitor_email.download_all_attachemnts(dir_path='/home/servidor/Desktop/', dir_name='attachments', str_contains_assunto=assunto, str_contains_anexo=anexo)
    print grau_leitor_email.download_all_attachemnts(dir_path='/home/felipe/Desktop/', dir_name='attachments', str_contains_anexo=anexo)
# print leitor_email()
# print download_all_attachemnts(str_contains_anexo='pesc')
# print download_all_attachemnts(str_contains_anexo='PESC')
# print download_all_attachemnts(str_contains_anexo='Pesc')
#print download_all_attachemnts(str_contains_anexo='PAPT')
# print download_all_attachemnts(str_contains_anexo='PROD')
