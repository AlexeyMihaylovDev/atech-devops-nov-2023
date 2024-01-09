def best_student(grades):
    
    maxgrade= list(grades.values())[0]
    for name, grade in grades.items():
        if grade > maxgrade:
            maxgrade = grade
            result = name

    return  result 

print('\nbest_student:\n--------------------')
print(best_student({
    "Ben": 78,
    "Hen": 88,
    "Natan": 99,
    "Efraim": 65,
    "Rachel": 95
    }))
    