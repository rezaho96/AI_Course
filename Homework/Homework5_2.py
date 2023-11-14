def kilometer_conversion_to_hectares(kilometer):
    return kilometer*100

def population_density_per_hectare(city_population,city_area):
    return city_population//city_area

def show_population_density(pop_list,area_list,city_list):
    area_hectares_list=[kilometer_conversion_to_hectares(k) for k in area_list]
    densiy_list=[population_density_per_hectare(p,a) for p,a in zip(pop_list,area_hectares_list)]
    print("List of cities by population density")
    print("------------------------------------")
    for city,dencity in zip(city_List,densiy_list):
        print(f"{city}\t{dencity}")
    print("*************************************")
    print("List of high-Density cities")
    print("------------------------------------")
    for city,dencity in zip(city_List,densiy_list):
        if dencity >= 50:
           print(f"{city}\t{dencity}")
   
city_List = ["city1","city2","city3","city4","city5","city6"]
population_List = [300000, 1000000, 3800000, 500000, 1900000, 100000]
area_List_squarekilometer = [100, 200, 500, 150, 300, 100]    
    
show_population_density(population_List,area_List_squarekilometer,city_List)

