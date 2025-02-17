scores = {"Class B": [96, 76, 98], "Class C": [60, 90]}

def calculate_class_average(score_dict):
    return {class_name: int(sum(marks)/ len(marks)) for class_name,marks in score_dict.items()}

avergs=calculate_class_average(scores)
print(avergs)
