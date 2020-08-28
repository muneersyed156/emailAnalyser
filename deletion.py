import smtplib
import imaplib
import email
import time


def read_emails():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        g = "maheshsai369@gmail.com"
        p = "9032786272"
        mail.login(g, p)
        mail.select('"[Gmail]/All Mail"')

        delete='adrian@pyimagesearch.com'
        result_status, email_ids = mail.search(None, '(FROM "%s")' %delete)
        email_ids = email_ids[0].split()
        print("%d emails found, sending to trash folder..." % len(email_ids))
        for num in email_ids:
            mail.store(num, '+X-GM-LABELS', '\\Trash')
        mail.expunge()
        print("Done!")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    read_emails()




#worked for ALL MAILS: mail.store(num, '+X-GM-LABELS', '\\Trash')
#worked for Inbox: mail.store(num, '+FLAG', '\\Deleted')
