# decimal = int(input("Enter a decimal number: "))
# hex_letters = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# hexadecimal = ""
# while decimal > 0:
#     remainder = decimal%16
#     if remainder <= 9:
#         hexadecimal = str(remainder) + hexadecimal

#     elif remainder >= 10 and remainder < 16:
#         hexadecimal = hex_letters[remainder] + hexadecimal

#     else:
#         decimal = decimal // 16

# print(hexadecimal)


# hex_map ={10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
# def to_hex(n):
#     result = ""
#     if n == 0:
#         print('0')
#     while n != 0:
#         result += str(hex_map[(n % 16)])
#         n = n // 16
#     print( '0x'+result[::-1])

