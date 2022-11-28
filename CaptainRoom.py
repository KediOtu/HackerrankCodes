from collections import Counter
roomlist = input().split(" ")
cnt = Counter(roomlist)

for room in roomlist:
    if cnt[room]==1:
        print(room)

