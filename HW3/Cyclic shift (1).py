def cyclic_shifts(n, shifts,numbers):
  k=shifts%n
  new_start=numbers[-k:]
  end=numbers[:-k]
  new_number=new_start+end
  print(new_number)

n=int(input())
shifts=int(input())
numbers = [int(input()) for _ in range(n)]
cyclic_shifts(n,shifts,numbers)