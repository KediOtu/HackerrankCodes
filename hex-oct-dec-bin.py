def print_formatted(number):
    for i in range(1, number+1):
        space= len(bin(number)[2:])
        print(str(i).rjust(space)+" "+str(oct(i)[2:]).rjust(space)+" "+str(hex(i)[2:]).upper().rjust(space)+" "+str(bin(i)[2:]).rjust(space))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
