#оператор return
def div(num1:int=1, num2:int=1) -> float:
    return num1 / num2 
print(div(10, 2))

call_func = div(100, 3)
print(call_func)

def reverse_number(num:int=32) -> int:
    return int(str(num)[::-1])
print(reverse_number())
print(type(reverse_number()))