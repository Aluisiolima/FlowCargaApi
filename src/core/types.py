from enum import Enum


class StatusAgendamento(str, Enum):
    PENDENTE = "pendente"
    CONFIRMADO = "confirmado"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"


class StatusDoca(str, Enum):
    DISPONIVEL = "disponivel"
    OCUPADA = "ocupada"
    MANUTENCAO = "manutencao"
    INATIVA = "inativa"


class StatusTransporte(str, Enum):
    SOLICITADO = "solicitado"
    EM_TRANSITO = "em_transito"
    AGUARDANDO_DESCARGA = "aguardando_descarga"
    DESCARREGANDO = "descarregando"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"


class TipoUsuario(str, Enum):
    ADMINISTRADOR = "administrador"
    SUPERVISOR = "supervisor"
