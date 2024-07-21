def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "adriám",
    "surname",
    location="logroño",
    field="developer",
    favorite_color="orange",
    age=25,
    isCool=True,
)

print(user_profile)
