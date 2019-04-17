# name = input("What is your name ? ")
# #favColor = input("What is your favourite color ? ")
# #print(name +" likes "+ favColor)
#
# #1 lb = 0.45359237 kg
# weight_kg = input("What is your weight in KG ? ")
# weight_lb = int(weight_kg) * 0.4535
# print(f" {name.upper()}! Your weight in LB is %d "%weight_lb)
# name = name.title()
# print(f"{name} name.find(a) ::")
#
# if name.__contains__("T"):
#     print(f" {name}! Your name has 'T' ")
# elif int(weight_kg) > 100 or (name.find("a") != -1 and name.find("a") > 2) :
#     print(f"{name}! Your name does not have 'T'")
# else:
#     print(True)


print(max(range(1, 10, 2)))
list_x = []
for x in range(1,100,2):
    list_x.append(x)
list_x.insert(len(list_x)+1, 2000)
print(list_x)

