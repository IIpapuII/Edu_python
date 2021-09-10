def run():
    my_list = [1,"hello",True,4.5]
    my_dict ={"firstname":"Wilmer","lastname":"serrano"}

    super_list= [
        {"firstname":"Wilmer","lastname":"serrano"},
        {"firstname":"Daniel","lastname":"Fernando"},
        {"firstname":"Carlos","lastname":"Ramirez"},
        {"firstname":"Diego","lastname":"Herrera"},
        {"firstname":"Carlos","lastname":"Fernando"},
        {"firstname":"Maria","lastname":"ortega"}
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5,6],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.2,4.5,6.43]
    }

    for key,value in super_dict.items():
        print(key, "-", value)
if __name__ == '__main__':
    run()