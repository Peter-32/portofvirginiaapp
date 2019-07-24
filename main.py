import os
import subprocess
import pandas as pd
import pyautogui as g
from time import sleep
import pyperclip as clip
from datetime import datetime

g.FAILSAFE = True
sleep(2)
g.size()
g.position()

def c():
    g.mouseDown()
    g.mouseUp()

def c2():
    c()
    c()

def rc():
    g.click(button='right')

def select_all_and_copy():
    rc()
    g.keyDown('a')
    g.keyUp('a')
    g.keyDown('ctrl')
    g.keyDown('c')
    g.keyUp('c')
    g.keyUp('ctrl')

def json_to_csv(license_plate):
    # Make JSON
    file = open("data.json", "w")
    file.write(clip.paste())
    file.close()

    try:
        # JSON to CSV
        run_command('in2csv "data.json" > "~/Desktop/output/{}_data.csv"'.format(license_plate))

        # Remove JSON
        os.remove("data.json")
    except Exception as e:
        print(e)

def run_command(command):
    try:
        subprocess.check_output(command, shell=True)
    except:
        raise

def main():
    i = 1
    df = pd.read_csv("~/Desktop/input.csv")
    for index, row in df.iterrows():
        start_date = row['start_date']
        end_date = row['end_date']
        license_plate = row['license_plate']
        g.moveTo(12, 632)
        c()
        g.keyDown('ctrl')
        g.keyDown('t')
        g.keyUp('ctrl')
        g.keyUp('t')
        sleep(0.3)
        clip.copy("http://propassva.portofvirginia.com/api/gate?startDateTime={}T07:00:00.000Z&endDateTime={}T07:00:00.000Z&licensePlate={}".\
                    format(start_date, end_date, license_plate))
        sleep(0.3)
        g.keyDown('ctrl')
        g.keyDown('v')
        g.keyUp('ctrl')
        g.keyUp('v')
        sleep(0.1)
        g.keyDown('enter')
        g.keyUp('enter')
        sleep(3.0)
        c()
        sleep(3.0)
        g.keyDown('ctrl')
        g.keyDown('a')
        g.keyUp('a')
        sleep(0.5)
        g.keyDown('c')
        g.keyUp('c')
        g.keyUp('ctrl')
        json_to_csv(license_plate)


#Execute the application
if __name__ == "__main__":
    main()
