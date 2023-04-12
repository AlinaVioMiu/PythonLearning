# # Cu dimensiunea bazei luata dintr-o variabila,
# #
# # a) Sa se afiseze in terminal o jumatate de brad de forma urmatoare
# #
# #        #
# #        ##
# #        ###
# #        ####
# #        #####
# #        ######
n = int(input('Dimensiune brad = '))
for i in range(0, n):
    for j in range(0, i + 1):
        print("#", end="")
    print()
print('\n')

# b) Sa se afiseze un brad de forma:
#
#         #
#        ###
#       #####
#      #######
#     #########
#    ###########
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("#", end="")
    print()
print('\n')
# c) Sa se afiseze un brad cu cer de forma:
#
# ^^^^ # ^^^^
# ^^^ ### ^^^
# ^^ ##### ^^
# ^ ####### ^
#  #########
# ###########
for i in range(1, n + 1):
    for j in range(n - i):
        print("^", end="")
    for j in range(2 * i - 1):
        print("#", end="")
    for j in range(i, n):
        print("^", end="")
    print()
