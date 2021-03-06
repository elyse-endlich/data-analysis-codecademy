# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatan Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatan Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatan Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:

def update_damages(list_of_damages):
    """Convert string to float and return damages as list"""

    conversion = {"M": 1000000, "B": 1000000000}
    updated_damages_list = []
    for record in list_of_damages:
        if record == "Damages not recorded":
            updated_damages_list.append(record)
        if record[-1] == 'M':
            updated_damages_list.append(float(record.strip('M')) * conversion['M'])
        if record[-1] == 'B':
            updated_damages_list.append(float(record.strip('B')) * conversion['B'])
    return updated_damages_list


updated_damages = update_damages(damages)


# print(updated_damages)


# write your construct hurricane dictionary function here:

def create_dict(names_list, months_list, years_list, max_sustained_winds_list, areas_affected_list,
                updated_damages_list, deaths_list):
    """Create dictionary from lists of hurricane information"""
    hurricanes_dict = {}
    num_hurricanes = len(names_list)
    for i in range(num_hurricanes):
        hurricanes_dict[names_list[i]] = {"Name": names_list[i], "Month": months_list[i], "Year": years_list[i],
                                          "Max Sustained Wind": max_sustained_winds_list[i],
                                          "Areas Affected": areas_affected_list[i],
                                          "Damage": updated_damages_list[i],
                                          "Deaths": deaths_list[i]}
    return hurricanes_dict


hurricanes = create_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# print(hurricanes)


# write your construct hurricane by year dictionary function here:
def create_dict_by_year(hurricanes_dict):
    """Create dictionary where hurricanes are organized by year"""
    hurricanes_by_year_dict = {}
    for hurricane in hurricanes_dict:
        current_year = hurricanes_dict[hurricane]['Year']
        current_hurricane = hurricanes_dict[hurricane]
        if current_year not in hurricanes_by_year_dict:
            hurricanes_by_year_dict[current_year] = [current_hurricane]
        else:
            hurricanes_by_year_dict[current_year].append(current_hurricane)
    return hurricanes_by_year_dict


hurricanes_by_year = create_dict_by_year(hurricanes)


# print(hurricanes_by_year)


# write your count affected areas function here:

def affected_areas(hurricanes_dict):
    """Create dictionary showing how many times each area of the world has been affected"""
    affected_areas_dict = {}
    for hurricane in hurricanes_dict:
        for area in hurricanes_dict[hurricane]['Areas Affected']:
            if area not in affected_areas_dict:
                affected_areas_dict[area] = 1
            else:
                affected_areas_dict[area] += 1
    return affected_areas_dict


affected_areas = affected_areas(hurricanes)


# print(affected_areas)


# write your find most affected area function here:

def most_affected_area(affected_areas_dict):
    """Finds most impacted area in the hurricanes dictionary"""
    most_affected_area_name = ''
    max_count = 0
    for area in affected_areas_dict:
        if affected_areas_dict[area] > max_count:
            most_affected_area_name = area
            max_count = affected_areas_dict[area]
    return most_affected_area_name, max_count


max_area, max_area_count = most_affected_area(affected_areas)


# print(max_area, max_area_count)


# write your greatest number of deaths function here:

def most_deaths(hurricanes_dict):
    """Finds hurricane with most deaths in hurricane dictionary"""
    max_hurricane_name = ''
    max_count = 0
    for hurricane in hurricanes_dict:
        if hurricanes_dict[hurricane]['Deaths'] > max_count:
            max_hurricane_name = hurricane
            max_count = hurricanes_dict[hurricane]['Deaths']
    return max_hurricane_name, max_count


max_hurricane, max_death_count = most_deaths(hurricanes)


# print(max_hurricane, max_death_count)


# write your categorize by mortality function here:

def mortality_scale(hurricanes_dict):
    """Sorts hurricanes into scale by number of deaths recorded"""
    mortality_scale_dict = {0: 0,
                            1: 100,
                            2: 500,
                            3: 1000,
                            4: 10000}
    hurricanes_by_mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes_dict:
        num_deaths = hurricanes_dict[hurricane]['Deaths']
        if num_deaths == mortality_scale_dict[0]:
            hurricanes_by_mortality_dict[0].append(hurricanes_dict[hurricane])
        elif mortality_scale_dict[0] < num_deaths <= mortality_scale_dict[1]:
            hurricanes_by_mortality_dict[1].append(hurricanes_dict[hurricane])
        elif mortality_scale_dict[1] < num_deaths <= mortality_scale_dict[2]:
            hurricanes_by_mortality_dict[2].append(hurricanes_dict[hurricane])
        elif mortality_scale_dict[2] < num_deaths <= mortality_scale_dict[3]:
            hurricanes_by_mortality_dict[3].append(hurricanes_dict[hurricane])
        elif mortality_scale_dict[3] < num_deaths <= mortality_scale_dict[4]:
            hurricanes_by_mortality_dict[4].append(hurricanes_dict[hurricane])
        elif mortality_scale_dict[4] < num_deaths:
            hurricanes_by_mortality_dict[5].append(hurricanes_dict[hurricane])
    return hurricanes_by_mortality_dict


hurricanes_by_mortality = mortality_scale(hurricanes)


# print(hurricanes_by_mortality)

# write your greatest damage function here:

def max_damage(hurricanes_dict):
    """Finds hurricane that caused the most damage in a hurricanes dictionary"""
    max_hurricane_name = ''
    max_damage_total = 0
    for hurricane in hurricanes_dict:
        if hurricanes_dict[hurricane]['Damage'] == 'Damages not recorded':
            pass
        elif int(hurricanes_dict[hurricane]['Damage']) > max_damage_total:
            max_hurricane_name = hurricane
            max_damage_total = int(hurricanes_dict[hurricane]['Damage'])
    return max_hurricane_name, max_damage_total


max_hurricane_damages, max_damage = max_damage(hurricanes)


# print(max_hurricane_damages, max_damage)

# write your categorize by damage function here:

def damage_scale(hurricanes_dict):
    """Sorts hurricanes by total damage caused"""
    damage_scale_dict = {0: 0,
                         1: 100000000,
                         2: 1000000000,
                         3: 10000000000,
                         4: 50000000000}
    hurricanes_by_damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes_dict:
        hurricane_damage = hurricanes_dict[hurricane]['Damage']
        if hurricane_damage == "Damages not recorded":
            hurricanes_by_damage_dict[0].append(hurricanes_dict[hurricane])
        elif hurricane_damage == damage_scale_dict[0]:
            hurricanes_by_damage_dict[0].append(hurricanes_dict[hurricane])
        elif damage_scale_dict[0] < hurricane_damage <= damage_scale_dict[1]:
            hurricanes_by_damage_dict[1].append(hurricanes_dict[hurricane])
        elif damage_scale_dict[1] < hurricane_damage <= damage_scale_dict[2]:
            hurricanes_by_damage_dict[2].append(hurricanes_dict[hurricane])
        elif damage_scale_dict[2] < hurricane_damage <= damage_scale_dict[3]:
            hurricanes_by_damage_dict[3].append(hurricanes_dict[hurricane])
        elif damage_scale_dict[3] < hurricane_damage <= damage_scale_dict[4]:
            hurricanes_by_damage_dict[4].append(hurricanes_dict[hurricane])
        elif damage_scale_dict[4] < hurricane_damage:
            hurricanes_by_damage_dict[5].append(hurricanes_dict[hurricane])
    return hurricanes_by_damage_dict


hurricanes_by_damage = damage_scale(hurricanes)
# print(hurricanes_by_damage)
