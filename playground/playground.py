def rgb(r, g, b):
    #your code here :)
    hex = '0123456789ABCDEF'
    def converter(value):
        if value < 0:
            test_value = 0
        else:
            test_value = value
        
        multtimes = hex[test_value // 16]
        remainder = hex[test_value % 16]
        converted = f"{multtimes}{remainder}"
        
        return converted
    
    return f"{converter(r)}{converter(g)}{converter(b)}"

print(rgb(-20,1,1))

