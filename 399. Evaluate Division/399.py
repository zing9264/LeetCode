class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        anstable={}
        anslist=[]
        for i in range(len(equations)):
            anstable[equations[i][0]+'_#split#_'+equations[i][1]]=values[i]
            anstable[equations[i][1]+'_#split#_'+equations[i][0]]=1/values[i]

        cptable=anstable.copy()
        
        
        while (True):
            for keyA in cptable:
                cmpA=keyA.split("_#split#_")[1]
                for keyB in cptable:
                    cmpB=keyB.split("_#split#_")[0]
                    if(cmpA==cmpB):
                        anstable[keyA.split("_#split#_")[0]+'_#split#_'+keyB.split("_#split#_")[1]]=anstable[keyA]*anstable[keyB]
            if(len(cptable)==len(anstable)):
                break
            cptable=anstable.copy()

        for A in queries:
            ans=anstable.get(A[0]+'_#split#_'+A[1],-1.0)
            anslist.append(ans)
        return(anslist)
    