from typing import TYPE_CHECKING

from pydantic import Field

from src.core.base_schema import Base
from src.core.types import TipoUsuario

if TYPE_CHECKING:
    from src.core.schemas import AgendamentoResponse, RelatorioResponse


class SupervisorResponse(Base):
    nome: str
    email: str
    senha_hash: str
    telefone: str | None

    tipo: TipoUsuario

    ativo: bool = True

    agendamentos: list[AgendamentoResponse] = []

    relatorios: list[RelatorioResponse] = []


class SupervisorCreate(Base):
    nome: str = Field(..., max_length=150)
    email: str = Field(..., max_length=150)
    senha_hash: str = Field(..., max_length=255)
    telefone: str | None = Field(None, max_length=20)

    tipo: TipoUsuario = TipoUsuario.SUPERVISOR

    ativo: bool = True


class SupervisorUpdate(Base):
    nome: str | None = Field(None, max_length=150)
    email: str | None = Field(None, max_length=150)
    senha_hash: str | None = Field(None, max_length=255)
    telefone: str | None = Field(None, max_length=20)

    tipo: TipoUsuario | None

    ativo: bool | None = None
