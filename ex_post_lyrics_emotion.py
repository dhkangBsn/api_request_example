# This is a sample Python script.
import requests
import json

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    URL = 'http://15.164.232.127:5001/lyrics_emotion'
    headers = {'User-Agent':'Mozila/5.0'}
    payload = {'lyrics':'기다리지마요'}
    session = requests.Session()
    res = session.post(URL, headers=headers, data=payload)
    result = json.loads(res.text)['emotion_score']
    print(result)
    session.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
