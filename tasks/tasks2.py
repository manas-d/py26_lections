'''Задача с долинами'''

# # case 1
# path = 8
# steps = 'UDDDUDUU'
# # result = 1 dolina


# # case 2
# path = 10
# steps = 'DUDDDUUDUU'
# # result = 2 dolina

# sealevel = 0
# valleys = 0

# for step in steps:
#     if step  == 'U':
#         sealevel += 1
#         if sealevel == 0:
#             valleys += 1
#     elif step == 'D':
#         sealevel -= 1

# print(f'Result: {valleys} count!')