def main():
    # borra la instrucción 'pass' y escribe tu código aquí abajo:
    num = int(input('Introduzca un numero: '))

    if num % 10 == 0:
      múltiplo = 'si'
    else:
      múltiplo = 'no'

    print(f'El numero {num} {múltiplo} es multiplo de 10')


if __name__ == '__main__': 
    main()
