def timeConversion(s):
    
    oldH = s[0:2]
    oldM =s[3:5]
    oldS = s[6:8]
    
    am_pm = s[8:]
    
    if am_pm == 'PM':
        newH = str((int(oldH) % 12) + 12)
    else:
        newH = str((int(oldH) % 12))
        
    if int(newH) < 10:
        newH = "0"+newH
        
    
    ans = newH + ":" + oldM + ":" + oldS
    
    return ans