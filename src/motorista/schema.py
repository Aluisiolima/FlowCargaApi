from src.core.base_schema import Base

from pydantic import Field, EmailStr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.core.schemas import TransporteResponse


class MotoristaResponse(Base):

    nome: str
    cpf: str
    cnh: str
    categoria_cnh: str | None = None
    telefone: str | None = None
    email: EmailStr | None = None
    ativo: bool

    transportes: list[TransporteResponse] = Field(default_factory=list)


class MotoristaCreate(Base):

    nome: str = Field(..., min_length=1, max_length=150)
    cpf: str = Field(..., min_length=11, max_length=11)
    cnh: str = Field(..., min_length=1, max_length=20)

    categoria_cnh: str | None = Field(None, max_length=5)
    telefone: str | None = Field(None, max_length=20)
    email: EmailStr | None = None

    senha: str = Field(..., min_length=8, max_length=128)

    ativo: bool = True


class MotoristaUpdate(Base):

    nome: str | None = Field(None, min_length=1, max_length=150)
    cpf: str | None = Field(None, min_length=11, max_length=11)
    cnh: str | None = Field(None, min_length=1, max_length=20)

    categoria_cnh: str | None = Field(None, max_length=5)
    telefone: str | None = Field(None, max_length=20)
    email: EmailStr | None = None

    senha: str | None = Field(None, min_length=8, max_length=128)

    ativo: bool | None = None