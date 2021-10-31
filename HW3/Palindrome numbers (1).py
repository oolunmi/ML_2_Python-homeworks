a=int(input())
b=int(input())
palindromes=""
for i in range(a,b+1):
   i_string=str(i) 
   i_reverse=int(i_string[::-1])
   if i==i_reverse:
       palindrome=str(i)
       palindromes+=palindrome+" " 
print(palindromes)