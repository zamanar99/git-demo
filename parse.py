

with open("readfile.txt", mode="r") as r_file:
    all_words = []
    for line in r_file.readlines():
        words = line.strip().split(" ")
        all_words += words
        unique_words = set(all_words)
    print(unique_words)

with open("writefile.txt", mode='w') as w_file:
    for item in sorted(unique_words):
        w_file.write(item)
        w_file.write(" ")

print("Finished")