from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    criar_access_token,
    hash_senha,
    verificar_senha,
)
from app.database import db
from app.models import Token, UsuarioCriar, UsuarioResposta

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post(
    "/registrar",
    response_model=UsuarioResposta,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar novo usuário",
)
async def registrar(dados: UsuarioCriar):
    """Cria um novo usuário no sistema."""
    if db.buscar_usuario_por_username(dados.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username já cadastrado.",
        )
    usuario = db.criar_usuario(
        username=dados.username,
        hashed_password=hash_senha(dados.password),
    )
    return UsuarioResposta(id=usuario.id, username=usuario.username)


@router.post(
    "/token",
    response_model=Token,
    summary="Login — obter JWT",
)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Autentica o usuário e retorna um **Bearer token JWT**.

    Use o token no header `Authorization: Bearer <token>` para acessar
    os endpoints protegidos.
    """
    usuario = db.buscar_usuario_por_username(form_data.username)
    if not usuario or not verificar_senha(form_data.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = criar_access_token(
        data={"sub": usuario.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return Token(access_token=access_token)
