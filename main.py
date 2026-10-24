class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self._saldo = saldo
        self._historico: list[str] = []
        
    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo")
        self._saldo += valor
        self._historico.append(f"+R${valor:.2f}")
    
    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Saque deve ser positivo")
        if valor > self._saldo:
            raise ValueError(f"Saldo insuficiente (R${self._saldo:.2f})")
        self._saldo -= valor
        self._historico.append(f"-R${valor:.2f}")
    
    def extrato(self) -> None:
        print(f"--- Extrato de {self.titular} ---")
        for op in self._historico:
            print(f" {op}")
        print(f" Saldo atual: R${self._saldo:.2f}")
    
    def __str__(self) -> str:
        return f"Conta({self.titular}, R${self._saldo:.2f})"
    
    def __repr__(self) -> str:
        return f"ContaBancaria('{self.titular}', {self._saldo})"
    

c1 = ContaBancaria("Eduardo", 1000)
c1.depositar(500)
c1.sacar(200)
c1.extrato()
print(c1)
print(repr(c1))