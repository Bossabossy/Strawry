import numpy as np
import random
from Env import Env 
from Recon import SensorReader
from datetime import datetime

read = SensorReader()
env = Env()




Q= np.zeros((env.n_state, env.n_action))
y = 0.99

num_episodes = 200

# list thats going to be used in the future
memo = []
rList = []

alpha=np.log(0.1)/num_episodes      # decay learning rate

for i in range(num_episodes):
    lr= np.exp(alpha*i) + 0.1 #decay learning rate
    s = env.reset( temp=read.get_temp(),humi=read.get_humi(),light=0,watp=0)
                                     
                                            
    rAll = 0
    done=False
  
    while done==False:               #random action to get next state and action
#        np.load(Qmemo.npy,Q)
        if np.random.rand() < lr*0.01:
            a = np.random.randint(env.n_action)
        else:
            a = np.argmax(Q[s,:] )
        s1,reward,done,_ = env.step(a)
        
        if done:
            r = 1 if reward > 0.0 else -0.1
        else:
            r =-0.00001
        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] +  lr*(r + y*np.max(Q[s1,:]) - Q[s,a])

        rAll += reward
        s = s1
        memo.append(Q)

#        np.save(Qmemo.npy,Q)

        if done == True:
            break
    if np.random.choice([True, False], p=[0.6, 0.4]) and len(memo) > 0:
        idx = np.random.choice(len(memo))
        pQ = memo[idx]
        Q = 0.1*pQ + 0.9*Q
        
    
    rList.append(rAll)
#    np.save(Qmemo,Q)
        

    
print ("Score over time: " +  str(sum(rList[-100:])/100.0))


