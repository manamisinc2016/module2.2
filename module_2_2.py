First=int(input("Enter First Digit"))
Second=int(input("Enter Second Digit"))
Third=int(input("Enter Third Digit"))
if First == Second == Third:
    print(3)
elif First == Second or Second == Third or First == Third:
    print(2)
else:
    print(0)
