
my_str = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
splited_list = my_str.split(" ")
my_list = list(x for x in splited_list if x.__contains__("Y") or x.__contains__("y"))

print(my_list)
