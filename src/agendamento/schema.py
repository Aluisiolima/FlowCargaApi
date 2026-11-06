from datetime import date, datetime, time
from typing import TYPE_CHECKING

from pydantic import Field

from src.core.base_schema import Base
from src.core.types import StatusAgendamento

if TYPE_CHECKING:
    from src.core.schemas import DocaResponse, SupervisorResponse, TransporteResponse


class AgendamentoResponse(Base):
    supervisor_id: int | None
    doca_id: int
    transporte_id: int

    data_agendamento: date
    horario_inicio: time
    horario_fim: time

    status: StatusAgendamento

    checkin_em: datetime | None = None
    inicio_descarga: datetime | None = None
    fim_descarga: datetime | None = None
    checkout_em: datetime | None = None

    observacoes: str | None = None
    motivo_cancelamento: str | None = None

    supervisor: SupervisorResponse | None = None
    doca: DocaResponse | None = None
    transporte: TransporteResponse | None = None


class AgendamentoCreate(Base):
    supervisor_id: int | None = Field(None, gt=0)
    doca_id: int = Field(..., gt=0)
    transporte_id: int = Field(..., gt=0)

    data_agendamento: date
    horario_inicio: time
    horario_fim: time

    status: StatusAgendamento = StatusAgendamento.PENDENTE

    observacoes: str | None = None


class AgendamentoUpdate(Base):
    supervisor_id: int | None = Field(None, gt=0)
    doca_id: int | None = Field(None, gt=0)
    transporte_id: int | None = Field(None, gt=0)

    data_agendamento: date | None = None
    horario_inicio: time | None = None
    horario_fim: time | None = None

    status: StatusAgendamento | None = None

    checkin_em: datetime | None = None
    inicio_descarga: datetime | None = None
    fim_descarga: datetime | None = None
    checkout_em: datetime | None = None

    observacoes: str | None = None
    motivo_cancelamento: str | None = None
