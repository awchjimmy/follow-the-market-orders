from helium import *
import time
import json

env_content = ''

def load_env():
    with open('.env', 'r') as fin:
        global env_content
        env_content = fin.read()
        env_content = json.loads(env_content)

def enter_credentials():
    global env_content
    wait_until(Button('Connect to account').exists)
    write(env_content['login'], into='Enter Login')
    write(env_content['password'], into='Enter Password')
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
    click(S('div[title="Show Trade Form (F9)"]')) # Show Trade Form
    
    tfs = find_all(TextField())
    if len(tfs) == 4:
        (input_volume, input_takeprofit, input_comment, input_stoploss) = tfs
        doubleclick(input_volume)
        write('0.01', into=input_volume)

        click(Button('Buy by Market')) # Click 'Buy by Market'
        wait_until(Button('OK').exists)
    else:
        print('Error: The layout has been changed. There are {0} TextField(s).'.format(len(tfs)))

def change_symbol():
    wait_until(Text('Symbol').exists)
    write('BTCUSD', into="Search symbol")
    click(Button('BTCUSD'))

    search = find_all(TextField())[0]
    click(Button(to_right_of=search)) # Close Search Symbol
    write(LEFT_CONTROL + 'm') # Close Watch

def close_position():
    rightclick(S('div[title="BTCUSD"]'))
    click('Modify Position')
    click(S('button.orange')) # Close position

def start_browser():
    global env_content
    start_chrome(env_content['server'], headless=False)

def open_long():
    load_env()
    start_browser()
    click_accept()
    enter_credentials()
    change_layout()
    change_symbol()
    enter_volume()
    kill_browser()

def close_long():
    load_env()
    start_browser()
    click_accept()
    enter_credentials()
    change_layout()
    change_symbol()
    close_position()
    kill_browser()

