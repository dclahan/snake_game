# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:58:52 2021

@author: clahad
"""

import matplotlib.pyplot as plt
from IPython import display
#import time

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    

''' 
if __name__ == '__main__':
    display.display(plt.gcf())
    plt.plot(range(20), range(20))
#    plt.show()
    display.display(plt.gcf())
#    time.sleep(20)
'''
    