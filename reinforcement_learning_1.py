# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:58:57 2022

@author: baum2
"""
import random
import pandas as pd
import re
import enum

# #create Environment class
class MyEnvironment:

    def __init__(self):
    
        self.remaining_steps=20
    
    def get_observation(self):
    
        return ["happy","sad","angry"]
    
    def get_actions(self):
    
        return ["congratulate","comfort","cool down"]
    
    def check_is_done(self):
    
        return self.remaining_steps==0
    
    def action(self,p_environment,p_action):
    
        if self.check_is_done():
        
            raise Exception("Game over")
            
        self.remaining_steps-=1
        res=0
        if p_environment=="happy":
            if p_action == "congratulate":
                res=1
            elif p_action == "comfort":
                res=0
            else:
                res=-1
        if p_environment=="sad":
           if p_action == "congratulate":
               res=-1
           elif p_action == "comfort":
               res=1
           else:
               res=0
        if p_environment=="angry": 
           if p_action == "congratulate":
               res=-1
           elif p_action == "comfort":
               res=0
           else:
               res=1
                
        return res
    
class myAgent:
   def __init__(self):
     self.total_rewards=0.0
     
   def step(self,ob:MyEnvironment):
     dict_mapping = {}
     
     list_obs = ob.get_observation()
     list_actions = ob.get_actions()
     
        
     curr_obs=random.choice(list_obs)
     print(curr_obs)
     
     if (pd.Series([curr_obs in i for i in dict_mapping.keys()]).sum())<=1:
         curr_action=random.choice(list_actions)
     elif (pd.Series([curr_obs in i for i in dict_mapping.keys()]).sum())==2:
         for num,j in [i for i in dict_mapping.keys() if curr_obs in i]:
             if num==0:
                 res = dict_mapping[j]
             else:
                 res = max(res,dict_mapping[j])
         
         list_actions = list(set(list_actions) - set([re.split(i)[0] for i in dict_mapping.keys() if curr_obs in i])).append()         
                 

         

     
     print(curr_action)
     
     curr_reward=ob.action(curr_obs,curr_action)    
     self.total_rewards+=curr_reward
     
     
     
     dict_mapping[curr_obs+"-" +curr_action]=curr_reward
         
     
     print("Total rewards so far= %.3f "%self.total_rewards)
     print("==============================================")
     
     
     
if __name__=='__main__':

    obj=MyEnvironment()
    
    agent=myAgent()
    
    step_number=0
    
    while not obj.check_is_done():
    
        step_number+=1
        
        print("Step-",step_number)
        
        agent.step(obj)
        
        print("Total reward is %.3f "%agent.total_rewards)