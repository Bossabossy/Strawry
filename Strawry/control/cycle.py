from datetime import datetime
from recon import Recon

control = Recon()
cs=0
origin=datetime.now()
if cs == 0:
    control.light_on()
    control.pump_on()
    print("light on and pump on")
    if 2 <= (datetime.now()-origin).minutes:
        cs = 1
        origin=datetime.now()
    else :
        print("something is wrong at cs0 ---> cs1")
if cs == 1:
    control.light_on()
    control.pump_off()
    print("light on and pump off")
    if 6 <= (datetime.now()-last).hours:
        cs = 2
        origin=datetime.now()
    else:
        print("something is wrong at cs1 --> cs 2")

if cs == 2:
    control.light_off()
    control.pump_on()
    print("light off and pump on")
    if 2 <= (datetime.now()-origin).minute:
        cs = 3
        origin=datetime.now()
    else :
        print("something is wrong at cs 2 --> cs 3")
if cs == 3:
    control.light_off()
    control.pump_off()
    print("light off and pump off")
    if 18 <= (datetime.now()-origin).hours:
        cs = 1
        origin=datetime.now()


        
            
        
        