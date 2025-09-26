def merge_the_tools(string, k):
    
    subs = []
    cleanSubs = []
    
    for i in range(0,int(len(string)/k)):
        sub = string[k*i: k*(i+1)]
        subs.append(sub)
        
    for i in subs:
        lst = list(i)
        clean_lst = ""
        for i in lst:
            if i not in clean_lst:
                clean_lst += i
        cleanSubs.append(clean_lst)
        
    for i in cleanSubs:
        print(f"{i}")