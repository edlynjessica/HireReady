import pandas as pd
import random

students = []

for i in range(1000):

    cgpa = round(random.uniform(6, 10), 2)

    lc_easy = random.randint(0, 500)
    lc_medium = random.randint(0, 300)
    lc_hard = random.randint(0, 80)

    contest_rating = random.randint(0, 2500)

    projects = random.randint(0, 5)

    internships = random.randint(0, 4)

    communication = random.randint(1, 10)

# normalize the values to a score out of 100

    score = (
        (cgpa/10) * 20
        + (lc_easy/500) * 8
        + (lc_medium/300) * 12
        + (lc_hard/80) * 15
        + (contest_rating/2500) * 10
        + (projects/5) * 15
        + (internships/4) * 15
        + (communication/10) * 5
    )

    score = min(100, round(score, 2))

    students.append({
        "cgpa": cgpa,
        "lc_easy": lc_easy,
        "lc_medium": lc_medium,
        "lc_hard": lc_hard,
        "contest_rating": contest_rating,
        "projects": projects,
        "internships": internships,
        "communication": communication,
        "hire_ready_score": score
    })

df = pd.DataFrame(students)

df.to_csv("synthetic_students.csv",index=False)

print("Dataset generated successfully!")
