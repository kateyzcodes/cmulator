# this is my utility function for optimizing stats bars

# resource used: http://www.gameaipro.com/GameAIPro/GameAIPro_Chapter09_An_Introduction_to_Utility_Theory.pdf

class Bar(object):
    def __init__(self, name):
        self.name = name
        self.level = 100

class Action(object):
    def __init__(self, name, statsAffected, barsAffected):
        self.name = name
        self.barsAffected = barsAffected
        self.statsAffected = statsAffected
        self.healthEffect = statsAffected[0]
        self.energyEffect = statsAffected[1]
        self.happinessEffect = statsAffected[2]
    
def getUtility(action):
    print(action.name)
    print('__________')
    for bar in action.barsAffected:
        # print(f'{bar.name} = {bar.level}')
        if bar.name == 'health':
            if 0<=bar.level+action.healthEffect<=100:
                healthU = ((bar.level+action.healthEffect)/100)**5
            else:
                healthU = ((bar.level)/100)**5
            print(f'healthU = {healthU}')
        if bar.name == 'energy':
            if 0<=bar.level+action.healthEffect<=100:
                energyU = ((bar.level+action.energyEffect)/100)**3
            else:
                energyU = ((bar.level)/100)**3
            print(f'energyU = {energyU}')
        if bar.name == 'happiness':
            if 0<=bar.level+action.healthEffect<=100:
                happyU = ((bar.level+action.happinessEffect)/100)**2
            else:
                happyU = ((bar.level)/100)**2
            print(f'happyU = {happyU}')
    print('----------')
    return (healthU + energyU + happyU)/3