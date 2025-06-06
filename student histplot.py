from Helper.AI_Helper import *


student_hp = Get_Dataset("jayaantanaath/student-habits-vs-academic-performance",
                         "student_habits_performance.csv")

# hue is best used with different string values
# kde is a way to see what the probability of a score to occur given a gender
sns.histplot(student_hp,x="exam_score" , hue="gender", multiple="stack" , kde=True)
plt.show()
#you can also convert the histplot to a heatmap by supplying 2 numerical variables on both axis
# cbar shows the max density possible (aka the max number of students in with the given characteristics)
sns.histplot(student_hp,x="exam_score" , y="study_hours_per_day", cbar=True )
plt.show()