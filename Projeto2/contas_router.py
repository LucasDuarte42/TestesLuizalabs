from fastapi import APIRouter, Depends, HTTPException, status

from app.auth import get_current_user
from app.database import db, UsuarioDB
from app.models import ContaCriar, ContaResposta

router = APIRouter(prefix="/contas", tags=["Contas Correntes"])


def _to_response(c) -> ContaResposta:
    return ContaResposta(
        id=c.id, numero=c.numero, agencia=c.agencia,
        titular=c.titular, saldo=c.saldo,
    )


@router.post(
    "/",
    response_model=ContaResposta,
    status_code=status.HTTP_201_CREATED,
    summary="Criar conta corrente",
)
async def criar_conta(
    dados: ContaCriar,
    usuario: UsuarioDB = Depends(get_current_user),
):
    """Cria uma nova conta corrente vinculada ao usuário autenticado."""
    if db.buscar_conta_por_numero(dados.numero):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Conta com número '{dados.numero}' já existe.",
        )
    conta = db.criar_conta(
        numero=dados.numero,
        agencia=dados.agencia,
        titular=dados.titular,
        usuario_id=usuario.id,
    )
    return _to_response(conta)


@router.get(
    "/",
    response_model=list[ContaResposta],
    summary="Listar minhas contas",
)
async def listar_contas(usuario: UsuarioDB = Depends(get_current_user)):
    """Retorna todas as contas correntes do usuário autenticado."""
    contas = db.listar_contas_usuario(usuario.id)
    return [_to_response(c) for c in contas]


@router.get(
    "/{conta_id}",
    response_model=ContaResposta,
    summary="Detalhar conta",
)
async def detalhar_conta(
    conta_id: int,
    usuario: UsuarioDB = Depends(get_current_user),
):
    """Retorna os dados de uma conta específica."""
    conta = db.buscar_conta_por_id(conta_id)
    if not conta or conta.usuario_id != usuario.id:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")
    return _to_response(conta)
