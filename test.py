import random
import numpy as np
from sys import stdin, stdout
import json
from collections import Counter


def randVec(m=10,lo=-10,hi=10,uniq=False):
    """
    creates random vector of integers
    :param m: size of vector
    :param lo: low end of range    
    :param hi: high end of range (inclusive)
    :param uniq: unique values or not
    :return: random vector
    """
    if not uniq:
        return [random.randint(lo,hi) for _ in range(m)]
    return random.sample([x for x in range(lo,hi+1)],m)

def randTree(m=10,lo=-10,hi=10,w=0.2,uniq=False,randVal=False):
    """
    creates random binary tree
    :param m: size of tree including "null"s
    :param lo: low end of range    
    :param hi: high end of range (inclusive)
    :param w: expands [lo, hi] by (hi-lo)*w extra elements for sampling, which correspond to "null"s
    :param uniq: unique values or not
    :param randVal: whether to return a random value from the sampled tree
    :return: (vector of ints and "null"s, random value) if randVal else vector of ints and "null"s
    """
    while True:
        v=[random.randint(lo,hi)]+randVec(m-1,lo,hi+int((hi-lo)*w))
        j=99
        for i in range(m):
            if v[i]>hi:
                if i==j+1: v[i]=str(v[i]-(hi-lo))
                else:
                    v[i]="null"
                    j=i
            else: v[i]=str(v[i])
        if not uniq: break
        c=Counter(v)
        c.subtract({"null":c["null"]})
        if c.most_common(1)[0][1]==1: break
    if randVal:
        randV=random.choice(list(filter(lambda x:x!="null",v)))
    return ("["+','.join(v)+"]", randV) if randVal else "["+','.join(v)+"]"

def wrapStrVec(vec,w=False):
    """
    this wraps a n-dimensional vector of strings into a format leetcode expects
    e.g. ['hi', 'bye'] to ["hi", "bye"]
    """
    recurseWrap=wrapStrVec if isinstance(vec[0],list) else lambda x,w:wrap(str(x) ) if w else str(x)
    res="["
    for i in range(len(vec)): 
        res+=recurseWrap(vec[i],w=w)+","
    return res[:-1]+"]" 
    

def wrap(r):
    """
    used in wrapStrVec
    """
    return "\""+r+"\""

def rand2DVec(M=10,m=10,lo=-10,hi=10,s=False,uniq=False,uniqInner=False):
    """
    creates random 2d vector of integers
    :param M: size of 2d vector
    :param m: size of each vector
    :param lo: low end of range    
    :param hi: high end of range (inclusive)
    :param s: sort each vector or not
    :param uniq: unique vectors or not (e.g. [1,2,3] only appears once)
    :param uniqInner: unique elements in each vector or not like in randVec
    :return: random 2d vector
    """
    v=None
    if uniq:
        se=set()
        while len(se)<M: 
            lis=randVec(m,lo,hi) if not uniqInner else np.random.choice(range(lo,hi+1),m,replace=False).tolist()
            se.add(tuple(sorted(lis) if s else lis))
        
        v=list((list(x) for x in se))
        assert len(set([tuple(x) for x in v]))==len(v)
    else: v=[sorted(randVec(m,lo,hi)) if s else randVec(m,lo,hi) for _ in range(M)]
    return v 

def format2DVec(v):
    for j in range(len(v)):
        print(''.join([str(x) for x in v[j]]))


def randStr(m=10,lo='a',hi='z',add=[],w=1,boo=False):
    """
    creates random string
    :param m: size of string
    :param lo: low end of char range
    :param hi: high end of char range (inclusive)
    :param add: add set of extra chars to sample from
    :param w: make ratio of samples from added chars to [lo, hi] as len(add)*w : hi-lo
    :param boo: whether to wrap return string in double quotes for leetcode compatibility
    :return: random string
    """
    r=""
    for i in range(m):
        i=random.randint(ord(lo[0]),ord(hi[0])+int(w*len(add)))
        if i<=ord(hi[0]): r+=chr(i)
        else: r+=random.choice(add)
    if boo: return wrap(r)
    else: return r

class Intv:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __eq__(self,itv):
        return not (self.a>itv.b or itv.a>self.b)
    def __hash__(self):
        return self.a.__hash__()^self.b.__hash__()

def test():
    i=0
    while(i<1000): # change for how many test cases you want

        # make a test case here
        print(sorted(randVec(random.randint(1,100),-100,100,uniq=True)))


        i+=1
        
        





        
            
def checkAns(b=False):
    """
    infer how to use this
    basically you paste the test cases, send ctrl-d, followed by your output and given answers, then send ctrl-d again
    tells you which outputs are wrong and the corresponding test cases
    """
    
    cases=stdin.readlines()
    inp=stdin.readlines()
    out,ans=inp[:len(inp)//2],inp[len(inp)//2:]
    lpc=len(cases)//len(out)#lines per case
    for i in range(len(out)):
        if(out[i]!=ans[i]):
            print("input:")
            print(cases[lpc*i:lpc*i+lpc])
            print("output",i,"wrong:")
            print(out[i])
            print("ans is")
            print(ans[i])
    if b:
        print("The ones that are wrong are:")
        for i in range(len(out)):
            if(out[i]!=ans[i]):
                print(cases[i],end="")

test()
