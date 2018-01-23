# encoding: 'latin-1'
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
import imaplib

def destinatarios(tipo='operacoes'):
    if tipo == 'operacoes':
        destinatarios = ['rafae@graugestao.com.br', 'utcho@graugestao.com.br', 'maria@graugestao.com.br','diogo@graugestao.com.br', 'moises@graugestao.com.br', 'kaio@graugestao.com.br']
    elif tipo == 'teste':
        destinatarios = ['rafael@graugestao.com.br', 'moises@graugestao.com.br', 'maria@graugestao.com.br']

    return destinatarios


def envio_email_anexo(para, de='rafael.chow@graugestao.com.br', senha='007J@mes',  assunto='', corpo_mensagem='', anexo='', nome_anexo=''):

    email_digital = de
    email_password = senha
    email_dest = para

    msg = MIMEMultipart()
    msg['From'] = email_digital
    msg['To'] = email_dest
    msg['Subject'] = assunto

    body = corpo_mensagem + signature()


    if anexo != '':
        msg.attach(MIMEText(body,'html'))
        filename = anexo
        attachment = open(filename,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= " + nome_anexo)
        msg.attach(part)

    else:
        msg.attach(MIMEText(body,'html'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email_digital, email_password)
    server.sendmail(email_digital, email_dest, msg.as_string())
    server.close()

    return 'Email enviado com sucesso.'

def signature():
    signature = """
    <html xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office"
    xmlns:w="urn:schemas-microsoft-com:office:word"
    xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
    xmlns="http://www.w3.org/TR/REC-html40">

    <head>
    <meta http-equiv=Content-Type content="text/html; charset=windows-1252">
    <meta name=ProgId content=Word.Document>
    <meta name=Generator content="Microsoft Word 15">
    <meta name=Originator content="Microsoft Word 15">
    <link rel=File-List href="Signature_files/filelist.xml">
    <link rel=Edit-Time-Data href="Signature_files/editdata.mso">
    <!--[if !mso]>
    <style>
    v\:* {behavior:url(#default#VML);}
    o\:* {behavior:url(#default#VML);}
    w\:* {behavior:url(#default#VML);}
    .shape {behavior:url(#default#VML);}
    </style>
    <![endif]--><!--[if gte mso 9]><xml>
     <o:DocumentProperties>
      <o:Template>NormalEmail.dotm</o:Template>
      <o:Revision>0</o:Revision>
      <o:TotalTime>1</o:TotalTime>
      <o:Pages>1</o:Pages>
      <o:Words>68</o:Words>
      <o:Characters>370</o:Characters>
      <o:Company>Microsoft</o:Company>
      <o:Lines>3</o:Lines>
      <o:Paragraphs>1</o:Paragraphs>
      <o:CharactersWithSpaces>437</o:CharactersWithSpaces>
      <o:Version>15.00</o:Version>
     </o:DocumentProperties>
     <o:OfficeDocumentSettings>
      <o:AllowPNG/>
     </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <link rel=themeData href="Signature_files/themedata.thmx">
    <link rel=colorSchemeMapping href="Signature_files/colorschememapping.xml">
    <!--[if gte mso 9]><xml>
     <w:WordDocument>
      <w:View>Normal</w:View>
      <w:Zoom>0</w:Zoom>
      <w:TrackMoves/>
      <w:TrackFormatting/>
      <w:HyphenationZone>21</w:HyphenationZone>
      <w:PunctuationKerning/>
      <w:ValidateAgainstSchemas/>
      <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
      <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
      <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
      <w:DoNotPromoteQF/>
      <w:LidThemeOther>PT-BR</w:LidThemeOther>
      <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
      <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
      <w:DoNotShadeFormData/>
      <w:Compatibility>
       <w:BreakWrappedTables/>
       <w:SnapToGridInCell/>
       <w:WrapTextWithPunct/>
       <w:UseAsianBreakRules/>
       <w:DontGrowAutofit/>
       <w:SplitPgBreakAndParaMark/>
       <w:EnableOpenTypeKerning/>
       <w:DontFlipMirrorIndents/>
       <w:OverrideTableStyleHps/>
       <w:UseFELayout/>
      </w:Compatibility>
      <m:mathPr>
       <m:mathFont m:val="Cambria Math"/>
       <m:brkBin m:val="before"/>
       <m:brkBinSub m:val="&#45;-"/>
       <m:smallFrac m:val="off"/>
       <m:dispDef/>
       <m:lMargin m:val="0"/>
       <m:rMargin m:val="0"/>
       <m:defJc m:val="centerGroup"/>
       <m:wrapIndent m:val="1440"/>
       <m:intLim m:val="subSup"/>
       <m:naryLim m:val="undOvr"/>
      </m:mathPr></w:WordDocument>
    </xml><![endif]--><!--[if gte mso 9]><xml>
     <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
      DefSemiHidden="false" DefQFormat="false" DefPriority="99"
      LatentStyleCount="371">
      <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
      <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
      <w:LsdException Locked="false" Priority="9" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 6"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 7"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 8"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index 9"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 1"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 2"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 3"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 4"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 5"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 6"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 7"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 8"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" Name="toc 9"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Normal Indent"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="footnote text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="annotation text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="header"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="footer"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="index heading"/>
      <w:LsdException Locked="false" Priority="35" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="caption"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="table of figures"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="envelope address"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="envelope return"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="footnote reference"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="annotation reference"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="line number"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="page number"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="endnote reference"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="endnote text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="table of authorities"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="macro"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="toa heading"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Bullet"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Number"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Bullet 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Bullet 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Bullet 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Bullet 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Number 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Number 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Number 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Number 5"/>
      <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Closing"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Signature"/>
      <w:LsdException Locked="false" Priority="1" SemiHidden="true"
       UnhideWhenUsed="true" Name="Default Paragraph Font"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text Indent"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Continue"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Continue 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Continue 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Continue 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="List Continue 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Message Header"/>
      <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Salutation"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Date"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text First Indent"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text First Indent 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Note Heading"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text Indent 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Body Text Indent 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Block Text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Hyperlink"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="FollowedHyperlink"/>
      <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
      <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Document Map"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Plain Text"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="E-mail Signature"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Top of Form"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Bottom of Form"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Normal (Web)"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Acronym"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Address"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Cite"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Code"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Definition"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Keyboard"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Preformatted"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Sample"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Typewriter"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="HTML Variable"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Normal Table"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="annotation subject"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="No List"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Outline List 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Outline List 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Outline List 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Simple 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Simple 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Simple 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Classic 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Classic 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Classic 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Classic 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Colorful 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Colorful 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Colorful 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Columns 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Columns 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Columns 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Columns 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Columns 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 6"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 7"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Grid 8"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 4"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 5"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 6"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 7"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table List 8"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table 3D effects 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table 3D effects 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table 3D effects 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Contemporary"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Elegant"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Professional"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Subtle 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Subtle 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Web 1"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Web 2"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Web 3"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Balloon Text"/>
      <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
      <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
       Name="Table Theme"/>
      <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
      <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
      <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
      <w:LsdException Locked="false" Priority="34" QFormat="true"
       Name="List Paragraph"/>
      <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
      <w:LsdException Locked="false" Priority="30" QFormat="true"
       Name="Intense Quote"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
      <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
      <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
      <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
      <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
      <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
      <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
      <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
      <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
      <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
      <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
      <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
      <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
      <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
      <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
      <w:LsdException Locked="false" Priority="19" QFormat="true"
       Name="Subtle Emphasis"/>
      <w:LsdException Locked="false" Priority="21" QFormat="true"
       Name="Intense Emphasis"/>
      <w:LsdException Locked="false" Priority="31" QFormat="true"
       Name="Subtle Reference"/>
      <w:LsdException Locked="false" Priority="32" QFormat="true"
       Name="Intense Reference"/>
      <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
      <w:LsdException Locked="false" Priority="37" SemiHidden="true"
       UnhideWhenUsed="true" Name="Bibliography"/>
      <w:LsdException Locked="false" Priority="39" SemiHidden="true"
       UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
      <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
      <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
      <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
      <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
      <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
      <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
      <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
      <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
      <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 1"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 1"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 1"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 2"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 2"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 2"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 3"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 3"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 3"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 4"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 4"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 4"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 5"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 5"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 5"/>
      <w:LsdException Locked="false" Priority="46"
       Name="Grid Table 1 Light Accent 6"/>
      <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
      <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
      <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
      <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
      <w:LsdException Locked="false" Priority="51"
       Name="Grid Table 6 Colorful Accent 6"/>
      <w:LsdException Locked="false" Priority="52"
       Name="Grid Table 7 Colorful Accent 6"/>
      <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
      <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
      <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 1"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 1"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 1"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 2"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 2"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 2"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 3"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 3"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 3"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 4"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 4"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 4"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 5"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 5"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 5"/>
      <w:LsdException Locked="false" Priority="46"
       Name="List Table 1 Light Accent 6"/>
      <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
      <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
      <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
      <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
      <w:LsdException Locked="false" Priority="51"
       Name="List Table 6 Colorful Accent 6"/>
      <w:LsdException Locked="false" Priority="52"
       Name="List Table 7 Colorful Accent 6"/>
     </w:LatentStyles>
    </xml><![endif]-->
    <style>
    <!--
     /* Font Definitions */
     @font-face
    	{font-family:Calibri;
    	panose-1:2 15 5 2 2 2 4 3 2 4;
    	mso-font-charset:0;
    	mso-generic-font-family:swiss;
    	mso-font-pitch:variable;
    	mso-font-signature:-536859905 -1073732485 9 0 511 0;}
    @font-face
    	{font-family:Verdana;
    	panose-1:2 11 6 4 3 5 4 4 2 4;
    	mso-font-charset:0;
    	mso-generic-font-family:swiss;
    	mso-font-pitch:variable;
    	mso-font-signature:-1593833729 1073750107 16 0 415 0;}
     /* Style Definitions */
     p.MsoNormal, li.MsoNormal, div.MsoNormal
    	{mso-style-unhide:no;
    	mso-style-qformat:yes;
    	mso-style-parent:"";
    	margin:0cm;
    	margin-bottom:.0001pt;
    	mso-pagination:widow-orphan;
    	font-size:11.0pt;
    	font-family:"Calibri","sans-serif";
    	mso-ascii-font-family:Calibri;
    	mso-ascii-theme-font:minor-latin;
    	mso-fareast-font-family:"Times New Roman";
    	mso-fareast-theme-font:minor-fareast;
    	mso-hansi-font-family:Calibri;
    	mso-hansi-theme-font:minor-latin;
    	mso-bidi-font-family:"Times New Roman";
    	mso-bidi-theme-font:minor-bidi;}
    a:link, span.MsoHyperlink
    	{mso-style-noshow:yes;
    	mso-style-priority:99;
    	mso-style-parent:"";
    	color:blue;
    	text-decoration:underline;
    	text-underline:single;}
    a:visited, span.MsoHyperlinkFollowed
    	{mso-style-noshow:yes;
    	mso-style-priority:99;
    	color:#954F72;
    	mso-themecolor:followedhyperlink;
    	text-decoration:underline;
    	text-underline:single;}
    p.MsoAutoSig, li.MsoAutoSig, div.MsoAutoSig
    	{mso-style-priority:99;
    	mso-style-link:"E-mail Signature Char";
    	margin:0cm;
    	margin-bottom:.0001pt;
    	mso-pagination:widow-orphan;
    	font-size:11.0pt;
    	font-family:"Calibri","sans-serif";
    	mso-ascii-font-family:Calibri;
    	mso-ascii-theme-font:minor-latin;
    	mso-fareast-font-family:"Times New Roman";
    	mso-fareast-theme-font:minor-fareast;
    	mso-hansi-font-family:Calibri;
    	mso-hansi-theme-font:minor-latin;
    	mso-bidi-font-family:"Times New Roman";
    	mso-bidi-theme-font:minor-bidi;}
    span.E-mailSignatureChar
    	{mso-style-name:"E-mail Signature Char";
    	mso-style-priority:99;
    	mso-style-unhide:no;
    	mso-style-locked:yes;
    	mso-style-link:"E-mail Signature";}
    .MsoChpDefault
    	{mso-style-type:export-only;
    	mso-default-props:yes;
    	font-size:11.0pt;
    	mso-ansi-font-size:11.0pt;
    	mso-bidi-font-size:11.0pt;
    	mso-ascii-font-family:Calibri;
    	mso-ascii-theme-font:minor-latin;
    	mso-fareast-font-family:"Times New Roman";
    	mso-fareast-theme-font:minor-fareast;
    	mso-hansi-font-family:Calibri;
    	mso-hansi-theme-font:minor-latin;
    	mso-bidi-font-family:"Times New Roman";
    	mso-bidi-theme-font:minor-bidi;}
    @page WordSection1
    	{size:612.0pt 792.0pt;
    	margin:70.85pt 3.0cm 70.85pt 3.0cm;
    	mso-header-margin:36.0pt;
    	mso-footer-margin:36.0pt;
    	mso-paper-source:0;}
    div.WordSection1
    	{page:WordSection1;}
    -->
    </style>
    <!--[if gte mso 10]>
    <style>
     /* Style Definitions */
     table.MsoNormalTable
    	{mso-style-name:"Table Normal";
    	mso-tstyle-rowband-size:0;
    	mso-tstyle-colband-size:0;
    	mso-style-noshow:yes;
    	mso-style-priority:99;
    	mso-style-parent:"";
    	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
    	mso-para-margin:0cm;
    	mso-para-margin-bottom:.0001pt;
    	mso-pagination:widow-orphan;
    	font-size:11.0pt;
    	font-family:"Calibri","sans-serif";
    	mso-ascii-font-family:Calibri;
    	mso-ascii-theme-font:minor-latin;
    	mso-hansi-font-family:Calibri;
    	mso-hansi-theme-font:minor-latin;
    	mso-bidi-font-family:"Times New Roman";
    	mso-bidi-theme-font:minor-bidi;}
    table.Tabelanormal
    	{mso-style-name:"Tabela normal";
    	mso-tstyle-rowband-size:0;
    	mso-tstyle-colband-size:0;
    	mso-style-noshow:yes;
    	mso-style-priority:99;
    	mso-style-unhide:no;
    	mso-style-parent:"";
    	mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
    	mso-para-margin:0cm;
    	mso-para-margin-bottom:.0001pt;
    	mso-pagination:widow-orphan;
    	font-size:11.0pt;
    	font-family:"Calibri","sans-serif";
    	mso-ascii-font-family:Calibri;
    	mso-ascii-theme-font:minor-latin;
    	mso-fareast-font-family:"Times New Roman";
    	mso-hansi-font-family:Calibri;
    	mso-hansi-theme-font:minor-latin;}
    </style>
    <![endif]-->
    </head>

    <body lang=PT-BR link=blue vlink="#954F72" style='tab-interval:35.4pt'>

    <div class=WordSection1>

    <table class=Tabelanormal border=0 cellspacing=0 cellpadding=0 width=559
     style='width:419.2pt;margin-left:5.4pt;border-collapse:collapse;mso-yfti-tbllook:
     1184;mso-padding-alt:0cm 0cm 0cm 0cm'>
     <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
      <td width=279 valign=top style='width:209.6pt;border:solid white 1.0pt;
      border-left:none;padding:0cm 0cm 0cm 0cm'>
      <p class=MsoNormal><span style='mso-fareast-font-family:"Times New Roman";
      mso-bidi-font-family:Calibri'><img width=300 height=101 id="_x0000_i1025"
      src="http://lw135550052750cb4418.hospedagemdesites.ws/grau/wp-content/uploads/2013/01/graulogoatualhorizontal.jpg"
      alt="logo grau" u5:shapes="_x0000_i1025" border=0><o:p></o:p></span></p>
      </td>
      <u6:p></u6:p>
      <td width=279 valign=bottom style='width:209.6pt;border:solid white 1.0pt;
      border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
      <p class=MsoNormal><b><span style='font-size:10.0pt;font-family:"Verdana","sans-serif";
      mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri;
      color:#365F91'>Rafael Chow</span></b><span style='Roman";mso-bidi-theme-font:minor-bidi;
                        color:#365F91'><u6:p></u6:p></span><span
      style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
      <p class=MsoNormal><u><span style='font-size:10.0pt;mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'><a
      href="mailto:rafael.chow@graugestao.com.br">rafael.chow@graugestao.com.br</a> <u6:p></u6:p></span></u><span
      style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
      <p class=MsoNormal><u><span style='font-size:10.0pt;mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'><a
      href="http://www.graugestao.com.br/">www.graugestao.com.br</a></span></u><span
      style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri'><u6:p></u6:p><o:p></o:p></span></p>
      <p class=MsoNormal><span style='font-size:10.0pt;mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'>Av. Presidente Juscelino
      Kubistchek,1400 - 2&ordm; andar conj.22</span><span style='mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'><u6:p></u6:p><o:p></o:p></span></p>
      <p class=MsoNormal><span style='font-size:10.0pt;mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'>S&atilde;o Paulo - SP - 04543-000</span><span
      style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri'><u6:p></u6:p><o:p></o:p></span></p>
      <p class=MsoNormal><span style='font-size:10.0pt;mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'>Tel:&nbsp;<span
      style='color:#365F91'>+55 (11) 3845-4370</span></span><span
      style='mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri'><u6:p></u6:p><o:p></o:p></span></p>
      <p class=MsoNormal><span style='font-size:5.0pt;font-family:"Verdana","sans-serif";
      mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri;
      color:#365F91'><u6:p>&nbsp;</u6:p></span><span style='mso-fareast-font-family:
      "Times New Roman";mso-bidi-font-family:Calibri'><o:p></o:p></span></p>
      <p class=MsoNormal><span style='font-size:5.0pt;font-family:"Verdana","sans-serif";
      mso-fareast-font-family:"Times New Roman";mso-bidi-font-family:Calibri;
      color:#365F91'>&nbsp;</span><span style='mso-fareast-font-family:"Times New Roman";
      mso-bidi-font-family:Calibri'><u6:p></u6:p><o:p></o:p></span></p>
      </td>
     </tr>
    </table>

    <p class=MsoAutoSig><o:p>&nbsp;</o:p></p>

    <p class=MsoAutoSig><o:p>&nbsp;</o:p></p>

    </div>

    </body>

    </html>
    """
    return signature
