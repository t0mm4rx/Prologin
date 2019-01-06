import os
import string
import time

chars = string.printable
def get_data(file):
    output = []
    with open(file, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            # Do stuff with byte.
            byte = f.read(1)
            output.append(byte)
    return output

def generate_output(input):
    file_from = open('data.txt', 'w+')
    file_from.write(input)
    file_from.close()
    os.system('python3 ctf3_backup.py 4 3 5 7 2 1 0 6 < data.txt > output.txt')
    time.sleep(0.001)
    return get_data('output.txt')

target = get_data('ctf3_output.txt')

print("Target", target)

res = [''] * (len(target) - 1)
index = 0

while (index < len(res)):
    for c in chars:
        test = "$" + ''.join(res) + c
        o = generate_output(test)
        print(test)
        if (o[index] == target[index]):
            #print('Found !')
            res[index] = c
            index += 1

print(generate_output("$" + ''.join(res)))
print(target)
# ery_crypto_such_wow
