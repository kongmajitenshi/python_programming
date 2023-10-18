def calculate_average_from_dict(dict1) :   
    avg = sum(dict1.values()) / len(dict1)
    return avg

student_scores = {"김인하": 92, "이인하": 85, "박인하": 78}
avg_score = calculate_average_from_dict(student_scores)
print(f"평균 점수: {avg_score:.2f}")