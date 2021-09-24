a=input("Enter the starting number :")
b=input("Enter the ending number :")
for i in range(int(a),int(b)+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)