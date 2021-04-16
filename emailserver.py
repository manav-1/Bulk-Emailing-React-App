import smtplib
import ssl
import mimetypes
import numpy as np
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from tkinter import *
import tkinter as tk
import six
import os.path
import tkinter.scrolledtext as scrolledtext
from pyfiglet import figlet_format
from email.mime.application import MIMEApplication
from tkinter import filedialog
import flask
from flask_cors import CORS
import json
from flask.json import jsonify
from flask import request
from werkzeug.utils import secure_filename
try:
    from termcolor import colored
except ImportError:
    colored = None

login_details = dict()
to_emails = np.zeros(3)
details = dict()


styletagsfinal = """<style>
        @media only screen and (min-width: 768px){
            .main{
                width: 50%;
            }
            .header{
                width:100%;
            }
            .inside{
                width:100%;
            }
            img{
                width:100%
            }
            .left{
                margin-left:15px;
                width:145px;
                float:right;
            }
            .text{
                font-family: nunito;
                font-size:18.5px;
                text-align:justify;
            }
        }
        @media only screen and (max-width: 768px){
            .main{
            width: 100%;
            }
            .header{
            width:100%;
            }
            .inside{
            width:100%;
            }
            img{
            width:100%
            }
            .left{
            margin-left:10px;
            width:80px;
            float:right;
            }
            .text{
            font-family: nunito;
            font-size:15px;
            text-align:justify;
            }
        }
    </style>"""

bodytagsfinal = """<body>
    <div class="main">
        <img class="header" src="https://i.ibb.co/WG52VhC/recruiters.jpg" alt="Document">

        <div class='inside'>
            <div class="left">
                <img src="https://i.ibb.co/SXkjZVJ/image-2.png
https://i.ibb.co/WW7gQZS/image-3.png" alt="Image">
                <img src="https://i.ibb.co/WW7gQZS/image-3.png" alt="Image">
            </div>

            <p class='text'> Dear Manager<br>
                Greeting from <strong>Start@KMV</strong>,
                The Placement Cell Of <strong>Keshav Mahavidyalaya, University of Delhi</strong><br><br>

                We would like to inform you about the <strong>commencement
                of the Placement Season</strong> for the session 2020-21.<br><br> The
                Students of Keshav Mahavidyalaya are a diverse group of
                exceptional individuals interested in a variety of
                opportunities. Our students have been placed in
                prestigious companies like AT Kearney, EY, TresVista,
                Deloitte, ZS, Infosys, S&P Global & Gartner among others.<br><br>

                We wish to set new records this season and thus <strong>invite
                your esteemed organization</strong> for placement and internship
                opportunities. In the light of the current situation, we are
                also open to Virtual hiring drives.<br>
                <strong>PFA</strong> : Placement Brochure<br><br>

                For further information, contact-<br>
                Pranjal Kukreja - 9711376316<br>
                Riya Himmatramka - 9289997915<br>

                Thank You<br>
                Regards<br>
                Start@KMV<br>
                The Placement Cell<br>
                Keshav Mahavidyalaya<br>
                University of Delhi</p>
        </div>
    </div>

</body>
"""


def emails_to_be_sent(snum, enum, mailaddr, sheetlink, subject):
    global login_details
    try:
        database = pd.read_csv(sheetlink)
        try:
            snum = int(snum)
            enum = int(enum)
            database = database.iloc[snum-1:enum, ::]
        #                starting: ending , 169, 200
            database["Name"] = database["Name"].fillna(
                "Sir/Ma'am")  # "" --> hiring manager
            details = dict(zip(database["Email"], database["Name"]))
            to_emails = database["Email"].values
            login_details = {'smtp_server': 'smtp.gmail.com', 'smtp_protocol': 'tls',
                             'example_no': '3', 'from_email': mailaddr, 'to_email': to_emails, 'subject': subject}

        except:
            return False
    except:
        return False
    return (login_details, details)


