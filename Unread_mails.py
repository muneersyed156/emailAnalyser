import smtplib
import imaplib
import email
import time


def read_emails(gmail,password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        g = gmail
        p = password
        mail.login(g, p)
        mail.select('"[Gmail]/All Mail"')
        result_status, unread = mail.search(None, 'UnSeen')
        unread = unread[0].split()
        print(len(unread))
        #print(mail.list())
        for num in unread:
            mail.store(num, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
        print("Done!")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    gmail=str(input())
    password=str(input())
    read_emails(gmail,password)
