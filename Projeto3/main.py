from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth_router import router as auth_router
from app.routers.contas_router import router as contas_router
from app.routers.transacoes_router import router as transacoes_router

# ──────────────────────────────────────────
#  Aplicação
# ──────────────────────────────────────────
app = FastAPI(
    title="API Bancária Assíncrona",
    description="""
## 🏦 API Bancária com FastAPI + JWT

Gerencie **contas correntes** e **transações bancárias** de forma segura.

### Fluxo de uso
1. **Registre-se** em `POST /auth/registrar`
2. **Faça login** em `POST /auth/token` e copie o `access_token`
3. Clique em **Authorize 🔒** e cole o token
4. Crie contas e realize transações!

### Regras de negócio
- Depósitos e saques devem ter valor **maior que zero**
- Saques só são permitidos com **saldo suficiente**
- Cada conta pertence ao usuário autenticado
""",
    version="1.0.0",
    contact={"name": "API Bancária", "email": "contato@banco.dev"},
    license_info={"name": "MIT"},
)

# ──────────────────────────────────────────
#  CORS
# ──────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────
#  Routers
# ──────────────────────────────────────────
app.include_router(auth_router)
app.include_router(contas_router)
app.include_router(transacoes_router)


@app.get("/", tags=["Health"], summary="Health check")
async def root():
    """Verifica se a API está no ar."""
    return {"status": "online", "message": "API Bancária funcionando! Acesse /docs"}
