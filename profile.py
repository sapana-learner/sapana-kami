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
