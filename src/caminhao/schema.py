from src.core.base_schema import Base

from pydantic import Field
from decimal import Decimal

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.schemas import TransporteResponse


class CaminhaoResponse(Base):

    placa: str
    marca: str | None = None
    modelo: str | None = None
    ano_fabricacao: int | None = None
    capacidade_kg: Decimal | None = None
    tipo_veiculo: str | None = None
    ativo: bool

    transportes: list[TransporteResponse] = Field(default_factory=list)


class CaminhaoCreate(Base):

    placa: str = Field(..., min_length=7, max_length=10)

    marca: str | None = Field(None, max_length=100)
    modelo: str | None = Field(None, max_length=100)

    ano_fabricacao: int | None = Field(None, gt=1900)

    capacidade_kg: Decimal | None = Field(
        None, gt=0, max_digits=12, decimal_places=2
    )

    tipo_veiculo: str | None = Field(None, max_length=50)

    ativo: bool = True


class CaminhaoUpdate(Base):

    placa: str | None = Field(None, min_length=7, max_length=10)

    marca: str | None = Field(None, max_length=100)
    modelo: str | None = Field(None, max_length=100)

    ano_fabricacao: int | None = Field(None, gt=1900)

    capacidade_kg: Decimal | None = Field(
        None, gt=0, max_digits=12, decimal_places=2
    )

    tipo_veiculo: str | None = Field(None, max_length=50)

    ativo: bool | None = None