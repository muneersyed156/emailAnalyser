import smtplib
import imaplib
import email
import time


def read_emails():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        g = "*****@gmail.com"
        p = "*******"
        mail.login(g, p)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0];d = {};dm={}
        id_list = mail_ids.split()   
        
        for i in reversed(id_list[:]):
            typ, data = mail.fetch(i, '(RFC822)')
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            msg = email.message_from_string(raw_email_string)
            mail_part = msg["from"].split(" ")[-1]
            category_part = (mail_part.split("@")[-1]).split(".")[0]
            if(category_part not in d.keys()):
                d[category_part] = 1
                dm[category_part]=msg['from']
            else:
                d[category_part] += 1
        print(d,dm)

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    read_emails()
