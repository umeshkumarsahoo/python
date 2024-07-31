one=input("write your name:").lower()
two=input("write your bf/gf name:").lower()
name=one+two
love=name.count("l")+name.count("o")+name.count("v")+name.count("e")
true=name.count("t")+name.count("u")+name.count("r")+name.count("e")
percentage=int(str(love)+str(true))
if percentage<50:
    print(f"love more\npercentage is {percentage}")
elif percentage<90:
    print(f"nice keep going\npercentage is {percentage}")
else:
    print(f"nice work keep it up\n percentage is 🤨{percentage}")