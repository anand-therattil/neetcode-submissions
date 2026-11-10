class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        key_list = self.hm[key]

        low = 0 
        high = len(key_list)-1
        ans = ""
        while low<=high:
            mid = (low+high)//2
            if key_list[mid][0]<=timestamp:
                ans = key_list[mid][1]
                low = mid+1
            elif key_list[mid][0]>timestamp:
                high = mid-1
        return ans
