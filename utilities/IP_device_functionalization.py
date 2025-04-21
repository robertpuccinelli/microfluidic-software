import logging
from logging.handlers import TimedRotatingFileHandler
import os
from time import sleep
from plfluidics.server.valve_controller import ValveControllerRGS

cdir = os.path.dirname(os.path.abspath(__file__))
ndir = os.path.join(cdir, "logs")
os.makedirs(ndir, exist_ok=True)
filename = os.path.basename(__file__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(name)s]', datefmt='%H:%M:%S')
handler_file = TimedRotatingFileHandler(filename=cdir + '/logs/' + filename + '.log', when='m', interval=1, backupCount=1)
handler_file.setLevel(logging.INFO)
handler_file.setFormatter(formatter)
logger.addHandler(handler_file)

logger.info('Beginning script : IP Device Functionalization')

valves = []

valves.append([0,False,False,'OUT'])
valves.append([1,False,False,'IN'])
valves.append([2,False,False,'WASH'])
valves.append([3,False,False,'BSA'])
valves.append([4,False,False,'STREP'])
valves.append([5,False,False,'AB'])
valves.append([6,False,False,'EXTRA'])
valves.append([7,False,False,'PHAGE'])
valves.append([8,False,False,'WASTE'])
valves.append([9,False,False,'P1'])
valves.append([10,False,False,'P2'])
valves.append([11,False,False,'P3'])
valves.append([12,False,True]) # Initialize to reduce air leakage through bank
valves.append([13,False,True]) # Initialize to reduce air leakage through bank
valves.append([14,False,True]) # Initialize to reduce air leakage through bank
valves.append([15,False,True]) # Initialize to reduce air leakage through bank

Ctrl = ValveControllerRGS(valves)

input('Press `Enter` when control lines are ready.')


