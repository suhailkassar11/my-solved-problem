class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cout=0
        i=0
        n=len(people)
        j=n-1
        people.sort()
        while i<=j:
            sum1=people[i]+people[j]
            if sum1>limit:
                j-=1
                cout+=1
            else:
                i+=1
                j-=1
                cout+=1
        return cout
        