def get_html_message(from_email, to_email, subject, detailinfo, style, body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    # Plain-text version of content
    plain_text = """\

        Greetings from Start@KMV, The Placement Cell of Keshav
        Mahavidyalaya, University of Delhi.

        To continue on the path of providing novel opportunities to the
        students, we are organizing the second edition of the Virtual
        Internship Fair on February 28, 2021.

        Last year’s fair was an extreme success with 30+ esteemed
        organizations offering a plethora of opportunities across diverse fields
        and witnessed more than a combined 6000+ student applications.

        The aim of the event is to bring employers from a variety of industries
        — Start-ups, MNCs and Social Organisations — hiring for various
        roles of internship and apprenticeship positions. In the past,
        companies such as Sharekhan, Zomato Feeding India, Sanguine
        Capital, Vivo, The MoneyRoller, Grant Thornton, Deloitte, NITI Aayog,
        Wipro and many more have participated and selected students for
        internships.

        We wish to invite your esteemed organisation for the same and look
        forward to a mutually beneficial relationship with your organisation.

        PFA: Brochure

        For further information, contact -
        Pranjal Kukreja - 9711376316
        Riya Himmatramka - 9289997915

        Thank You
        Regards
        Start@KMV
        The Placement Cell
        Keshav Mahavidyalaya
        University of Delhi
    """
    # html version of content
    html_content = """\
    <!DOCTYPE html>
        <html lang="en">
            <head>
                styletags
                <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
                jQuery library-->
                <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> -->

                <!--Latest compiled and minified JavaScript-->
                <!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> -->


                <meta charset="UTF-8">
                <!-- <link rel="stylesheet" href="css/bootstrap.css"> -->
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            bodytags
        </html>

    """
    html_content = html_content.replace("styletags", style, 1)
    html_content = html_content.replace("bodytags", body, 1)
    html_content = html_content.replace("Manager", detailinfo[to_email])
    text_part = MIMEText(plain_text, 'plain')
    html_part = MIMEText(html_content, 'html')
    msg.add_header('Content-Type', 'text/html')
    msg.attach(text_part)
    msg.attach(html_part)
    return msg


def get_attachment_message(from_email, to_email, subject, detailinfo, style, body, filename):
    msg = get_html_message(from_email, to_email, subject,
                           detailinfo, style, body)
    
    file_path = filename
    ctype, encoding = mimetypes.guess_type(file_path)
    maintype, subtype = ctype.split('/', 1)
    pdf = MIMEApplication(open(file_path, 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename=os.path.splitext(
        filename)[0].split("/")[-1] + os.path.splitext(filename)[1])
    msg.attach(pdf)
    return msg


def send_email(email_info, detailinfo, style, body, filename, server):
    example_no = email_info.get('example_no', '')
    from_email = email_info.get('from_email', '')
    to_email = email_info.get('to_email', '')
    subject = email_info.get('subject', '')

    try:
        if filename == '':
            for x in to_email:
                msg = get_html_message(
                    from_email, x, subject, detailinfo, style, body)
                server.send_message(msg)
            return True
            
        else:
            for x in to_email:
                msg = get_attachment_message(
                    from_email, x, subject, detailinfo, style, body, filename)
                server.send_message(msg)
            return True
    finally:
        server.quit()


def sendMails(email, password, subject, link, eno, sno, filename):
    smtp_server = 'smtp.gmail.com'
    protocol = 'tls'
    context = ssl.create_default_context()
    try:
        if protocol == 'ssl':
            port = 465
            server = smtplib.SMTP_SSL(smtp_server, port, context=context)
            server.login(email, password)
        elif protocol == 'tls':
            port = 587
            server = smtplib.SMTP(smtp_server, port)
            server.starttls(context=context)
            server.login(email, password)
    except Exception as e:
           print(e)
           return "email"
    x = main(sno, eno, email, password, link, subject,styletagsfinal,bodytagsfinal,filename,server )
    return x


def main(start, end, mailaddr, passwd, sheetlink, subject, style, body, filename, server):
    loginreturn = emails_to_be_sent(start, end, mailaddr, sheetlink, subject)
    if(loginreturn):
        email_info, detailinfo = loginreturn
        val = send_email(email_info, detailinfo, style, body, filename, server)
        if(val):
            return True
        else:
            return "error"
    else:
        return "link"




app = flask.Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'uploads')
CORS(app)
@app.route('/api', methods=['GET', 'POST'])
def email():
    if flask.request.method == 'POST':
        print("Received a req")
        email = request.form.get('email')
        password = request.form.get('password')
        subject = request.form.get('subject')
        link = request.form.get('link')
        eno = request.form.get('eno')
        sno = request.form.get('sno')
        file = request.files['file']
        file.save(os.path.join(uploads_dir, secure_filename(file.filename)))
        x = sendMails(email, password, subject, link, eno, sno, ".//instance//uploads//"+file.filename)
        if(x  == "email"):
            return "cred"
        elif( x =="link"):
            return "link"
        elif( x =="error"):
            return "error"
        else:
            return "Done"


app.run(host="127.0.0.1", port=5000, debug=True)




