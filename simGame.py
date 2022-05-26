from numpy.random import normal
import numpy as np
import matplotlib.pyplot as plt

probA = 0.6
probB = 0.6
n = 100
weather = 1
luck = True

def drawRadar(results):
    data_length = len(results[0])
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(8, 6), dpi=100)
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, score_a, color='g')
    ax.plot(angles, score_b, color='b')
    ax.set_thetagrids(angles*180/np.pi, labels)
    ax.set_theta_zero_location('N')
    ax.set_rlim(0, 1)
    ax.set_rlabel_position(270)
    plt.show()

def radar(probA,probB):
    results = [{
    "attack"   : probA * normal(probA, 0.2),
    "defence"  : probA * normal(probA, 0.2),
    "speed"    : probA * normal(probA, 0.2),
    "strength" : probA * normal(probA, 0.2),
    "technic"  : probA * normal(probA, 0.2),
    "power"    : probA * normal(probA, 0.2)
    }, {
    "attack"   : probB * normal(probB, 0.3),
    "defence"  : probB * normal(probB, 0.3),
    "speed"    : probB * normal(probB, 0.3),
    "strength" : probB * normal(probB, 0.3),
    "technic"  : probB * normal(probB, 0.3),
    "power"    : probB * normal(probB, 0.3)}]
    
    drawRadar(results)
    

def printsummary(winsA, winsB):
    n = winsA+winsB
    print("分析开始，共模拟{}场比赛".format(n))
    print("A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))

def luckCondition(probA,probB):
    if (luck):
        probA = normal(probA, 0.05)
        probB = normal(probB, 0.05)
    return probA, probB

def weatherCondition(probA,probB): #Weather condition may affect the prabability
    if weather == 1:
        print("The Weather is Sunny")
        probA = 1.2 * probA
        probB = 1.1 * probB
    elif weather == 2:
        print("The Weather is Cloudy")
        probA = 1 * probA
        probB = 1 * probB
    elif weather == 3:
        print("The Weather is Windy")
        probA = 0.8 * probA
        probB = 0.9 * probB
    elif weather == 4:
        print("The Weather is Rainy")
        probA = 0.7 * probA
        probB = 0.8 * probB
    return probA, probB

def gameOver(a,b):
    return a or b
    
#这里将返回Ture或False
def simOnegame(probA,probB):
    scoreA, scoreB = 0, 0
    serving = "A" #A发球
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if normal(probB, 0.1) < probA: #Normal Distribution
                scoreA += 1
            else :
                serving = "B"
        else:
            if normal(probA, 0.1) < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def simGame():
    winsA, winsB = 0, 0
    probA1, probB1 = weatherCondition(probA,probB)
    probA2, probB2 = luckCondition(probA1,probB1)
    print("ProbA1 = ", probA2)
    print("ProbB1 = ", probB2)
    for i in range(n):
        scoreA, scoreB = simOnegame(probA2, probB2)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    printsummary(winsA, winsB) #总结
    radar(probA2,probB2)
    return winsA, winsB

if __name__ == '__main__':
    simGame()