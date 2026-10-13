from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/")
def read_root():
    return {
        "app": "Flow Carga",
        "message": "Sistema de gerenciamento de transporte de cargas",
        "status": "online",
    }


@router.get("/empresas")
def listar_empresas():
    return {
        "empresas": [
            {"id": 1, "nome": "Transportadora Nordeste"},
            {"id": 2, "nome": "Logistica Brasil"},
            {"id": 3, "nome": "Carga Express"},
        ]
    }


@router.get("/empresas/{empresa_id}")
def consultar_empresa(empresa_id: int):
    return {
        "empresa_id": empresa_id,
        "nome": "Transportadora Nordeste",
        "cidade": "Teresina",
        "estado": "PI",
    }


@router.get("/motoristas")
def listar_motoristas():
    return {
        "motoristas": [
            {"id": 1, "nome": "Carlos Silva", "status": "disponivel"},
            {"id": 2, "nome": "Joao Santos", "status": "em_viagem"},
            {"id": 3, "nome": "Pedro Oliveira", "status": "disponivel"},
        ]
    }


# 5. Consultar informações de um motorista
@router.get("/motoristas/{motorista_id}")
def consultar_motorista(motorista_id: int):
    return {
        "motorista_id": motorista_id,
        "nome": "Carlos Silva",
        "veiculo": "Caminhao Truck",
        "placa": "ABC1D23",
        "status": "disponivel",
    }


@router.get("/cargas")
def listar_cargas():
    return {
        "cargas": [
            {
                "id": 1,
                "origem": "Teresina - PI",
                "destino": "Fortaleza - CE",
                "valor": 3200.00,
                "status": "disponivel",
            },
            {
                "id": 2,
                "origem": "Sao Luis - MA",
                "destino": "Recife - PE",
                "valor": 4500.00,
                "status": "agendada",
            },
        ]
    }


@router.get("/cargas/{carga_id}")
def consultar_carga(carga_id: int):
    return {
        "carga_id": carga_id,
        "produto": "Materiais de construcao",
        "peso": "12000 kg",
        "origem": "Teresina - PI",
        "destino": "Fortaleza - CE",
        "valor_frete": 3200.00,
        "status": "disponivel",
    }


@router.post("/entregas/agendar")
def agendar_entrega(carga_id: int, motorista_id: int, data_entrega: str):
    return {
        "message": "Entrega agendada com sucesso",
        "carga_id": carga_id,
        "motorista_id": motorista_id,
        "data_entrega": data_entrega,
        "status": "agendada",
    }


@router.put("/entregas/{entrega_id}/status")
def atualizar_status(entrega_id: int, status: str):
    return {
        "message": "Status atualizado com sucesso",
        "entrega_id": entrega_id,
        "novo_status": status,
    }


@router.get("/pagamentos/{motorista_id}")
def consultar_pagamentos(motorista_id: int):
    return {
        "motorista_id": motorista_id,
        "pagamentos": [
            {"carga_id": 1, "valor": 3200.00, "status": "pago"},
            {"carga_id": 2, "valor": 4500.00, "status": "pendente"},
        ],
        "total_recebido": 3200.00,
        "total_pendente": 4500.00,
    }
