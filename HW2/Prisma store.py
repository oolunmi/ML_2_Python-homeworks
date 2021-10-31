n = int(input())
stores=[]
for i in range(n):
    stores.append(input())
store_count={}
for store in stores:
    if store not in store_count:
        store_count[store]=1
    else:
        store_count[store]+=1

print(store_count)
missed_stores = n - len(store_count)

print(missed_stores)

