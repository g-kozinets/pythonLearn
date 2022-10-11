
my_str = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
splited_list = my_str.split(" ")
my_list = [x for x in splited_list if "y" in x.lower()[0]]

print(my_list)
