from django.core.mail import send_mail
from celery import shared_task
import requests as rqst
from bs4 import BeautifulSoup
from .models import AuthorName, QuoteName
from datetime import datetime

def add_to_db_autor_and_quote(author , quote):
    add_author = AuthorName.objects.create(name=author.text, time=datetime.now())
    add_author.save()
    add_quote = QuoteName.objects.create(name=quote.text, quote_connect=add_author)
    add_quote.save()
    
def add_to_db_qoute(author, quote):
    db_queryset = AuthorName.objects.filter(name=author.text).first()
    add_quote = QuoteName.objects.create(name=quote.text, quote_connect=db_queryset)
    add_quote.save() 
    
def email_message():
    message = 'at' + str(datetime.now()) + 'process complited'
    send_mail('soup is over',
            message,
            '123rrtyis2@gmail.com', 
            ['goodelita1@gmail.com'], 
            fail_silently=False, 
            auth_user='123rrtyis2@gmail.com', 
            auth_password='hwtmamsvabdnbmue')

@shared_task
def bs_scraping():
    page = 1
    while True:
        request_soup = rqst.get('https://quotes.toscrape.com/page/' + str(page) + '/')
        soup = BeautifulSoup(request_soup.content, features="html.parser")
        if 'No quotes found!' in soup.text:
            print('the last one')
            email_message()
            break
        else:
            quote = soup.find_all('span' , class_='text')
            author = soup.find_all('small', class_='author')
            if len(author) == len(quote):
                for authors , quotes in zip(author, quote):
                    author_name = AuthorName.objects.filter(name=authors.text).first()
                    if author_name is not None and str(authors.text) == author_name.name:
                        add_to_db_qoute(authors, quotes)
                    elif author_name is not None and str(authors.text) != author_name.name:
                        add_to_db_autor_and_quote(authors , quotes)
                    else:
                        add_to_db_autor_and_quote(authors , quotes)
        page+=1
    return 'process succes'