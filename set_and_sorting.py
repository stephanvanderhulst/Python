#sets and sorting
def cars_count(dic):
    colors = list(dic.values())
    for color in set(colors):
        count = colors.count(color)
        print(f"you have {count} cars with color {color}")

cars = {
    "golf":"red",
    "clio":"red",
    "r25":"white",
    "bmw":"black",
    "evok":"white",
    "maruti":"red"
}
cars_count(cars)

