import os, time, subprocess, json
with open('ids.txt') as ids:
    ids = ids.readlines()

with open('config.json') as config:
    config = json.load(config)

    delay = int(config['delay'])

try:
    while True:
        for i in ids:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            subprocess.Popen(['steam-idle.exe', i], startupinfo=startupinfo)

        time.sleep(60*delay)
        os.system('taskkill /im steam-idle.exe')

except KeyboardInterrupt:
    os.system('taskkill /im steam-idle.exe')