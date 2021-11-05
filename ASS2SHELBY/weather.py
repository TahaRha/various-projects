sensorTemps = ""
list_of_temps = []
while (sensorTemps != "stop"):
    sensorTemps = ""
    sensorTemps = input("Enter readings: ")
    if sensorTemps != "stop":
        list_of_temps += sensorTemps.split()

new_list = []

for i in list_of_temps:
    if (float(i)<50 and float(i)>-50):
        new_list.append(i)

list_of_temps = new_list

sum_temps = 0
for i in list_of_temps:
    list_of_temps[list_of_temps.index(i)]=float(i)
    i = float(i)
    sum_temps += i

avg_temp = round((sum_temps/len(list_of_temps)), 1)

list_of_temps.sort()
min_temps = list_of_temps[0:3]
list_of_temps.sort(reverse=True)
max_temps = list_of_temps[0:3]
print("Average temperature:" + str(avg_temp))
print("Min 3 temperatures:")
for i in min_temps:
    print(i)
print("Max 3 temperatures:")
for i in max_temps:
    print(i)

