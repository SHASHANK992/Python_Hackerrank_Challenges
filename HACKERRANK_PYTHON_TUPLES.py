import builtinsT = tuple()new = []input1=[]input2=[]looper=input("")input1=input()#print(input1)input2 = str.split(input1)for i in range(len(input2)):    input2[i]=int(input2[i])#print(type(input2[1]))#print(input2)Tuple=tuple(input2)#print(Tuple)print(builtins.hash(Tuple))""" ACCEPTED CODE:import __builtin__T = tuple()new = []input1=[]input2=[]looper=raw_input("")input1=raw_input()#print(input1)input2 = str.split(input1)for i in range(len(input2)):    input2[i]=int(input2[i])#print(type(input2[1]))#print(input2)Tuple=tuple(input2)#print(Tuple)print(__builtin__.hash(Tuple))"""