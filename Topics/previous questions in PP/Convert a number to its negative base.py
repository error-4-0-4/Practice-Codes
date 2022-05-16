def toNgBase(n, NgBase):
    if (n==0):
        return "0"
    
    converted='01'
    while (n):
        remainder = n%(NgBase)
        n = int(n/NgBase)

        if (remainder<0):
            remainder += ((-1)*NgBase)
            n += 1
        converted = str(remainder)+ converted

    return converted

if __name__ == '__main__':
    n=13
    NgBase= -2
    print(toNgBase(n, NgBase))