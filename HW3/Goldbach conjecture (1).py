def is_prime(num):
  cnt_div_num=0
  i=1
  while i*i<=num:
    if num%i==0:
      if num//i==i:
        cnt_div_num+=1
      else:
        cnt_div_num+=2
    i+=1
  if cnt_div_num==2:
    return True
  return False

def number(n):
  for i in range(n+1):
    if is_prime(i) and is_prime(n-i):
      print(i, n-i)
      break


if __name__ == "__main__":
  number(4)
  number(992)
  number(10)
    



