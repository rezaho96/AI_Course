import operator
str = """
Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble.
He changed our ideas about the universe and how it developed.
Edwin hubble made his most important discoveries in the nineteen twenties. Today, other
astronomers continue the work he began. Many of them are using the Hubble space
telescope that is named after him.
Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early
years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He
attended the University of Chicago. He studied mathematics and astronomy.
"""
str1="Edwin"
str2="Hubble"
list1=str.split(".")

for sentance in list1:
    list2=sentance.split()
    check_str=False
    for item in list2:
        if operator.contains(item.lower(),str1.lower()):
            check_str=True
        elif operator.contains(item.lower(),str2.lower()):
            check_str=True
    if check_str==True:
        # Sentences containing the special name "Edwin Hubble"
        print(sentance+".",end="/")
print("\n***********************************")
list_sentance=[]

for sentance in list1:
    list2=sentance.split()
    check_str=False
    idx_list=-1
    for item in list2:
        idx_list+=1
        if operator.contains(item.lower(),str1.lower()):
            check_str=True
            list2[idx_list]=str1
            
        elif operator.contains(item.lower(),str2.lower()):
            check_str=True
            list2[idx_list]=str2
    sent2=" ".join(list2)  
    list_sentance.append(sent2)
# Corrected text      
print(".".join(list_sentance))    



    

