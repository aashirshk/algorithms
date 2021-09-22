def gradingStudent(grades):
    final_grade = []
    for grade in grades:
        if grade >= 38:
            if (grade % 5) > 2:
                grade += (5 - (grade % 5))
        final_grade.append(grade)
    return final_grade 

    


if __name__ == "__main__":
    grades = [73, 67, 38, 33]
    res = gradingStudent(grades)

    print(res)
