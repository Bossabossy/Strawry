from Recon import Recon , SensorReader
import time
control = Recon()
read = SensorReader()

for i in range(120):
	print(i)
	control.com_on()
	time.sleep(1)
	control.com_off()
	time.sleep(1)
control.clean()
