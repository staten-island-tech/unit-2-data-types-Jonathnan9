def gcf_calculator(numb1, numb2):
    list1 = []
    list2 = []

    for a in range(1, numb1 + 1):
        if numb1 % a == 0:
            list1.append(a)

    for b in range(1, numb2 + 1):
        if numb2 % b == 0:
            list2.append(b)

    common_factors = set(list1) & set(list2)
    gcf = max(common_factors)

    return gcf


numb1 = int(input("What is the first number? "))
numb2 = int(input("What is the second number? "))

gcf = gcf_calculator(numb1, numb2)
print("The greatest common factor is:", gcf)
