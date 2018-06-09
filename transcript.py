'''

API for getting messages from transcript

'''

import urllib.request, re
import webbrowser

import html_code as hc

class Room:

    def __init__(self, room_number, year=0, month=0, day=0):
        
        if year != 0 and month != 0 and day != 0: 
            self.room_url = 'https://chat.stackoverflow.com/transcript/{}/{}/{}/{}'.format(room_number, year, month, day)
        else:
            self.room_url = 'https://chat.stackoverflow.com/transcript/{}'.format(room_number)

    

    def request(self):
        '''Request the raw page'''
        request = urllib.request.urlopen(self.room_url)
        return request.read()
            
        

    def user_id(self):
        '''Get user id in order of time'''
        regex = re.compile(br'<div class="monologue user-(\d+)">')
        return regex.findall(self.request())

    def user(self):
        '''Get user name in order of time'''
        regex = re.compile(br'<div class="username"><a href="\S+" title="(\S+)">')
        return regex.findall(self.request())

    def time(self):
        '''Get the time of the post'''
        regex = re.compile(br'<div class="timestamp">(\d+:\d+ \S+)</div>')
        return regex.findall(self.request())

    def messages(self, raw=False):
        '''Get each messages in order of time'''
        regex = re.compile(br'<div class=\"content\">([\S|\s]+?)</div>')
        messages = [x.strip(b'                      \r\n                    ') for x in regex.findall(self.request())]

        if raw == True:
            return messages

        else:
            return [hc.replace(message) for message in messages]

