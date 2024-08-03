travel_log=[
    {
        "country":"india",
        "visited":['mumbai','bangalore','kolkata'],
        "number_cities":24
    },
    {
        "country":"france",
        "visited":['paris','dijon','lille'],
        "number_cities":4
    },
]
def add(country,no,list):
    new_log={
        "country":country,
        "visited":list,
        "number_cities":no,
    }
    travel_log.append(new_log)
    print(travel_log)

add("russia",3,["moscow","saint row","peru"])
