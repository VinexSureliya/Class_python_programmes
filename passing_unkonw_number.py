#passing unkonw numbers of argument
#Arbitrary arguments

def my_sum(* numbers):
    tot = 0
    for i in numbers:
        tot += 1
    return tot

ans = my_sum()
print(ans)
ans = my_sum(1)
print(ans)
ans = my_sum(1,2,3,4,5,6,7,8,9,10)
print(ans)