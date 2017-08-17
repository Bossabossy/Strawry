import numpy as np 




class Env(object):

	def cap(self,x, down, up, ninter):
        if x<down:
            x=down
        if up<=x:
            x=up-1
        step=(up-down)/ninter
        #print x
        return (x-down)//step

    def __init__(self):
        self.n_action=16
        self.n_state=500        
        self.max_step=100
        self.reset()

            
    def get_state(self):        
        x1=self.cap(self.temp, 10, 25, 5)
        x2=self.cap(self.humi, 10, 100, 5)
        x3=self.cap(self.co2, 300, 3000, 5)
        x4=self.light
        x5=self.watp
        return int(x1*5*5*2*2 + x2*5*2*2 + x3*2*2 + x4*2 +x5)

    
    def reset(self, temp=25, humi=50, co2=350, light=0, watp=0):        
        self.temp=temp
        self.humi=humi
        self.co2=co2
        self.light=light
        self.watp=watp
        self.done=0
        self.n_step=0
        return self.get_state()
    
    
    def get_reward(self):
        if self.t_temp-2<self.temp and self.temp<=self.t_temp+2:
            if self.t_humi-10<self.humi and self.humi<=self.t_humi+10:
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
        self.n_step+=1
        comp,mist,light,watp = self.int2code(a)
        if comp==1:
            self.humi-=5
            self.temp-=1
        if mist==1:
            self.humi+=5
        if light==1:
            self.humi+=1
            self.temp+=1
        if watp==1:
            self.humi+=1
        if self.max_step <= self.n_step:
            self.done=1
        return self.get_state(), self.get_reward(), self.done, 0
    
    def render(self):
        print( "step:{} temp:{}, humi:{}, co2:{}, light:{}, watp{}".format(
             self.n_step, self.temp, self.humi, self.co2, self.light, self.watp))
