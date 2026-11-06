from src.core.base_schema import Base

from pydantic import Field
from decimal import Decimal

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.schemas import TransporteResponse


class CargaResponse(Base):

    descricao: str
    tipo_carga: str | None = None
    peso_kg: Decimal
    quantidade: int | None = None
    unidade_medida: str | None = None
    origem: str | None = None
    destino: str | None = None
    nota_fiscal: str | None = None
    observacoes: str | None = None

    transportes: list[TransporteResponse] = Field(default_factory=list)


class CargaCreate(Base):

    descricao: str = Field(..., min_length=1, max_length=255)
    tipo_carga: str | None = Field(None, max_length=100)

    peso_kg: Decimal = Field(
        ..., gt=0, max_digits=12, decimal_places=2
    )

    quantidade: int | None = Field(None, gt=0)
    unidade_medida: str | None = Field(None, max_length=30)

    origem: str | None = Field(None, max_length=200)
    destino: str | None = Field(None, max_length=200)

    nota_fiscal: str | None = Field(None, max_length=50)
    observacoes: str | None = None


class CargaUpdate(Base):

    descricao: str | None = Field(None, min_length=1, max_length=255)
    tipo_carga: str | None = Field(None, max_length=100)

    peso_kg: Decimal | None = Field(
        None, gt=0, max_digits=12, decimal_places=2
    )

    quantidade: int | None = Field(None, gt=0)
    unidade_medida: str | None = Field(None, max_length=30)

    origem: str | None = Field(None, max_length=200)
    destino: str | None = Field(None, max_length=200)

    nota_fiscal: str | None = Field(None, max_length=50)
    observacoes: str | None = None