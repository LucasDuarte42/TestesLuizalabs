from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional


# ──────────────────────────────────────────
#  Enums
# ──────────────────────────────────────────
class TipoTransacao(str, Enum):
    deposito = "deposito"
    saque = "saque"


# ──────────────────────────────────────────
#  Auth
# ──────────────────────────────────────────
class UsuarioCriar(BaseModel):
    username: str = Field(..., description="Nome de usuário único")
    password: str = Field(..., min_length=6, description="Senha (mín. 6 caracteres)")


class UsuarioResposta(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: Optional[str] = None


# ──────────────────────────────────────────
#  Conta Corrente
# ──────────────────────────────────────────
class ContaCriar(BaseModel):
    numero: str = Field(..., description="Número da conta (único)")
    agencia: str = Field(default="0001", description="Agência da conta")
    titular: str = Field(..., description="Nome do titular")


class ContaResposta(BaseModel):
    id: int
    numero: str
    agencia: str
    titular: str
    saldo: float

    model_config = {"from_attributes": True}


# ──────────────────────────────────────────
#  Transação
# ──────────────────────────────────────────
class TransacaoCriar(BaseModel):
    tipo: TipoTransacao = Field(..., description="Tipo: 'deposito' ou 'saque'")
    valor: float = Field(..., gt=0, description="Valor deve ser maior que zero")


class TransacaoResposta(BaseModel):
    id: int
    tipo: TipoTransacao
    valor: float
    data_hora: datetime
    conta_id: int
    saldo_apos: float

    model_config = {"from_attributes": True}


class ExtratoResposta(BaseModel):
    conta: ContaResposta
    transacoes: list[TransacaoResposta]
    total_depositos: float
    total_saques: float
