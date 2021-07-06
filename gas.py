#Cracked by dziu69
from json import encoder
from typing import Container
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import HorizontalSeparator
import pyautogui, time, json, threading
from datetime import datetime
from os import path
from appdata import AppDataPaths
import pyperclip, requests
from win32gui import GetWindowText, GetForegroundWindow
import emoji, surrogates, sched

pyautogui.FAILSAFE = False
config_file_path = 'configs.json'
if not path.exists(config_file_path):
    new_json_dict = {'groups':[],  'waves_interval':15,  'groups_interval':0.3,  'max_duration':'0',  'max_messages':'0'}
    with open(config_file_path, 'w+', newline='\n') as (outfile):
        json.dump(new_json_dict, outfile)
        outfile.close()
with open(config_file_path) as (json_file):
    data = json.load(json_file)
    groups_text = my_string = ', '.join(map(str, data['groups']))
    if 'waves_interval' not in data:
        data['waves_interval'] = 15
        with open(config_file_path, 'w', newline='\n') as (outfile):
            json.dump(data, outfile)
    if 'groups_interval' not in data:
        data['groups_interval'] = 0.2
        with open(config_file_path, 'w', newline='\n') as (outfile):
            json.dump(data, outfile)
    if 'max_duration' not in data:
        data['max_duration'] = '0'
        with open(config_file_path, 'w', newline='\n') as (outfile):
            json.dump(data, outfile)
    if 'max_messages' not in data:
        data['max_messages'] = '0'
        with open(config_file_path, 'w', newline='\n') as (outfile):
            json.dump(data, outfile)
    waves_interval = data['waves_interval']
    groups_interval = float(data['groups_interval'])
    max_duration = float(data['max_duration'])
    max_messages = float(data['max_messages'])
    json_file.close()

def waitUntilTelegramWindow():
    current_window_name = GetWindowText(GetForegroundWindow()).lower()
    while 'telegram' not in current_window_name.lower():
        current_window_name = stop_bot or GetWindowText(GetForegroundWindow())
        time.sleep(0.1)


def inTelegramWindow():
    current_window_name = GetWindowText(GetForegroundWindow()).lower()
    if 'telegram' not in current_window_name.lower():
        if not stop_bot:
            print('Please switch to Telegram Desktop to keep the bot running.')
            while 'telegram' not in current_window_name.lower():
                current_window_name = stop_bot or GetWindowText(GetForegroundWindow())
                time.sleep(0.1)


searchResult = [
 95, 96]

def changeChat(username):
    pyautogui.press('esc')
    pyperclip.copy(username)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.15)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')


def typeShill():
    pyperclip.copy('CRACKED BY @dziu69')
    pyautogui.hotkey('ctrl', 'v')


first_col = [
 [
  sg.Text('List of group names (comma separated)')],
 [
  sg.Multiline(size=(60, 6), font=('Courier', 10), key='-GROUPS-', default_text=groups_text)],
 [
  sg.Text('Text to advertise (You can copy & paste a message)')],
 [
  sg.Multiline(size=(60, 11), font=('Courier', 10), key='-TEXT-', default_text='This is a DEMO for TGAdvertiserBOT by @vobruno', disabled=True)],
 [
  sg.Text(' Relative image path: '),
  sg.In(size=(40, 1), font=('Courier', 10), key='-IMAGEPATH-', default_text='Not available in demo', disabled=True)],
 [
  sg.Column([
   [
    sg.Text('Time interval between waves (s)'), sg.In(size=(4, 1), font=('Courier', 10), key='-WAVESINTERVAL-', default_text=waves_interval)],
   [
    sg.Text('Time interval between groups (s)'), sg.In(size=(4, 1), font=('Courier', 10), key='-GROUPSINTERVAL-', default_text=groups_interval)]]),
  sg.Column([
   [
    sg.Text('Max duration (mins)'), sg.In(size=(4, 1), font=('Courier', 10), key='-MAXDURATION-', default_text=(str(max_duration)))],
   [
    sg.Text('Max messages p/group'), sg.In(size=(4, 1), font=('Courier', 10), key='-MAXMESSAGES-', default_text=max_messages)]])],
 [
  sg.HorizontalSeparator(pad=(10, 20))],
 [
  sg.Button('START'), sg.Button('STOP', disabled=True), sg.Text('Official website: TgAdvertiserBot.com')]]
second_col = [
 [
  sg.Output(size=(50, 27), font=('Courier', 10), key='-STATUS-')]]
layout = [
 [
  sg.Column(first_col), sg.Column(second_col)]]

def showStats():
    end_time = datetime.now().strftime('%H:%M:%S')
    print('--- STATISTICS ---')
    print('Start time: ' + start_time.strftime('%H:%M:%S') + ' - End time: ' + end_time)
    sum = 0
    for idx, group in enumerate(groups):
        sum += statistics[idx]

    print('Total messages sent: ' + str(sum))


def stopBot(show_stats=True):
    if show_stats:
        print('Bot stopped\n')
        showStats()
    window['-GROUPS-'].Update(disabled=False)
    window['-WAVESINTERVAL-'].Update(disabled=False)
    window['-GROUPSINTERVAL-'].Update(disabled=False)
    window['-MAXDURATION-'].Update(disabled=False)
    window['-MAXMESSAGES-'].Update(disabled=False)
    window.FindElement('START').Update(disabled=False)
    window.FindElement('STOP').Update(disabled=True)


