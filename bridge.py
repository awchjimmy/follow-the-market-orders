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
    time.sleep(3)

def click_accept():
    wait_until(Button('Accept').exists)
    click('Accept')

def change_layout():
    wait_until(Text('Symbol').exists)
    time.sleep(2)
    press(ALT + '3') # from 'CandleSticks' to 'Area'

def enter_volume():
    wait_until(Text('Symbol').exists)
    press(F9) # Press F9 to Show Trade Form 
    tfs = find_all(TextField())

    if len(tfs) == 5:
        input_comment = tfs[0]
        input_stoploss = tfs[1]
        input_takeprofit = tfs[2]
        input_volume = tfs[3]
        input_searchsymbol = tfs[4]

        doubleclick(input_volume)
        write('1', into=input_volume) # Volume: 1.00

        click(Button('Buy by Market')) # Click 'Buy by Market'
        wait_until(Button('OK').exists)
    else:
        print('Error: The layout has been changed.')


def open_long():
    start_chrome(server, headless=False)

    # Click 'Accept'
    click_accept()

    # Enter credentials
    enter_credentials()

    # Change layout
    change_layout()

    # Enter volume
    enter_volume()

    # Kill browser
    kill_browser()

def close_long():
    pass
