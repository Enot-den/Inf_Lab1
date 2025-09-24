def fib_to_ten(fib_ns_num):
    result = 0
    ch_fib1, ch_fib2 = 1, 1  #числа Фибоначи
    for i in fib_ns_num[::-1]:
        if i == "1":
            result += ch_fib2
        ch_fib1, ch_fib2 = ch_fib2, ch_fib1 + ch_fib2
    return result


while 1:
   xdd = input("Write your number in Fib. num system: ")
   if len(set(xdd) - set("01")):
      print("wrong input")
   else:
      print(f"{xdd} => {fib_to_ten(xdd)}")
