# Ruslan Gusakov
import datetime
stu = [{'name': "Anderson, Manuel",      'hw': 89,     'mid_exam': 92,     'fin_exam': 94,     'fin_grade': 0,     'ltr_grade': "X", },         {'name': "Thompson, Yani",      'hw': 63,     'mid_exam': 74,     'fin_exam': 59,     'fin_grade': 0,     'ltr_grade': "X"},              {'name': "Ortiz, Graciela",      'hw': 81,     'mid_exam': 76,
                                                                                                                                                                                                                                                                                           'fin_exam': 79,     'fin_grade': 0,     'ltr_grade': "X"},              {'name': "Wilson, Danielle",      'hw': 100,     'mid_exam': 89,     'fin_exam': 94,     'fin_grade': 0,     'ltr_grade': "X"},              {'name': "Thompson, Yani",      'hw': 63,     'mid_exam': 74,     'fin_exam': 59,     'fin_grade': 0,     'ltr_grade': "X"},]


student_file = "students.csv"
out_file = "stu_report.txt"


def main():
    filename = input("Enter the filename: ")
    stu = read_data_file(filename)
    stu, average = calculate_grades(stu, repfile)
    create_report_file(stu, average)

    stu = read_data_file()
    stu, average = calculate_grades(stu)
    create_report_file(stu, average)
    print("Class report created successfully!")


def read_data_file():
    with open("students.csv", "r") as file:
        data = []
        for line in file:
            values = line.strip().split(",")
            if len(values) < 6:
                # Skip lines that don't have enough values
                continue
            name, hw, mid_exam, fin_exam, fin_grade, ltr_grade = values
            data.append((name, int(hw), int(mid_exam), int(
                fin_exam), float(fin_grade), ltr_grade))
        return data


def calculate_grades(stu):
    totA=0
    totA = 0

    for student in stu:
        grades = student[1:]
        average = sum(grades) / len(grades)
        student.append(average)
        if average >= 90:
            totA += 1
    for s in stu:
        hw = float(s[1])
        mid_exam = float(s[2])
        fin_exam = float(s[3])
        fin_grade = round(0.4 * hw + 0.3 * mid_exam + 0.3 * fin_exam, 2)

        if fin_grade >= 90:
            ltr_grade = "A"
        elif fin_grade >= 80:
            ltr_grade = "B"
        elif fin_grade >= 70:
            ltr_grade = "C"
        elif fin_grade >= 60:
            ltr_grade = "D"
        else:
            ltr_grade = "F"
        s.append(fin_grade)
        s.append(ltr_grade)
    grades = [s[4] for s in stu]
    if len(grades) > 0:
        average = sum(grades) / len(grades)
    grades = []
    for i in range(1, len(stu)):
        grades.append(int(stu[i][2]))

    if len(grades) > 0:
        average = sum(grades) / len(grades)
    else:
        average = 0

    totA = 0
    for i in range(len(grades)):
        if grades[i] >= 90:
            totA += 1    
    if totA > 0:
        repfile.write("\nTotal number of A grades  : " + str(totA))
    else:
        repfile.write("\nNo A grades were earned.")
    return stu, average


def create_report_file(stu, average):
    with open("report.txt", "w") as repfile:
        repfile.write("Student report\n\n")
        repfile.write("\Average student grade      : " +
                      format(average, '5,.2f'))

        # calculate the number of A grades
        totA = sum(1 for grade in stu.values() if grade >= 90)

        # check if there are any A grades
        if totA > 0:
            repfile.write("\nTotal number of A grades  : " + str(totA))

        # calculate the number of B grades
        totB = sum(1 for grade in stu.values() if 80 <= grade < 90)
        repfile.write("\nTotal number of B grades  : " + str(totB))

        # calculate the number of C grades
        totC = sum(1 for grade in stu.values() if 70 <= grade < 80)
        repfile.write("\nTotal number of C grades  : " + str(totC))

        # calculate the number of D grades
        totD = sum(1 for grade in stu.values() if 60 <= grade < 70)
        repfile.write("\nTotal number of D grades  : " + str(totD))

        # calculate the number of F grades
        totF = sum(1 for grade in stu.values() if grade < 60)
        repfile.write("\nTotal number of F grades  : " + str(totF))

    repfile.write(line)
    repfile.write("\nName                    HW\tMID\tFIN\tFINAL GRADE")
    repfile.write(line)
    for i in range(len(stu)):
        sname = '{0:<18}'.format(stu[i][0]+', '+stu[i][1])
        hw = str(stu[i][2])
        midex = str(stu[i][3])
        finex = str(stu[i][4])
        fingrade = format(stu[i][5], '6,.2f')
        repfile.write("\n" + sname + "\t" + hw + "\t" + midex +
                      "\t" + finex + "\t" + fingrade + " "+stu[i][6])
    repfile.write(line)
    repfile.close()
    print("Open this file to view the Grades Report " + out_file)


main()
