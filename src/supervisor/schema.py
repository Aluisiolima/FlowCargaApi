from typing import TYPE_CHECKING

from pydantic import EmailStr, Field

from src.core.base_schema import Base
from src.core.types import TipoUsuario

if TYPE_CHECKING:
    pass


class SupervisorResponse(Base):
    id: int
    nome: str
    email: EmailStr
    telefone: str | None

    tipo: TipoUsuario
    ativo: bool

    agendamentos: list[dict] = []
    relatorios: list[dict] = []


class SupervisorCreate(Base):
    nome: str = Field(..., max_length=150)
    email: EmailStr
    senha: str = Field(..., min_length=8, max_length=128)
    telefone: str | None = Field(None, max_length=20)


class SupervisorUpdate(Base):
    nome: str | None = Field(None, max_length=150)
    email: EmailStr | None = None
    senha: str | None = Field(None, min_length=8, max_length=128)
    telefone: str | None = Field(None, max_length=20)


class SupervisorLogin(Base):
    email: EmailStr
    senha: str


class TokenResponse(Base):
    access_token: str
    token_type: str = "bearer"
    supervisor: SupervisorResponse
