# Sa se scrie cate un algoritm pentru urmatoarele cazuri:
# - Conversia unei temperaturi din 'C in 'F.
celsius = float(input('Introduceti temperatura in grade Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print(f' {celsius} grade Celsius = {fahrenheit} grade Fahrenheit')

# - Conversia unei temperaturi din 'F in 'C.
fahrenheit = float(input('Introduceti temperatura in grade Fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8
print(f' {fahrenheit} grade Fahrenheit = {celsius} grade Celsius')


#Conversie din kelvin in celsius. Functie.
def conversie_k_c(k):
    c = k - 273.15
    return c

if __name__ == '__main__':

    print(conversie_k_c(0))
    print(conversie_k_c(100))