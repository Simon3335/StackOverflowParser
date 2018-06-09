# StackOverflowParser
A module to scrape and parse Stack Overflow using only default library tools.

**driver.py**

A graphic interface allowing the module to be used more simply.

**console.py**

The module used to log all the events.

**Transcript.py**

Example to get all messages:

import transcript as ts
room = ts.Room(6)
print(room.messages())
