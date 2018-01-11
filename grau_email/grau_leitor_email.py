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
import getpass
import imaplib
import sys
import os
import email.utils
import time
import datetime

def leitor_email():
    email  = 'rafael.chow@graugestao.com.br'
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

def download_all_attachemnts(str_contains_anexo=''):
    detach_dir = '/home/servidor/Desktop/'
    if 'attachments' not in os.listdir(detach_dir):
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

        # Iterating over all emails
        for msgId in data[0].split():
            typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print 'Error fetching mail.'
                raise

            emailBody = messageParts[0][1]
            mail = message_from_string(emailBody)
            print emailBody
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue

                fileName = part.get_filename()

                if bool(fileName):
                    if str_contains_anexo != '':

                        date = mail['date']
                        if str_contains_anexo in fileName:
                            date = email.utils.parsedate(date)
                            print date
                            date = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2])
                            fileName = date + ' _ ' + fileName
                            print fileName
                            filePath = os.path.join(detach_dir, 'attachments', fileName)
                            if not os.path.isfile(filePath) :
                                fp = open(filePath, 'wb')
                                fp.write(part.get_payload(decode=True))
                                fp.close()

                    else:
                        filePath = os.path.join(detach_dir, 'attachments', fileName)
                        if not os.path.isfile(filePath) :
                            print fileName
                            fp = open(filePath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()

        imapSession.close()
        imapSession.logout()
    except :
        print 'Not able to download all attachments.'

# print leitor_email()
print download_all_attachemnts(str_contains_anexo='pesc')
# print download_all_attachemnts(str_contains_anexo='PAPT')
# print download_all_attachemnts(str_contains_anexo='PROD')
