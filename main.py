import os
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])

from bs4 import BeautifulSoup
import requests
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "brosaurus.rex@gmail.com"
sender_password = os.environ.get('EMAIL_PASS')
receiver_email = "braydonmillard@gmail.com"
subject = "New Cats available"
# body = "There are new cats available at the Hamilton SPCA! Click here to unsubscribe"

# dir = os.getcwd()
# os.chdir(dir)

def find_cats():
    print('finding cats...')
    html_text = requests.get(
        'http://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals2.aspx?species=Cat&gender=A&agegroup=All&location=&site=&onhold=N&orderby=ID&colnum=3&css=&authkey=ps0gapjsjok4y3tc5lwfkppd483o0jnlylxlenfy8d5l271x11&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=').text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')

    cats = soup.find_all('div', class_ = 'list-animal-name')
    # cats = soup.find_all('a')

    # cat_name = cats.find('a')
    # cat_name_sanitized = cat_name[:-4]
    cat_names = []

    for cat in cats:
        cat_names.append(cat.contents[0])
        # print(cat.contents[0])
    
    # for cat_name in cat_names:
    #     print(cat_name.contents[0])

    for cat_name in cat_names:
        with open(r"C:\Code\PetFinder\PetFinder\seenCats.txt", "r+") as f:
            if not cat_name.contents[0].text in f.read():
                print(cat_name.contents[0].text + ' is a new cat')
                body = '''
                <html>
                    <body>
                        <p>'There is a new cat available at the Hamilton SPCA named " + cat_name.contents[0].text + ". <a href="http://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals2.aspx?species=Cat&gender=A&agegroup=All&location=&site=&onhold=N&orderby=ID&colnum=3&css=&authkey=ps0gapjsjok4y3tc5lwfkppd483o0jnlylxlenfy8d5l271x11&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=">here</a> to view.'</p>
                        <p>Click <a href="https://example.com">here</a> to visit Example.com</p>
                    </body>
                </html>
                '''

                send_email(body)
                # Send an email of new cat to user with link to page
                
                f.write(', ' + cat_name.contents[0].text)




    # print(os.environ.get('EMAIL_PASS'))
def send_email(body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        # Log in to the SMTP server
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
    finally:
        # Close the SMTP server connection
        server.quit()

    # for cat in cats:
    #     with open('seenCats.txt', "r+") as f:
    #         if not cat.text in f.read():
    #             print(cat.text + ' is a new cat')
    #             # Send an email of new cat to user with link to page
                
    #             f.write(', ' + 'hello')


if __name__ == '__main__':
    while True:
        find_cats()
        time.sleep(6000)


'''
for cat in cats:
    if not cat.text in seenCats.txt:
        oldCats.append(cat.text)
        print(cat.text + ' added to old cats')

print(oldCats)
'''

'''
for course in course_cards:
    course_name = course.h5.text
    course_price = course.a
'''
"""
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a
"""
