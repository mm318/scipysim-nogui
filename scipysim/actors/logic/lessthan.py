'''
Created on Feb 2, 2010

@author: Brian Thorne
'''
from scipysim.actors.logic import Compare

class LessThan(Compare):
    def compare(self, event):
        return event.value < self.threshold
