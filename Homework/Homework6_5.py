import operator,itertools

expert_List1 = [("Ali","Ahmadi","M",35), ("Sima","Sadri","C",39),
("Ahmad","Moradi","M",30), ("Ftemeh","Majd","C",29), ("Sara","Biglar","IE",27),
("Reza","Rahnama","EE",45)]
expert_List2 = [("Mina","Gohari","EE",40), ("Iman","Shams","M",26),
("Farzad","Yeganeh","M",41), ("Ali","Imani","C",33), ("Aref","Alameh","M",32),
("Narges","Sohrabi","C",35)]
# Combination of lists
expert_list3=list(itertools.chain.from_iterable([expert_List1,expert_List2]))
#Sort by field of study
sorted_list=sorted(expert_list3,key=operator.itemgetter(2))
print(sorted_list)
print("********************************")
# Separating the math expert
expert_math=list(itertools.islice(sorted_list,7,12,1))
# Forming groups of three
group_list=list(itertools.combinations(expert_math,3))
for item in group_list:
    print(item)