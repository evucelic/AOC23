input_path = "input.txt"

with open(input_path, "r") as file:
    time = file.readline().split(":")[1].strip().split()
    distance = file.readline().split(":")[1].strip().split()

time = [int(num) for num in time]
distance = [int(dist) for dist in distance]

print(time, distance)

values = [0]*len(time)
print(values)

for n,t in enumerate(time):
    for i in range(t+1):
        if i*(t-i) > distance[n]:
            values[n] += 1

print(values)
product = 1
for k in values:
    product*=k

print(product)    