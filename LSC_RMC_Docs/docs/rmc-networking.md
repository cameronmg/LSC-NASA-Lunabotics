# rmc-networking

## IP Configurations

> This describes ip configurations depending on your environment

### TE.AM IP Notation

> This notation refers to your four digit team number

- Example: - `10.TE.AM.2`
- Team 6969 - `10.69.69.2`

### Server Initialization (Robot)

> WPILiv automatically starts NetworkTables for you, no additional configuration should need to done.

### Client initialization (Driver Station/Coprocessor)

_Installation: _ `pip3 install pynetworktables`

```python:connecting to server
from networktables import NetworkTables

NetworkTables.initialize(server'10.xx.xx.2')
```

> If we we're team number 6969 then it would be 10.69.69.2

- NetworkTables does not connect instantly, you will need to wait for a connection first before trying to read data.

```python
import threading
from networktables import NetworkTables

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.xx.xx.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")
```

> Essentially, you're connecting to your host server, but, it's checking to make sure that it has established a connection

### NetworkTables in practice

- **NetworkTables** is essentially a dictionary that is shared across different computers, and, the purpose of this is so that when one value is changed it's transmitted and retrieved to another client.

### External Tools

- **WPILIB's Shuffleboard** Shuffleboard is a modern looking driveteam focused dashboard. It displays network tables data using a variety of widgets that can be positioned and controlled with robot code. It includes many extra features like: tabs, recording / playback, and advanced custom widgets.
  - [OutlineView Docs](https://docs.wpilib.org/en/stable/docs/software/dashboards/shuffleboard/index.html)
