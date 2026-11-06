from src.core.base_schema import Base
from src.core.types import StatusDoca

from pydantic import Field
from decimal import Decimal

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.schemas import AgendamentoResponse


class DocaResponse(Base):

    numero: str
    descricao: str | None = None
    localizacao: str | None = None

    capacidade_maxima_kg: Decimal | None = None

    status: StatusDoca
    ativo: bool

    agendamentos: list[AgendamentoResponse] = Field(default_factory=list)


class DocaCreate(Base):

    numero: str = Field(..., min_length=1, max_length=20)
    descricao: str | None = Field(None, max_length=255)
    localizacao: str | None = Field(None, max_length=150)

    capacidade_maxima_kg: Decimal | None = Field(
        None, gt=0, max_digits=12, decimal_places=2
    )

    status: StatusDoca = StatusDoca.DISPONIVEL

    ativo: bool = True


class DocaUpdate(Base):

    numero: str | None = Field(None, min_length=1, max_length=20)
    descricao: str | None = Field(None, max_length=255)
    localizacao: str | None = Field(None, max_length=150)

    capacidade_maxima_kg: Decimal | None = Field(
        None, gt=0, max_digits=12, decimal_places=2
    )

    status: StatusDoca | None = None

    ativo: bool | None = None