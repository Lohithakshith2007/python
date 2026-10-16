def build_profile(name,*skills,**details):
    return {
        "name": name,
        "skills": skills,
        "details": details
    }


profile = build_profile(
    "Lohith",
    "Python",
    "React",
    "Django",
    age=20,
    goal="Full Stack Developer"
)

print(profile)