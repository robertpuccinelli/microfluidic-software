import logging
from logging.handlers import TimedRotatingFileHandler
import os
from time import sleep
from plfluidics.valve_controller import ValveControllerRGS

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

logger.info('Beginning script : HW Test RGS Controller')

valves = []
valve_names = ['OUT', 'IN', 'WASH', 'BSA', 'STREP', 'AB', 'EXTRA', 'PHAGE', 'WASTE', 'P1', 'P2', 'P3']

for i in range(len(valve_names)):
    valves.append([i,False,False,valve_names[i]])

VCRGS = ValveControllerRGS(valves)

logger.info('Opening valves sequentially.')
for valve in valve_names:
    VCRGS.setValvesOpen([valve])
    sleep(0.01)

logger.info('Closing valves sequentially.')
for valve in valve_names:
    input('Press enter close valve {} '.format(valve))
    VCRGS.setValvesClosed([valve])

