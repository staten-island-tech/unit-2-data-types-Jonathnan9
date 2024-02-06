def gcf_calculator(numb1, numb2):
    if numb1 > numb2:
      gcf1 = numb1 - numb2
    if numb1 < numb2:
      gcf2 = numb2 - numb1
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