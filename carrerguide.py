developer_type = input("Which type of developer do you want to become? (App, Web, Data Science, Cyber Security)")

if developer_type.lower() == "app":
    app_type = input("Which type of app developer do you want to become? (Native, Hybrid)")
    if app_type.lower() == "native":
        print("You can learn Java or Swift.")
    elif app_type.lower() == "hybrid":
        print("You can learn Flutter or React Native.")
    else:
        print("Invalid input.")
elif developer_type.lower() == "web":
    web_type = input("Which type of web developer do you want to become? (Frontend, Backend)")
    if web_type.lower() == "frontend":
        print("You can learn HTML & CSS and Javascript.")
    elif web_type.lower() == "backend":
        print("You can learn Python, Javascript, Ruby, or Java.")
    else:
        print("Invalid input.")
elif developer_type.lower() == "data science":
    print("You can learn Python.")
elif developer_type.lower() == "cyber security":
    print("You can learn Networking.")
else:
    print("Invalid input.")
