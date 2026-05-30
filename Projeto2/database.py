"""
Banco de dados em memória.
Em produção, substitua por SQLAlchemy + PostgreSQL/SQLite async.
"""
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


# ──────────────────────────────────────────
#  Entidades internas (equivalente às tabelas)
# ──────────────────────────────────────────
@dataclass
class UsuarioDB:
    id: int
    username: str
    hashed_password: str


@dataclass
class ContaDB:
    id: int
    numero: str
    agencia: str
    titular: str
    saldo: float = 0.0
    usuario_id: int = 0


@dataclass
class TransacaoDB:
    id: int
    tipo: str          # "deposito" | "saque"
    valor: float
    data_hora: datetime
    conta_id: int
    saldo_apos: float


# ──────────────────────────────────────────
#  "Banco" em memória
# ──────────────────────────────────────────
class FakeDB:
    def __init__(self):
        self.usuarios: dict[int, UsuarioDB] = {}
        self.contas: dict[int, ContaDB] = {}
        self.transacoes: dict[int, TransacaoDB] = {}
        self._uid = 0
        self._cid = 0
        self._tid = 0

    # ── helpers de ID ────────────────────
    def _next_uid(self) -> int:
        self._uid += 1
        return self._uid

    def _next_cid(self) -> int:
        self._cid += 1
        return self._cid

    def _next_tid(self) -> int:
        self._tid += 1
        return self._tid

    # ── usuários ─────────────────────────
    def criar_usuario(self, username: str, hashed_password: str) -> UsuarioDB:
        u = UsuarioDB(id=self._next_uid(), username=username, hashed_password=hashed_password)
        self.usuarios[u.id] = u
        return u

    def buscar_usuario_por_username(self, username: str) -> Optional[UsuarioDB]:
        return next((u for u in self.usuarios.values() if u.username == username), None)

    def buscar_usuario_por_id(self, uid: int) -> Optional[UsuarioDB]:
        return self.usuarios.get(uid)

    # ── contas ───────────────────────────
    def criar_conta(self, numero: str, agencia: str, titular: str, usuario_id: int) -> ContaDB:
        c = ContaDB(id=self._next_cid(), numero=numero, agencia=agencia,
                    titular=titular, usuario_id=usuario_id)
        self.contas[c.id] = c
        return c

    def buscar_conta_por_numero(self, numero: str) -> Optional[ContaDB]:
        return next((c for c in self.contas.values() if c.numero == numero), None)

    def buscar_conta_por_id(self, cid: int) -> Optional[ContaDB]:
        return self.contas.get(cid)

    def listar_contas_usuario(self, usuario_id: int) -> list[ContaDB]:
        return [c for c in self.contas.values() if c.usuario_id == usuario_id]

    # ── transações ───────────────────────
    def criar_transacao(self, tipo: str, valor: float, conta_id: int, saldo_apos: float) -> TransacaoDB:
        t = TransacaoDB(
            id=self._next_tid(),
            tipo=tipo,
            valor=valor,
            data_hora=datetime.utcnow(),
            conta_id=conta_id,
            saldo_apos=saldo_apos,
        )
        self.transacoes[t.id] = t
        return t

    def listar_transacoes_conta(self, conta_id: int) -> list[TransacaoDB]:
        return sorted(
            [t for t in self.transacoes.values() if t.conta_id == conta_id],
            key=lambda x: x.data_hora,
        )


# instância global (singleton)
db = FakeDB()
