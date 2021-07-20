
import imaplib
import email




def read_emails():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        g = ""
        p = ""
        mail.login(g, p)
        mail.select('inbox')
        type, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0]
        m = []
        id_list = mail_ids.split()
        delete = "try.avoid.mails@gmail.com"
        print(id_list)
        typ, data = mail.fetch(id_list[0], '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        msg = email.message_from_string(raw_email_string)
        mail_part = msg["from"].split(" ")[-1]
        mail_part = mail_part[1:len(mail_part) - 1]
        m.append(mail_part)
        print(m)
        if (delete == m[0]):
            print("found")
            mail.store(id_list[0], '+X-GM-LABELS', '\\Trash')
            mail.expunge()
            print("Done!")
        else:
            print("not found")
    except Exception as e:
        pass




if __name__=="__main__":
    while(1):
        read_emails()
