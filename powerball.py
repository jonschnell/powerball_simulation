'''
@author: Jonathon Schnell

@date: 9/29/2020

@version: 1.0.0

'''

import random

if __name__ == "__main__":
    day = 0
    while day < 10:
        balls = []
        i = 0
        seed = 100
        
        random.seed(seed + day)
        while i < 6:
            w = random.randint(1,69)
            if w not in balls:
                balls.append(w)
                i = i + 1
                
        r = random.randint(1,26)
        balls.append(r)
        print day, " : ", balls
        day = day + 1
        