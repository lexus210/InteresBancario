class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def actualizar_saldo(self):
        if self.saldo < 10000.00:
            self.saldo *= (1 + 0.03)
        else:
            self.saldo *= (1 + 0.04)

    def mostrar_saldo(self):
        print(f"Saldo final es {self.saldo:.2f}")


# Solicitar saldo inicial al usuario
saldo_inicial = float(input("Dame el saldo actual: "))

# Crear una instancia de la clase Cuenta
cuenta = Cuenta(saldo_inicial)

# Actualizar y mostrar el saldo
cuenta.actualizar_saldo()
cuenta.mostrar_saldo()