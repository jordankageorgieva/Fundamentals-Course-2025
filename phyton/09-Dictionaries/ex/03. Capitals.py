country_names = input().split(", ")
capital_cities = input().split(", ")
match = dict(zip(country_names, capital_cities))
print("\n".join([key + " -> "+ str(value) for key, value in match.items()]))