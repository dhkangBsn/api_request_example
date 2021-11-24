# This is a sample Python script.
import requests
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main(name):
    URL = 'http://15.164.232.127:5000/recommend'
    headers = {'User-Agent':'Mozila/5.0'}
    payload = {'name':'기다리지마요'}
    session = requests.Session()
    res = session.post(URL, headers=headers, data=payload)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
