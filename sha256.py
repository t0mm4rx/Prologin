import hashlib, string

print('Brute forcing sha256')
hashes = [
  [88, 21, 124, 196, 146, 49, 119, 33, 236, 141, 215, 52, 175, 46, 216, 250,
      44, 240, 8, 8, 90, 0, 178, 146, 232, 194, 180, 161, 61, 230, 163, 255],
  [39, 102, 165, 69, 101, 60, 62, 150, 101, 12, 27, 191, 238, 69, 125, 79,
      241, 23, 112, 234, 181, 246, 191, 79, 32, 138, 116, 54, 194, 64, 181, 13],
  [42, 100, 127, 92, 224, 26, 85, 32, 25, 25, 175, 195, 247, 146, 142, 225,
      44, 215, 146, 207, 44, 20, 181, 36, 105, 149, 27, 183, 156, 172, 201, 197],
  [139, 49, 171, 172, 18, 150, 234, 124, 82, 58, 200, 132, 46, 48, 91, 185, 120,
      142, 181, 107, 160, 145, 196, 246, 80, 171, 162, 156, 199, 69, 229, 116],
  [5, 58, 156, 201, 121, 208, 217, 118, 108, 51, 134, 193, 100, 26, 59, 84,
      131, 52, 41, 1, 17, 138, 227, 127, 198, 51, 174, 102, 125, 174, 213, 98],
  [221, 205, 219, 228, 67, 77, 174, 36, 90, 229, 32, 193, 244, 86, 4, 3, 176,
      132, 32, 202, 181, 73, 146, 86, 110, 146, 201, 55, 79, 147, 68, 129],
  [164, 212, 163, 137, 35, 147, 158, 126, 217, 155, 195, 248, 174, 132, 69, 154,
      109, 232, 144, 39, 43, 127, 222, 250, 210, 35, 30, 44, 101, 249, 47, 11],
  [228, 254, 179, 209, 39, 106, 188, 0, 51, 200, 153, 56, 251, 226, 156, 254,
      197, 140, 91, 174, 75, 15, 140, 55, 144, 209, 182, 184, 178, 121, 86, 229],
  [245, 164, 120, 25, 122, 83, 237, 103, 238, 86, 38, 11, 227, 90, 87, 5, 206,
      190, 43, 251, 208, 140, 111, 210, 88, 62, 145, 243, 218, 207, 57, 230]]

chars = string.ascii_lowercase
chars = chars + string.ascii_uppercase
chars = chars + string.digits

def test(str, target):
    m = hashlib.sha256()
    m.update(str.encode('ascii'))
    res = m.hexdigest()
    res_arr = []
    for i in range(int(len(res) / 2)):
        res_arr.append(int('0x' + res[i * 2:i*2 + 2], 16))
    return res_arr == target

str = 'Le flag est : 8v0F3G6lTgx7SFe8fWr3'

total = len(chars) * len(chars) * len(chars) * len(chars)
current = 0

for i in chars:
    for j in chars:
        #for k in chars:
            #for l in chars:
        current += 1
        a = i + j + chr(0) + chr(0)
        if (test(a, hashes[8])):
            print('-- Found ! -- Value:', a)
            exit()
            break
        else:
            print(round(current / total * 100, 4), "%", " --", a)
