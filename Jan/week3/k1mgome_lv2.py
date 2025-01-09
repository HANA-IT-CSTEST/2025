def solution(s):
    n=0
    c=0
    while s!='0':
        if s=='1':
            break
        else :
            n=n+s.count("0")
            s=str(format(len(s.replace("0","")),'b'))
            c=c+1
    answer=[c,n]
    return answer