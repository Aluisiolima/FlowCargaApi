from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.core.repository import Transporte


class Carga(Base):
    __tablename__ = "cargas"

    descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    tipo_carga: Mapped[str | None] = mapped_column(String(100))
    peso_kg: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    quantidade: Mapped[int | None] = mapped_column(Integer)
    unidade_medida: Mapped[str | None] = mapped_column(String(30))
    origem: Mapped[str | None] = mapped_column(String(200))
    destino: Mapped[str | None] = mapped_column(String(200))
    nota_fiscal: Mapped[str | None] = mapped_column(String(50))
    observacoes: Mapped[str | None] = mapped_column(Text)

    transportes: Mapped[list["Transporte"]] = relationship(
        back_populates="carga"
    )