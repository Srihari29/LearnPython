import requests
from bs4 import BeautifulSoup
import smtplib

# URL and headers are important for this script
URL = '<Shopping Site Link>'
# Ask in search engine - what is my user agent - it will give the below result
headers = {"User-Agent": '<User Agent Details>'}

# Function to check Price of a product in amazon
def check_price():
    # This "page" enclosed URL and headers together and get all the data on it
    page = requests.get(URL, headers=headers)

    # This is to bring bs4 in the script to parse the HTML data
    soup = BeautifulSoup(page.content, 'html.parser')

    # This will print all the Source data in that Amazon page
    #print(soup.prettify())
    
    # find and get the title & price out of the page
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    # It will give you first five letters including space
    converted_price = float(price[2:5])

    # Print the name of the item and its rate
    print(title.strip())
    #print(price.strip())
    print(converted_price)
    
    if(converted_price > 150):
        send_mail()

# Function to send email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Add Google App Password after two step authentication has been provided
    server.login('<Email>', '<Password>')
    
    # Add Subject and Body that needs to be sent
    subject = 'Price fell down!'
    body = 'check the Shopping Site link <Shopping Site Link>'
    
    # Add the subject and body to the message that should be sent
    msg = f"Subject: {subject}\n\n{body}"
    
    # Send email from Gmail to Outlook 
    server.sendmail(
        '<From Email>',
        '<To Email>',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    
    # This is used to close the SMTP server connection
    server.quit()
    
check_price()

# Thanks to Dev Ed, I Used it and its working
