# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:07:12 2022

@author: Prof. Dr. Drews
"""

import sys

class ReinforcementAlgorithm:
    
    def __init__(self):
        pass

class Environment:
    
    def __init__(self):
        pass


class Chatbot:
    
    def __init__(self):
        self.InputTextInMemory=[]
        self.OutputTextInMemory=[]
        self.start()
        self.showInput()
    
    def start(self):
        index = 0
        while(True):
            if(index == 0):
                response = self.getResponse('Möchten Sie mir etwas mitteilen?\nZum Abbrechen: "n" für "no" eingeben\n >>>')
            else:
                self.dummyRuleBasedAnswer(response)
                response = self.getResponse("Eingabe:")
                if(response=="n"):
                    break
            self.storeInput("memory", response)
            index=index+1
            
    def showInput(self):
        print("\n-------\nIhre Eingaben:")
        for word in self.InputTextInMemory:
            print(word)
            
    def getResponse(self,text):
        return input(text)
            
    def storeInput(self, type, response):
        if type=="memory":
            self.InputTextInMemory.append(response)
            
    def generateOutput(self, response):
        self.dummyRuleBasedAnswer(response)
        
    def dummyRuleBasedAnswer(self, response):
        if len(response)<6:
            text="Chatbot: Ja\n"
            sys.stdout.write(text)
            self.OutputTextInMemory.append(text)
        else:
            text="Chatbot: Nein\n"
            sys.stdout.write(text)
            self.OutputTextInMemory.append(text)
                        
            
            
if __name__=="__main__":
    
    chatbot = Chatbot()
            
            