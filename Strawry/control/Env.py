import time
import numpy as np 
from datetime import datetime
from Recon import SensorReader, Reacon


class Env(object):

    def cap(self,x, down, up, ninter):
        if x<=down:
            x=down
        if up<=x:
            x=up-1
        step=(up-down)/ninter
        #print x
        return (x-down)//step

    def __init__(self):
        self.n_action=16
        self.n_state=500        
        self.max_step=25
        self.recon= Recon()
        self.reset()
        self.cs=0
        self.origin=datetime.now()
      


            
    def get_state(self):        
        x1=self.cap(self.temp, 10, 25, 10)
        x2=self.cap(self.humi, 10, 100, 5)
        x3=self.light
        x4=self.watp
        return int(x1*5*2*2 + x2*5*2*2 + x3*2*2 + x4*2 +x5)

    
    def reset(self, temp=25, humi=50, light=0, watp=0):        
        self.temp=temp
        self.humi=humi
        self.light=light
        self.watp=watp
        self.done=0
        self.n_step=0
        return self.get_state()
    
    def set_target(self, temp=25, humi=80, light=0, watp=0):
        self.t_temp=temp
        self.t_humi=humi
        self.t_light=light
        self.t_watp=watp
        return self.get_state()
  
    def get_reward(self):
        if self.t_temp-1<self.temp and self.temp<=self.t_temp+1:
            if self.t_humi-5<self.humi and self.humi<=self.t_humi+5:
                return 1         
        return 0
        #return np.log(np.sqrt(((self.t_temp-self.temp)**2)+((self.t_humi-self.humi)**2)))

    def code2int(self,code):
        #(comp,mist,light,watp)
        return code[0]*8 + code[1]*4 + code[2]*2 + code[3]
    
    def int2code(self,a=0):
        b=bin(16+a)
        return int(b[-4]),int(b[-3]),int(b[-2]),int(b[-1])
    
    def step(self,a):
        self.cycle()
        self.n_step+=1
        comp,mist,light,watp = self.int2code(a)
        
        if comp==1:
            self.recon.com_on()
        else:
            self.recon.com_off()
    
        if mist==1:
            self.recon.humi_on()
        else :
            self.recon.humi_off()
       
        if light==1:
            self.recon.light_on()
        else:
            self.recon.light_off()

        if watp==1:
            self.recon.pump_on()
        else:
            self.recon.pump_off()

        if self.max_step <= self.n_step:
            self.done=1
            
        time.sleep(30)

        self.temp = SensorReader.get_temp()
        self.humi = SensorReader.get_humi()
        
        return self.get_state(), self.get_reward(), self.done, 0
    
    def render(self):
        print( "step:{} temp:{}, humi:{}, light:{}, watp{}".format(
             self.n_step, self.temp, self.humi, self.light, self.watp))

    def cycle(self):
        if cs == 0:
            self.set_target(temp=18, humi= 80, light=1 ,watp =1)
            print("light on and pump on")
            if 2 <= (datetime.now()-origin).minutes:
                cs = 1
                origin=datetime.now()
            else :
                print("Morning water")
        if cs == 1:
            self.set_target(temp=18, humi= 80, light=1 ,watp =0)
            print("light on and pump off")
            if 6 <= (datetime.now()-origin).hours:
                cs = 2
                origin=datetime.now()
            else:
                print("Morning time")
        if cs == 2:
            self.set_target(temp=10, humi= 60, light=0 ,watp =1)
            print("light off and pump on")
            if 2 <= (datetime.now()-origin).minute:
                cs = 3
                origin=datetime.now()
            else :
                print("Night water")
        if cs == 3:
            self.set_target(temp=10, humi= 60, light=0 ,watp =0)
            print("light off and pump off")
            if 18 <= (datetime.now()-origin).hours:
                cs = 0
                origin=datetime.now()
            else:
                print("Night time")
