#indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = 1234-6789-9090-1233 

#1 print(credit_number[0])
#2 print(credit_number[0:4])
#3 print(credit_number[5:9])
#4 print(credit_number[5:])
#5 print(credit_number[-1])
#6 print(credit_number[-4])
#7 print(credit_number[::2])

#1 output - 1
#2 output - 1234
#3 output - 5678
#4 output - 6789-9090-1233
#5 output - 3
#6 output - 2
#7 output - 13-7999-23  - step ::2 = alternate numbers

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1]
print(credit_number)
#output - 3321-0909-9876-4321 - it will get reverse