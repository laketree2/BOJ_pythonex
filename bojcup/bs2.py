meme = ["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

answer = "No"

for i in range(int(input())):
    n_list = input()
    if n_list not in meme:
        answer = 'Yes'
print(answer)
