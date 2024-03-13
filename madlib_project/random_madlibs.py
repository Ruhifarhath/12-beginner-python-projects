from sample_madlibs import hp,zombie,code,hunger_games  
import random

if __name__=='__main__':
    m=random.choice([hp,code,hunger_games,zombie])
    m.madlib()