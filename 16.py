
def check_input(gt,input_string, print_string):
    input_from_user = int(input(input_string))
    if input_from_user > gt:
        print(print_string)
check_input(0,"enter your age: ", "age is ok")
def sqre(x):
    result = print(x * x)
    return result

a = sqre(100)
if a > 100:
    print("hey")


