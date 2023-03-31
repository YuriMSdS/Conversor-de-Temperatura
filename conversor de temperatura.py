
def celsius_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

def celsius_para_kelvin(temp_celsius):
    temp_kelvin = temp_celsius + 273.15
    return temp_kelvin

temp_celsius = float(input("Digite a temperatura em graus Celsius: "))
print("Escolha a unidade de destino para a conversão:")
print("1 - Fahrenheit")
print("2 - Kelvin")
opcao = int(input("Opção: "))

if opcao == 1:
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
    print(f"A temperatura em graus Fahrenheit é: {temp_fahrenheit}")
elif opcao == 2:
    temp_kelvin = celsius_para_kelvin(temp_celsius)
    print(f"A temperatura em Kelvin é: {temp_kelvin}")
else:
    print("Opção inválida.")
