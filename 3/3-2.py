number=int(input("your num: "))

ascending = int("".join(sorted(str(number)))) #3rd sort digits

mult=1
rnum=0
while number != 0:
    mult*=number%10 #1st task
    rnum=rnum*10+number%10 #2nd
    number=number//10
print(f"mult: {mult}, reverse: {rnum}, sorted: {ascending}")
