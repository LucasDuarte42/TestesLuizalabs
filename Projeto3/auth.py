from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.database import db, UsuarioDB
from app.models import TokenData

# ──────────────────────────────────────────
#  Configurações JWT
# ──────────────────────────────────────────
SECRET_KEY = "super-secret-key-troque-em-producao-123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


# ──────────────────────────────────────────
#  Utilitários de senha
# ──────────────────────────────────────────
def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)


def verificar_senha(senha_plana: str, hash: str) -> bool:
    return pwd_context.verify(senha_plana, hash)


# ──────────────────────────────────────────
#  Utilitários de token
# ──────────────────────────────────────────
def criar_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# ──────────────────────────────────────────
#  Dependência: usuário atual autenticado
# ──────────────────────────────────────────
async def get_current_user(token: str = Depends(oauth2_scheme)) -> UsuarioDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.buscar_usuario_por_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user
