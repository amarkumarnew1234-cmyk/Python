'''
10. Write a program to print truth table for bitwise operators( & , | and ^ operators)
 '''
print("Truth table for bitwise operators:")
print("A\tB\tA&B\tA|B\tA^B")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a}\t{b}\t{a & b}\t{a | b}\t{a ^ b}")