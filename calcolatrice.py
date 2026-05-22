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

if __name__ == "__main__":
    print("Somma:", somma(10, 5))

    try:
        print("Divisione:", dividi(10, 0))
    except ValueError as e:
        print("Errore:", e)