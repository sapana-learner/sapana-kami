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

print("\nTechnical Skills")
print("----------------")

for skill in skills:
    print(f"- {skill}")
