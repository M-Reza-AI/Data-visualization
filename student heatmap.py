from Helper.AI_Helper import *


student_hp = Get_Dataset("jayaantanaath/student-habits-vs-academic-performance",
                         "student_habits_performance.csv")


# shows a heatmap of the dataset
temp = sns.heatmap(student_hp.corr(numeric_only=True), cmap='YlGnBu', linewidths=.5 )

# shows the compact heatmap with all the column names visible
temp.figure.tight_layout()
plt.show()