looper = int(input())list=' 'list2=[]mainlist=[]for i in range(looper):    list=input()    list2=str.split(list)    mainlist.append(list2)"""for i in range(looper):    for j in range(4):        print(mainlist[i][j],i,j)""""""for i in range(looper):        for j in range(1,looper+1):            print(type(int(mainlist[i][j])))            print(int(mainlist[i][j])+1)"""#print(mainlist)sum=0.00listnew=[]track=[]for i in range(looper):    sum=0.00    for j in range(4):        #print(mainlist[i][j],i,j)        if(j>0):           sum=sum+float(mainlist[i][j])    average=float(sum/3)    listnew.append(i)    listnew.append(average)track.append(listnew)search=str(input())"""for j in range(looper*2):    if (j%2!=0):        print(track[0][j])"""for i in range(looper):        #print(mainlist[i][0])        if(mainlist[i][0]==search):            if(looper>2):               myvalue=track[0][i*looper-1]            else:                myvalue=track[0][i]            print(myvalue,"HELLO")if(looper>=2 and looper<=10):    for i in range(looper):        for j in range(1,looper+1):            if (float(mainlist[i][j])>=0.00 and float(mainlist[i][j])<=100.00):                flag=0if flag==0:    myvalue=str(myvalue)    myvalue=myvalue+'0'    print(myvalue)"""for i in range(looper):    for j in range(4):        print(track[i][j],i,j)"""