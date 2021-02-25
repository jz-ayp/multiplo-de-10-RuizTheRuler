def main():
    # borra la instrucción 'pass' y escribe tu código aquí abajo:
    num = int(input('Introduzca un número: '))
    
    if num % 10 == 0:
      múltiplo = 'sí'
    else:
      múltiplo = 'no'

    print(f'El número {num} {múltiplo} es múltiplo de 10')


if __name__ == '__main__': 
    main()
