def city_country(city, country, population = ''):
    """return a string containing city and country names"""
    if population:
        result = f'{city.title()}, {country.title()} - population {population}'
        return result
    else:
        result = f'{city.title()}, {country.title()}'
        return result