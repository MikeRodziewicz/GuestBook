# **Guestbook / Journal** - A simple application that allows people to add
# comments or write journal entries. It give a timestamp to each entry and stores
# it in postrgesSQL.
# Once you make an entry - e-mail confirmation gets send to you with
# all your previous comments.
# Deploy to the live server or setup with LAMP on Raspi.


from datetime import datetime
import backend


if __name__ == "__main__":
    data = datetime.now()
