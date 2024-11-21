class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}"
        else:
            return "La cantidad a depositar debe ser positiva."

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}"
            else:
                return "Fondos insuficientes."
        else:
            return "La cantidad a retirar debe ser positiva."

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self.saldo:.2f}"
