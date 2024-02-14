def gcf_calculator(numb1, numb2):
  list1 = []
  list2 =[]

  for a in range(1, numb1+1):
    if  numb1 % a == 0:
      list1.append(a)

  for b in range(1, numb2+1):
    if  numb2 % b == 0:
      list2.append(b)

  print(list1,list2)



numb1 = int(input("What is the first number? "))
numb2 = int(input("What is the secomd number? "))
gcf = gcf_calculator(numb1, numb2)

""" 
if isinstance(gcf, str):
    print(gcf)
else:
    print("The GCF is ", round(gcf, 2))
 """