sequence = int(input("Sequence ends at: "))

x = 0
y = 1

# if the value is 0 print this
if sequence == 0:
    print ("0: 0 0")

# if the value is 1 print this
elif sequence == 1:
    print ("0: 0 0")
    print ("1: 1 1")


# if the value is greater than 1 execute these lines

elif sequence > 1:
    print("0: 0 0")
    print("1: 1 1")

    # for loop creates a range of values to print starting from 2 to the sequence number
    for i in range(2, sequence+1): #(sequence + 1 allows the for loop to be printed to the sequence number)
        z = x + y
        x = y
        y = z
        print(str(i) + ":",z, "{:,}".format(z))#{:,}.format() method allows the 4 digit and higher
                                               #numbers to be printed with commas seperating them
else:
    print("Please enter number greater than or equal to 0")
