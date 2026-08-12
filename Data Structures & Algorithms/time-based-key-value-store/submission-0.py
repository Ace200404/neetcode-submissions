class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key]=[]
        self.dict[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res=''
        values=self.dict.get(key,[])
        left=0
        right=len(values)-1
        while left<=right:
            m=(left+right)//2
            if values[m][1]<=timestamp:
                res=values[m][0]
                left=m+1
            else:
                right=m-1
        return res
