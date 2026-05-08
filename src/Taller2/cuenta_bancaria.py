class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


def main():
    cuenta = CuentaBancaria("Ana Lopez", 1000)

    print("Informacion de la cuenta")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: ${cuenta.saldo}")
    print()

    print("Depositar dinero")
    if cuenta.depositar(500):
        print(f"Deposito exitoso. Nuevo saldo: ${cuenta.saldo}")
    else:
        print("La cantidad a depositar debe ser positiva")
    print()

    print("Retirar dinero")
    if cuenta.retirar(200):
        print(f"Retiro exitoso. Nuevo saldo: ${cuenta.saldo}")
    else:
        print("Fondos insuficientes")
    print()

    print("Intentar retirar mas de lo que hay")
    if cuenta.retirar(2000):
        print(f"Retiro exitoso. Nuevo saldo: ${cuenta.saldo}")
    else:
        print("Fondos insuficientes")
    print()

    print("Intentar asignar saldo negativo")
    try:
        cuenta.saldo = -50
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Intentar cambiar el titular")
    try:
        cuenta.titular = "Otro nombre"
    except AttributeError:
        print("No se puede modificar el titular")
    print()

    print(f"Titular final: {cuenta.titular}")
    print(f"Saldo final: ${cuenta.saldo}")


if __name__ == "__main__":
    main()
