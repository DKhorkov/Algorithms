def recursion(number):
    if number > 0:
        print(f'Printing number {number:,.2f}')
        recursion(number - 1)
    else:
        return


recursion(3.15)
