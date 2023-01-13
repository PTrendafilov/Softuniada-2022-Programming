a=int(input())
name=input()
s=""
for j in range(a):
    for i in range(a):
        s+=" "
    for i in range(3):
        if i==2:
            s += "~"
        else:
            s+="~ "
    """for i in range(a):
        s+=" " """
    s+="\n"
for i in range(a*3+6-1):
    s+="="
draw=False
for j in range(a-2):
    s+="\n|"

    if (a==3 or a-((j+1)*2)==1 or a-((j+1)*2)==0) and draw!=True:
        for i in range((a*3+6-a-2-len(name))//2):
            s+="~"
        s+=name.upper()
        for i in range((a*3+6-a-2-len(name))//2):
            s+="~"
        draw=True
    else:
        for i in range(a*3+6-a-2):
            s+="~"
    s+="|"
    for i in range(a-1):
        s+=" "
    s+="|"
s+="\n"
for i in range(a*3+6-1):
    s+="="
temp=a
space=0
for j in range(temp):
    s+="\n"
    for i in range(space):
        s+=" "
    s+="\\"
    for i in range(temp*3+6-temp-2):
        s+="@"
    s+="/"
    temp-=1
    space+=1
s+="\n"
for i in range(a*3+6-1):
    s+="-"


print(s)
