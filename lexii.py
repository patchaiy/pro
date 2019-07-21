bri=input()
for i in range(1,len(bri)):
    if ord(bri[i])>ord(bri[0]):
        ans=bri[i:]
        break
print(ans)
