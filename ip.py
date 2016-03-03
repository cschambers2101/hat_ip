# Gets IP address of Raspberry Pi and displays it on the Sense Hat LEDs
# Run at boot to show IP address to SSH into

import sense_hat from SenseHat
from time import sleep
from subprocess import *

ip = Popen("ip addr show wlan0 | grep inet | awk '{print $2}' |cut -d -f1", shell=True, stdout=PIPE).communicate()[0]
