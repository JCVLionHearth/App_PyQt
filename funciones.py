def cifrar(numero):
    # Convertimos el número a una lista de dígitos
    digitos = [int(d) for d in str(numero)]
    
    # Sumar 7 a cada dígito y tomar el residuo de dividir entre 10
    cifrado = [(d + 7) % 10 for d in digitos]
    
    # Intercambiar los dígitos según la especificación
    cifrado[0], cifrado[2] = cifrado[2], cifrado[0]
    cifrado[1], cifrado[3] = cifrado[3], cifrado[1]
    cifrado[4], cifrado[5] = cifrado[5], cifrado[4]
    
    # Convertir de nuevo a entero
    return int(''.join(map(str, cifrado)))

def descifrar(cifrado):
    # Invertir los intercambios
    digitos = [int(d) for d in str(cifrado)]
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]
    digitos[4], digitos[5] = digitos[5], digitos[4]
    
    # Restar 7 y ajustar valores
    descifrado = [(d - 7 + 10) % 10 for d in digitos]
    
    return int(''.join(map(str, descifrado)))