if(code):
    ans = []
    for i in range(1,len(arr)):
        if(len(i)>3):
            nwi = i[1:]+i[0]
            ans.append(nwi)
        else:
            ran = 'dfg'
            ans.append(ran+i[::-1]+ran)