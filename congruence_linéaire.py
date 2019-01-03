a = 1337
c = 404
m = 1000
seed = 42

x = seed
for i in range(303):
    x = (a * x + c) % m

print (x)
