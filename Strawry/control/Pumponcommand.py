from Recon import Recon , SensorReader
import time
control = Recon()
read = SensorReader()
control.humi_on()
time.sleep(5)
control.humi_off()
