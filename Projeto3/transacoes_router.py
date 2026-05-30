from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user
from app.database import db, UsuarioDB
from app.models import (
    ExtratoResposta,
    ContaResposta,
    TransacaoCriar,
    TransacaoResposta,
    TipoTransacao,
)

router = APIRouter(prefix="/contas", tags=["Transações"])


def _transacao_to_response(t) -> TransacaoResposta:
    return TransacaoResposta(
        id=t.id,
        tipo=t.tipo,
        valor=t.valor,
        data_hora=t.data_hora,
        conta_id=t.conta_id,
        saldo_apos=t.saldo_apos,
    )


def _get_conta_autorizada(conta_id: int, usuario: UsuarioDB):
    """Helper: busca conta e valida que pertence ao usuário."""
    conta = db.buscar_conta_por_id(conta_id)
    if not conta or conta.usuario_id != usuario.id:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")
    return conta


@router.post(
    "/{conta_id}/transacoes",
    response_model=TransacaoResposta,
    status_code=status.HTTP_201_CREATED,
    summary="Realizar depósito ou saque",
)
async def realizar_transacao(
    conta_id: int,
    dados: TransacaoCriar,
    usuario: UsuarioDB = Depends(get_current_user),
):
    """
    Registra uma transação (depósito ou saque) na conta informada.

    - **deposito**: adiciona valor ao saldo (valor > 0)
    - **saque**: subtrai valor do saldo; exige saldo suficiente
    """
    conta = _get_conta_autorizada(conta_id, usuario)

    if dados.tipo == TipoTransacao.deposito:
        conta.saldo += dados.valor

    elif dados.tipo == TipoTransacao.saque:
        if dados.valor > conta.saldo:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Saldo insuficiente. Saldo atual: R$ {conta.saldo:.2f}",
            )
        conta.saldo -= dados.valor

    transacao = db.criar_transacao(
        tipo=dados.tipo.value,
        valor=dados.valor,
        conta_id=conta.id,
        saldo_apos=conta.saldo,
    )
    return _transacao_to_response(transacao)


@router.get(
    "/{conta_id}/extrato",
    response_model=ExtratoResposta,
    summary="Exibir extrato da conta",
)
async def extrato(
    conta_id: int,
    usuario: UsuarioDB = Depends(get_current_user),
):
    """
    Retorna o extrato completo da conta:
    - Dados da conta
    - Lista de todas as transações
    - Total de depósitos e saques
    """
    conta = _get_conta_autorizada(conta_id, usuario)
    transacoes = db.listar_transacoes_conta(conta.id)

    total_dep = sum(t.valor for t in transacoes if t.tipo == "deposito")
    total_saq = sum(t.valor for t in transacoes if t.tipo == "saque")

    return ExtratoResposta(
        conta=ContaResposta(
            id=conta.id, numero=conta.numero, agencia=conta.agencia,
            titular=conta.titular, saldo=conta.saldo,
        ),
        transacoes=[_transacao_to_response(t) for t in transacoes],
        total_depositos=total_dep,
        total_saques=total_saq,
    )
