num1=8
num2=23
num3=16
if(num1>=num2)and(num1>=num3):
 largest=num1
elif(num2>=num1)and(num2>=num3):
   largest=num2
else:
   largest=num3
print("the largest num between",num1,num2,"and",num3,"is" ,largest)