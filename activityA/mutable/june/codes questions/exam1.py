input_counts=input().split()
counts=list(map(int,input_counts))
denominations=[20,40,100,200,500,1000]
total_cents=sum(count*denom for count,denom in zip(counts,denominations))
total_dollars=total_cents/100
print(round(total_dollars,1))


