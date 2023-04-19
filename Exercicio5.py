def inverter_string(string):
    

    lista_caracteres = list(string)
   
    lista_caracteres.reverse()
    
    string_invertida = ''.join(lista_caracteres)
   
    return string_invertida

string_original = input("Digite uma string: ")

string_invertida = inverter_string(string_original)

print("String invertida:", string_invertida)
