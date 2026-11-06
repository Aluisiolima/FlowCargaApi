from enum import StrEnum


class StatusAgendamento(StrEnum):
    PENDENTE = "pendente"
    CONFIRMADO = "confirmado"
    EM_ANDAMENTO = "em_andamento"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"


class StatusDoca(StrEnum):
    DISPONIVEL = "disponivel"
    OCUPADA = "ocupada"
    MANUTENCAO = "manutencao"
    INATIVA = "inativa"


class StatusTransporte(StrEnum):
    SOLICITADO = "solicitado"
    EM_TRANSITO = "em_transito"
    AGUARDANDO_DESCARGA = "aguardando_descarga"
    DESCARREGANDO = "descarregando"
    FINALIZADO = "finalizado"
    CANCELADO = "cancelado"


class TipoUsuario(StrEnum):
    ADMINISTRADOR = "administrador"
    SUPERVISOR = "supervisor"
