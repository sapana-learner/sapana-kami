student = {
    "name": "Sapana Kami",
    "degree": "B.Tech in Computer Science and Engineering (AI & Machine Learning)",
    "university": "REVA University",
    "graduation": 2029,
    "interests": [
        "Artificial Intelligence",
        "Machine Learning",
        "Python",
        "Software Development"
    ]
}

print("Student Profile")
print("----------------")

for key, value in student.items():
    print(f"{key.title()}: {value}")

skills = [
    "Python",
    "C",
    "Git and GitHub",
    "Problem Solving",
    "Machine Learning",
    "Artificial Intelligence",
    "HTML",
    "Communication Skills",
    "Time Management"
]

goals = [
    "Build practical AI and ML projects",
    "Strengthen programming fundamentals",
    "Contribute to collaborative projects",
    "Develop a strong professional portfolio"
]

print("\nCurrent Goals")
print("------------")

for goal in goals:
    print(f"- {goal}")

print("\nTechnical Skills")
print("----------------")

for skill in skills:
    print(f"- {skill}")
