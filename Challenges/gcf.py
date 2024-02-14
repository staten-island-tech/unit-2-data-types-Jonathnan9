def gcf_calculator(numb1, numb2):
  list1 = []
  list2 =[]

  for a in range(1, numb1+1):
    if  numb1 % a == 0:
      list1.append(a)

  for b in range(1, numb2+1):
    if  numb2 % b == 0:
      list2.append(b)

  for a in list1:
    print(a, end=' ')

numb1 = int(input("What is the first number? "))
numb2 = int(input("What is the secomd number? "))
gcf = gcf_calculator(numb1, numb2)
""" 

    if numb1 > numb2:
      gcf = numb1 - numb2
    if numb1 < numb2:
      gcf = numb2 - numb1
    else:
     print('0')

    return gcf_calculator(numb1, numb2)
     

numb1 = int(input("What is the first number? "))
numb2 = int(input("What is the secomd number? "))
gcf = gcf_calculator(numb1, numb2)

if isinstance(gcf, str):
    print(gcf)
else:
    print("The GCF is ", round(gcf, 2))
 """
