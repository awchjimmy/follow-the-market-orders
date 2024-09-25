from helium import *
import time
import json

server = 'https://mt5demo2.ftmo.com/'
login = ''
password = ''

def load_credentials():
    with open('.env', 'r') as fin:
        content = fin.read()
        content = json.loads(content)

        global login
        global password
        login = content['login']
        password = content['password']

def enter_credentials():
    load_credentials()
    wait_until(Button('Connect to account').exists)
    write(login, into='Enter Login')
    write(password, into='Enter Password')
    click('Connect to account')

def click_accept():
    wait_until(Button('Accept').exists)
    click('Accept')

def open_long():
    start_chrome(server, headless=False)

    # Click 'Accept'
    click_accept()

    # Enter credentials
    enter_credentials()

def close_long():
    pass
