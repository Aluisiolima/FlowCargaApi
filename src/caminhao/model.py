from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base

if TYPE_CHECKING:
    from src.core.repository import Transporte


class Caminhao(Base):
    __tablename__ = "caminhoes"

    placa: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    marca: Mapped[str | None] = mapped_column(String(100))
    modelo: Mapped[str | None] = mapped_column(String(100))
    ano_fabricacao: Mapped[int | None] = mapped_column(Integer)
    capacidade_kg: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    tipo_veiculo: Mapped[str | None] = mapped_column(String(50))
    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    transportes: Mapped[list["Transporte"]] = relationship(back_populates="caminhao")
