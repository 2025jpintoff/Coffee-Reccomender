from coffee import coffees

print(coffees[0])

def recommend(temperature, size, strength, sweet, flavor, milk):
    recommendations = []
    for coffee in coffees:
        if temperature.lower() == coffee["temperature"].lower():
            if sweet.lower() == coffee["sweet"].lower():
                if (strength.lower() == "high" and coffee["strength"] >= 90) or (strength.lower() == "low" and coffee["strength"] < 90):
                    if (milk.lower() == "yes" and coffee["milk"].lower() == "yes") or (milk.lower() == "no" and coffee["milk"].lower() == "no"):
                        recommendations.append(coffee)
    return recommendations

# from  coffee import coffees
# print(coffees[0])
        
# def recommend(temperature, size, strength, sweet, flavor, milk):
#     recommendations = []
#     for coffee in coffees:
#         if temperature.lower() == coffee["temperature"].lower():
#             if sweet.lower() == coffee["sweet"].lower():
#                if strength.lower() == "high" and coffee["strength"] >= 90:
#                 if (milk and coffee["milk"]) or (not milk and not coffee["milk"]):
#                     recommendations.append(coffee)
#             elif strength.lower() == "low" and coffee["strength"] < 90:
#                 if (milk and coffee["milk"]) or (not milk and not coffee["milk"]):
#                     recommendations.append(coffee)
#     return recommendations

# print(reccomend("Hot", 0, 0, 0, 0, 0))