def startAds():
    global groups_interval
    global max_duration
    global max_messages
    global stop_bot
    global waves_interval
    print('Starting bot')
    print('- Number of groups: ' + str(len(groups)))
    print('- Using image: No\n')
    print('Please switch to Telegram Desktop. The bot will begin automatically.\n')
    waitUntilTelegramWindow()
    if stop_bot:
        return
    print('Bot started')
    time.sleep(1)
    stop_max = False
    while 1:
        for idx, group in enumerate(groups):
            if stop_bot:
                break
            else:
                if max_duration > 0:
                    if (datetime.now() - start_time).total_seconds() / 60 >= max_duration:
                        stop_max = True
                        stop_bot = True
                        break
                inTelegramWindow()
                changeChat(group)
                typeShill()
                pyautogui.press('enter')
                statistics[idx] += 1
                if max_messages > 0 and statistics[idx] >= max_messages:
                    stop_max = True
                    stop_bot = True
                    break
            time.sleep(groups_interval)

        for i in range(int(waves_interval) * 2 - 1):
            if stop_bot:
                break
            time.sleep(0.5)

        if stop_max:
            print('Max reached')
            stopBot()
        if stop_bot:
            break


credentials_layout = [
 [
  sg.Text('CRACKED BY @dziu69')],
 [
  sg.Text('Please enter your licence (case sensitive)')],
 [
  sg.In(key='-LICENCE-')],
 [
  sg.Button('VERIFY')]]

def stopBotThread():
    botThread.join(timeout=2)
    if botThread.is_alive():
        print("Bot couldn't stop. Trying again.")
        s = sched.scheduler(time.time, time.sleep)
        s.enter(1, 1, stopBotThread)
        s.run()
        return
    stopBot()


def main():
    global botThread
    global data
    global groups
    global groups_interval
    global max_duration
    global max_messages
    global start_time
    global statistics
    global stop_bot
    global waves_interval
    global window
    paths = AppDataPaths('TGAdvertiserBOT DEMO')
    if not path.exists(paths.main_config_path):
        window = sg.Window(title='CRACKED BY @dziu69', layout=credentials_layout, margins=(25,
                                                                                                                            25))
        must_exit = False
        while 1:
            event, values = window.read()
            if not event == 'Exit':
                if event == sg.WIN_CLOSED:
                    must_exit = True
                    break
                if event == 'VERIFY':
                    datas = {'licence': values['-LICENCE-']}
                    url = 'https://tgadvertiserbot.com/validate_demo.php'
                    try:
                        requests.get('https://www.google.com', timeout=5)
                        response = requests.post(url, datas)
                        response_json = response.json()
                        if response_json['status'] == 'error':
                            paths.setup(verbose=False)
                            
                        else:
                            if response_json['status'] == 'ok':
                                paths.setup(verbose=False)
                                window.close()
                                break
                    except (requests.ConnectionError, requests.Timeout) as exception:
                        try:
                            sg.Popup('Please verify your internet connection.')
                        finally:
                            exception = None
                            del exception

        if must_exit:
            return
    window = sg.Window(title='CRACKED BY @dziu69', layout=layout, margins=(25,
                                                                                                            25))
    while 1:
        event, values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        if event == 'STOP':
            print('STOP order received... Please wait.')
            stop_bot = True
            stopBotThread()
        if event == 'START':
            if values['-GROUPS-'].strip() == '':
                sg.Popup('You must write at least one group')
                continue
            if values['-WAVESINTERVAL-'].strip() == '' or float(values['-WAVESINTERVAL-'].strip()) < 0:
                sg.Popup('You must write time for interval between waves')
                continue
            if values['-GROUPSINTERVAL-'].strip() == '' or float(values['-GROUPSINTERVAL-'].strip()) < 0:
                sg.Popup('You must write time for groups interval')
                continue
            if values['-MAXDURATION-'].strip() == '' or float(values['-MAXDURATION-'].strip()) < 0:
                sg.Popup('You must write time for max duration. "0" means infinite time')
                continue
        if not values['-MAXMESSAGES-'].strip() == '':
            if float(values['-MAXMESSAGES-'].strip()) < 0:
                sg.Popup('You must write max number of messages p/group. "0" means infinite messages')
                continue
            window['-GROUPS-'].Update(disabled=True)
            window['-WAVESINTERVAL-'].Update(disabled=True)
            window['-GROUPSINTERVAL-'].Update(disabled=True)
            window['-MAXDURATION-'].Update(disabled=True)
            window['-MAXMESSAGES-'].Update(disabled=True)
            groups = [group.strip() for group in values['-GROUPS-'].split(',')]
            statistics = [0] * len(groups)
            data['groups'] = groups
            data['waves_interval'] = values['-WAVESINTERVAL-']
            waves_interval = data['waves_interval']
            data['groups_interval'] = values['-GROUPSINTERVAL-']
            groups_interval = float(data['groups_interval'])
            data['max_duration'] = str(values['-MAXDURATION-'])
            max_duration = float(data['max_duration'])
            data['max_messages'] = str(values['-MAXMESSAGES-'])
            max_messages = float(data['max_messages'])
            with open(config_file_path, 'w', newline='\n') as (outfile):
                json.dump(data, outfile, ensure_ascii=False)
            stop_bot = False
            window.FindElement('START').Update(disabled=True)
            window.FindElement('STOP').Update(disabled=False)
            start_time = datetime.now()
            botThread = threading.Thread(target=startAds)
            botThread.start()


if __name__ == '__main__':
    main()
# okay decompiling main.pyc
