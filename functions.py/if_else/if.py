cost=float(input("product cost"))
gst=0.10
net=cost+(cost*gst)
print(net)
if(net>500):
    discount=net*0.80
    print("discount",discount)

    
    