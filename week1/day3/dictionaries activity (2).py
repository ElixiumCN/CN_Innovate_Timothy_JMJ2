countries = {
    "countries": {
        "unitedkingdom":"london",
        "france":"paris",
        "germany":"berlin",
        "spain":"madrid",
        "italy":"rome"

        },
    "example": {
        "lorem":"ipsum",
    }
}

countries.setdefault("switzerland","bern")
countries.setdefault("canada","ottawa")


countries["unitedkingdom"] = "english"
countries["france"] = "french"
countries["germany"] = "german"
countries["spain"] = "spanish"
countries["italy"] = "italian"
countries["switzerland"] = "german"
countries["canada"] = "english"


# for x in countries.items():
#     print(x)
# for y in countries.keys():
#     print(y)
for z in countries.values():
    print(z)

    # Update all the values with the main language spoken in the countries instead of capitals

# countries.setdefault("unkitedkingdom","english") can't use this

