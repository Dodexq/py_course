def main():
    grades = {}
    grades["English"] = int(input("English grade is: "))
    grades["Math"] = int(input("Math grade is: "))
    grades["Global Studies"] = int(input("Global Studies grade is: "))
    grades["Art"] = int(input("Art grade is: "))
    grades["Music"] = int(input("Music grade is: "))
    grades_values = grades.values()
    av_grades = sum(grades_values) / len(grades)
    print("Average grade is", av_grades)

    re_grades_subj = input("Choose subj to re_grade: ")
    new_grades = input(f"What is your new  {re_grades_subj} grade? ")
    grades[re_grades_subj] = int(new_grades)
    av_grades = sum(grades_values) / len(grades)
    print("NEW Average grade is", av_grades)

main()