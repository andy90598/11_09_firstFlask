from a11_3_news import news
def NewsTitle(text):
    newstitle = ''
    media = ''
    a = news()
    # 媒體
    for i in a['headNews'][0]:
        media = media+i+'\n'
    # 標題
    if text in a['headNews'][0].keys():
        for i in range(len(a['headNews'][0][text]['title'])):
            newstitle = newstitle+a['headNews'][0][text]['title'][i]+'\n' + \
                a['headNews'][0][text]['link'][i] + \
                '\n'+'------------------------'+'\n'
        replyMSG = newstitle  
    return media,replyMSG