string = input("Input your string: ")

print("=" * 25)

for i in range(1, len(string)+1):
    for j in range(len(string)-i+1):
        print(string[j:j+i])
