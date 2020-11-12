import random


def Pss(text,fist):
    ai = random.randint(0, 2)
    player = fist.index(text)
    if ai == player:
        replyMSG = '電腦出'+fist[ai]+'，平手'
    elif (ai == 0 and player == 1) or (ai == 1 and player == 2) or (ai == 2 and player == 0):
        replyMSG = '電腦出'+fist[ai]+'，你獲勝'
    else:
        replyMSG = '電腦出'+fist[ai]+'，你輸了'
    return replyMSG
