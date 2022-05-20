import datetime

def getDate():
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())

def getTime():
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
