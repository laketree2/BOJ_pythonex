# import sys
# sys.stdout.write(''.join(sorted(list(str, sys.stdin.readline().strip()), reversed=True)))

# import sys
# print(''.join(sorted(list(str, input(), reversed=True))))

n = str(input())
n_list = []
for i in n:
    n_list.append(i)
n_list.sort(reverse=True)
print(''.join(n_list))
