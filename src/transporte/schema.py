from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import Field

from src.core.base_schema import Base
from src.core.types import StatusTransporte

if TYPE_CHECKING:
    from src.core.schemas import (
        AgendamentoResponse,
        CaminhaoResponse,
        CargaResponse,
        MotoristaResponse,
    )


class TransporteResponse(Base):
    motorista_id: int
    caminhao_id: int
    carga_id: int

    codigo_transporte: str | None = None
    data_saida: datetime | None = None
    previsao_chegada: datetime | None = None
    chegada_real: datetime | None = None

    status: StatusTransporte
    observacoes: str | None = None

    motorista: MotoristaResponse | None = None
    caminhao: CaminhaoResponse | None = None
    carga: CargaResponse | None = None

    agendamentos: list[AgendamentoResponse] = Field(default_factory=list)


class TransporteCreate(Base):
    motorista_id: int = Field(..., gt=0)
    caminhao_id: int = Field(..., gt=0)
    carga_id: int = Field(..., gt=0)

    codigo_transporte: str | None = Field(None, max_length=50)

    data_saida: datetime | None = None
    previsao_chegada: datetime | None = None
    chegada_real: datetime | None = None

    status: StatusTransporte = StatusTransporte.SOLICITADO

    observacoes: str | None = Field(None, max_length=200)


class TransporteUpdate(Base):
    motorista_id: int | None = Field(None, gt=0)
    caminhao_id: int | None = Field(None, gt=0)
    carga_id: int | None = Field(None, gt=0)

    codigo_transporte: str | None = Field(None, max_length=50)

    data_saida: datetime | None = None
    previsao_chegada: datetime | None = None
    chegada_real: datetime | None = None

    status: StatusTransporte | None = None

    observacoes: str | None = Field(None, max_length=200)
