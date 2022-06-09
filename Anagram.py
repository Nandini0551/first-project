D1={}
D2={}
def anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        elementNumber = 0
        for char in s1:                    
            D1[elementNumber] = char
            elementNumber = elementNumber + 1
        elementNumber = 0
        for char in s2:                   
            elementNumber = elementNumber + 1

        print(sorted(D1.values()))         
        print(sorted(D2.values()))         
        if sorted(D1.values())==sorted(D2.values()): 
             return True
        else:
             return False

print("Anagrams: "+str(anagrams("Hello", "oHlel")))
print("Anagrams: "+str(anagrams("Hello", "xyzlo"))) 


