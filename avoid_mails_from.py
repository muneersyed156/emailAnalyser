import smtplib
import imaplib
import email
import time


def read_emails():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        g = ""
        p = ""
        mail.login(g, p)
        mail.select()
        while(1):
            delete='try.avoid.mails@gmail.com'
            result_status, email_ids = mail.search(None, '(FROM "%s")' %delete)
            email_ids = email_ids[0].split()
            if(len(email_ids)!=0):
                print("%d emails found, sending to trash folder..." % len(email_ids))
                mail.store(email_ids[0], '+X-GM-LABELS', '\\Trash')
                mail.expunge()
                print("Done!")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    read_emails()




#worked for ALL MAILS: mail.store(num, '+X-GM-LABELS', '\\Trash')
#worked for Inbox: mail.store(num, '+FLAG', '\\Deleted')
