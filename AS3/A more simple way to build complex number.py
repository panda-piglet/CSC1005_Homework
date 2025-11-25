def p_complex(complexnumber):
        result = []
        tmp = 0
        for index in range(1,len(complexnumber)):
            if complexnumber [index] == "+" or complexnumber [index] == "-":
                result.append(complexnumber[tmp:index])
                tmp = index
        result.append(complexnumber[tmp::])
        real = 0
        imag = 0
        try:
            for element in result:
                if element.endswith("*i"):
                    imag += float(element[:-2:])
                else:
                    real += float(element)
        except ValueError:
            print("This is not a complex number")
        return real,imag
    
print(p_complex("3.1+2.2*i"))