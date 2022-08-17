class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",
           'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",
           'm':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",
           'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        s1=[]
        for i in words:
            s=""
            for j in i:
                s+=d[j]
            s1.append(s)
        s2=set(s1)
        return len(s2)
                
                                                                