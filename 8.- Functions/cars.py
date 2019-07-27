def make_car(brad, model, **more_info):
    car = {}

    car['brad'] = brad
    car['model'] = model

    for key, value in more_info.items():
        car[key] = value
    
    return car

car = make_car('SEAT', 'IBIZA', color='negro', doors=4)
print(car)