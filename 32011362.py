print("\t.: Cajero Automatico :.")
moneda = int(input("Moneda (1 para Bs / 2 para $): "))
retirar = int(input("Cuanto va a retirar?: "))
tipo = int(input("1. Ahorro / 2. Corriente: "))
if retirar % 10 != 0:
    print("Error: El cajero solo da billetes de 10, 20, 50 y 100.")
else:
    op_valida = True
    if moneda == 1 and retirar > 10000:
        op_valida = False
    elif moneda == 2 and retirar > 500:
        op_valida = False     
    if not op_valida:
        print("Lo sentimos, el monto excede el limite por dia.")
    else:
        comis = 0
        if tipo == 2:
            comis = retirar * 0.05    
        total = retirar + comis
        res = retirar
        b100 = int(res / 100)
        res = res % 100       
        b50 = int(res / 50)
        res = res % 50        
        b20 = int(res / 20)
        res = res % 20        
        b10 = int(res / 10)
        tipo_moneda = "Bolivares"
        if moneda == 2:
            tipo_moneda = "Dolares"
        print("\n" + "="*25)
        print("      RECIBO")
        print("="*25)
        print(f"Retiro en: {tipo_moneda}")
        print(f"Monto: {retirar}")
        print(f"Comision: {comis}")
        print(f"Total debito: {total}")
        print("-" * 25)
        print("BILLETES:")
        if b100 > 0: print(f"100: {b100}")
        if b50 > 0:  print(f"50:  {b50}")
        if b20 > 0:  print(f"20:  {b20}")
        if b10 > 0:  print(f"10:  {b10}")
        print("="*25)