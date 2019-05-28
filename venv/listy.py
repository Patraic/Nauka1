brand = ['BMW', 'Peugeot', 'Opel']
color = ['srebrny', 'niebieski', 'zielony', 'czarny', 'czerwony']
vintage = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
def mix():
    brand_start = 0
    max_brand= len(brand) - 1
    color_start = 0
    max_color= len(color) - 1
    vintage_start = 0
    max_vintage = len(vintage) - 1
    total_list = {}
    n=0
    while brand_start <= max_brand:
        color_start = 0
        while color_start <= max_color:
            vintage_start = 0
            while vintage_start <= max_vintage:
                total_list['car_%s' %(n)] = brand[brand_start], color[color_start], vintage[vintage_start]
                n+=1
                vintage_start += 1
            color_start+=1
        brand_start += 1
    for i in total_list:
        print(f"Index: {i} | Content: {total_list[i]}")
mix()