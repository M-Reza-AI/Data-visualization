from Helper.AI_Helper import *


student_hp = Get_Dataset("jayaantanaath/student-habits-vs-academic-performance",
                         "student_habits_performance.csv")

# to see what the pair plot looks like
sns.pairplot(student_hp)

# to see a pair plot of a specific bunch of variables, use x_vars and y_vars with the name of the columns you want

sns.pairplot(student_hp,
           x_vars=["exam_score"],
           y_vars=["study_hours_per_day"])

sns.pairplot(student_hp,
             x_vars=["exam_score"],
             y_vars=["attendance_percentage"])

sns.pairplot(student_hp,
             x_vars=["exam_score"],
             y_vars=["sleep_hours"])

plt.show()