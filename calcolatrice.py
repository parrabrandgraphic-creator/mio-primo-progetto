def somma(a: float, b: float) -> float:
    return a + b

def sottrai(a: float, b: float) -> float:
    return a - b

def moltiplica(a: float, b: float) -> float:
    return a * b

def dividi(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Impossibile dividere per zero")
    return a / b

def potenza(a: float, b: float) -> float:
    return a ** b

def radice(a: float) -> float:
    if a < 0:
        raise ValueError("Impossibile calcolare la radice di un numero negativo")
    return a ** 0.5

if __name__ == "__main__":
    print("Somma:", somma(10, 5))
    
    try:
        print("Divisione:", dividi(10, 0))
    except ValueError as e:
        print("Errore:", e)
    
    print("Potenza:", potenza(2, 8))