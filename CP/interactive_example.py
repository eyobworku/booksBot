low, high = 1, 10**6

while low < high:
    mid = (low + high + 1) // 2
    print(mid,flush=True)
    
    s = input()
    if s == ">=":
            low = mid
    else:
        high = mid - 1
    
print(f"! {low}\n",flush=True)