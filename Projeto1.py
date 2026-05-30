from abc import ABC, abstractmethod
from datetime import datetime


# ─────────────────────────────────────────
#  Interface / Classe Abstrata: Transacao
# ─────────────────────────────────────────
class Transacao(ABC):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    @abstractmethod
    def registrar(self, conta: "Conta") -> None:
        pass


# ─────────────────────────────────────────
#  Deposito
# ─────────────────────────────────────────
class Deposito(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar(self, conta: "Conta") -> None:
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


# ─────────────────────────────────────────
#  Saque
# ─────────────────────────────────────────
class Saque(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar(self, conta: "Conta") -> None:
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


# ─────────────────────────────────────────
#  Historico
# ─────────────────────────────────────────
class Historico:
    def __init__(self):
        self._transacoes: list[Transacao] = []

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(transacao)

    def exibir(self) -> None:
        if not self._transacoes:
            print("  Nenhuma transação registrada.")
            return
        for t in self._transacoes:
            tipo = t.__class__.__name__
            print(f"  {tipo:10s}  R$ {t.valor:.2f}")


# ─────────────────────────────────────────
#  Conta
# ─────────────────────────────────────────
class Conta:
    def __init__(self, cliente: "Cliente", numero: int, agencia: str = "0001"):
        self._saldo: float = 0.0
        self._numero: int = numero
        self._agencia: str = agencia
        self._cliente: "Cliente" = cliente
        self._historico: Historico = Historico()

    # ── propriedades ──────────────────────
    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self) -> "Cliente":
        return self._cliente

    @property
    def historico(self) -> Historico:
        return self._historico

    # ── factory ───────────────────────────
    @classmethod
    def nova_conta(cls, cliente: "Cliente", numero: int) -> "Conta":
        return cls(cliente, numero)

    # ── operações ─────────────────────────
    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("⚠  Valor de depósito inválido.")
            return False
        self._saldo += valor
        print(f"✔  Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self._saldo:.2f}")
        return True

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("⚠  Valor de saque inválido.")
            return False
        if valor > self._saldo:
            print("⚠  Saldo insuficiente.")
            return False
        self._saldo -= valor
        print(f"✔  Saque de R$ {valor:.2f} realizado. Saldo: R$ {self._saldo:.2f}")
        return True

    def __str__(self) -> str:
        return (
            f"Agência: {self._agencia}  |  "
            f"Conta: {self._numero}  |  "
            f"Saldo: R$ {self._saldo:.2f}"
        )


# ─────────────────────────────────────────
#  ContaCorrente  (herda de Conta)
# ─────────────────────────────────────────
class ContaCorrente(Conta):
    def __init__(
        self,
        cliente: "Cliente",
        numero: int,
        agencia: str = "0001",
        limite: float = 500.0,
        limite_saques: int = 3,
    ):
        super().__init__(cliente, numero, agencia)
        self._limite: float = limite
        self._limite_saques: int = limite_saques
        self._saques_realizados: int = 0

    @property
    def limite(self) -> float:
        return self._limite

    @property
    def limite_saques(self) -> int:
        return self._limite_saques

    def sacar(self, valor: float) -> bool:
        if self._saques_realizados >= self._limite_saques:
            print("⚠  Limite de saques diários atingido.")
            return False
        if valor > self._saldo + self._limite:
            print("⚠  Valor ultrapassa saldo + limite.")
            return False
        if valor <= 0:
            print("⚠  Valor de saque inválido.")
            return False
        self._saldo -= valor
        self._saques_realizados += 1
        print(f"✔  Saque de R$ {valor:.2f} realizado. Saldo: R$ {self._saldo:.2f}")
        return True

    def __str__(self) -> str:
        return super().__str__() + f"  |  Limite: R$ {self._limite:.2f}"


# ─────────────────────────────────────────
#  Cliente  (base)
# ─────────────────────────────────────────
class Cliente:
    def __init__(self, endereco: str):
        self._endereco: str = endereco
        self._contas: list[Conta] = []

    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def contas(self) -> list[Conta]:
        return self._contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta) -> None:
        self._contas.append(conta)


# ─────────────────────────────────────────
#  PessoaFisica  (herda de Cliente)
# ─────────────────────────────────────────
class PessoaFisica(Cliente):
    def __init__(
        self,
        nome: str,
        cpf: str,
        data_nascimento: datetime,
        endereco: str,
    ):
        super().__init__(endereco)
        self._nome: str = nome
        self._cpf: str = cpf
        self._data_nascimento: datetime = data_nascimento

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def data_nascimento(self) -> datetime:
        return self._data_nascimento

    def __str__(self) -> str:
        return f"{self._nome} (CPF: {self._cpf})"


# ═══════════════════════════════════════════
#  DEMONSTRAÇÃO
# ═══════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 55)
    print("         SISTEMA BANCÁRIO — DEMO")
    print("=" * 55)

    # Criar cliente
    cliente = PessoaFisica(
        nome="Lucas Silva",
        cpf="123.456.789-00",
        data_nascimento=datetime(2000, 5, 15),
        endereco="Rua das Flores, 42 — Itaquaquecetuba/SP",
    )
    print(f"\nCliente criado: {cliente}")

    # Criar conta corrente
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=1001)
    cliente.adicionar_conta(conta)
    print(f"Conta: {conta}\n")

    # Transações via interface Transacao
    print("── Depósito R$ 1.500,00 ──")
    cliente.realizar_transacao(conta, Deposito(1500.00))

    print("\n── Saque R$ 200,00 ──")
    cliente.realizar_transacao(conta, Saque(200.00))

    print("\n── Saque R$ 50,00 ──")
    cliente.realizar_transacao(conta, Saque(50.00))

    print("\n── Tentativa de saque R$ 5.000,00 (deve falhar) ──")
    cliente.realizar_transacao(conta, Saque(5000.00))

    print("\n── Extrato ──")
    conta.historico.exibir()
    print(f"\nSaldo final: R$ {conta.saldo:.2f}")
    print("=" * 55)