from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#api = KaggleApi()
#api.authenticate()

# the dataset used in this lecture
#api.dataset_download_file("jayaantanaath/student-habits-vs-academic-performance"
#                          , "student_habits_performance.csv")

student_hp = pd.read_csv("student_habits_performance.csv")

# First we need to know what the dataset looks like
# print(student_hp)

# or you can use this too , you can change how many rows you want to see (5 is default)
# print(student_hp.head())

# you can also use [ student_hp.tail() ] to get the last elements

# to see general information about the dataset (existent datatypes, null values and names of columns)
#print(student_hp.info())

# you can also ask for specific parts of the dataset
print(student_hp.columns)

# to see what the pair plot looks like
#sns.pairplot(student_hp)

# to see a pair plot of a specific bunch of variables use x_vars and y_vars with the name of the columns you want

#sns.pairplot(student_hp,
#            x_vars=["exam_score"],
#            y_vars=["study_hours_per_day","attendance_percentage", "sleep_hours","exercise_frequency","mental_health_rating"])

# shows a heatmap of the dataset
#temp = sns.heatmap(student_hp.corr(numeric_only=True), cmap='YlGnBu', linewidths=.5 )

# shows the compact heatmap with all the column names visible
#temp.figure.tight_layout()

# hue is best used with different string values
# kde is a way to see what the probability of a score to occur given a gender
#sns.histplot(student_hp,x="exam_score" , hue="gender", multiple="stack" , kde=True)

#you can also convert the histplot to a heatmap by supplying 2 numerical variables on both axis
# cbar shows the max density possible (aka the max number of students in with the given characteristics)
#sns.histplot(student_hp,x="exam_score" , y="mental_health_rating", cbar=True )
plt.show()