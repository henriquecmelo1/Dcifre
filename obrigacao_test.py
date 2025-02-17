import pytest
from fastapi.testclient import TestClient
from api import app  # Importa a aplicação FastAPI
from obrigacao_model import Obrigacao  # Modelo da tabela Obrigacao
from database_test import db  # Sessão de banco de dados de teste
from empresa_model import Empresa  


@pytest.fixture(scope="module")
def client():
    """Fixture para inicializar o cliente de teste"""
    with TestClient(app) as client:
        yield client

def create_empresa(db):
    empresa = Empresa(nome="Empresa Teste")
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    return empresa


def test_create_obrigacao(client: TestClient, db):
    
    empresa = create_empresa(db)

    obrigacao_data = {
        "nome": "Obrigação Teste Create",
        "periodicidade": "Mensal",
        "empresa_id": empresa.id  
    }

    response = client.post("/obrigacoes/", json=obrigacao_data)

    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == obrigacao_data["nome"]
    assert data["periodicidade"] == obrigacao_data["periodicidade"]
    assert "id" in data


def test_get_obrigacoes(client: TestClient, db):
    empresa = create_empresa(db)
    obrigacao1 = Obrigacao(nome="Obrigação Teste 1", periodicidade="Anual", empresa_id=empresa.id)
    db.add(obrigacao1)
    db.commit()
    db.refresh(obrigacao1)

    obrigacao2 = Obrigacao(nome="Obrigação Teste 2", periodicidade="Mensal", empresa_id=empresa.id)
    db.add(obrigacao2)
    db.commit()
    db.refresh(obrigacao2)

    response = client.get("/obrigacoes/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


def test_get_obrigacao(client: TestClient, db):
    empresa = create_empresa(db)
    obrigacao = Obrigacao(nome="Obrigação Teste Get", periodicidade="Trimestral", empresa_id=empresa.id)
    db.add(obrigacao)
    db.commit()
    db.refresh(obrigacao)

    response = client.get(f"/obrigacoes/{obrigacao.id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == obrigacao.id
    assert data["nome"] == obrigacao.nome
    assert data["periodicidade"] == obrigacao.periodicidade


def test_update_obrigacao(client: TestClient, db):
    empresa = create_empresa(db)
    obrigacao = Obrigacao(nome="Obrigação Teste Update", periodicidade="Semanal", empresa_id=empresa.id)
    db.add(obrigacao)
    db.commit()
    db.refresh(obrigacao)

    updated_data = {
        "nome": "Obrigação Atualizada",
        "periodicidade": "Diária",
        "empresa_id": 1
    }

    response = client.put(f"/obrigacoes/{obrigacao.id}", json=updated_data)

    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == updated_data["nome"]
    assert data["periodicidade"] == updated_data["periodicidade"]


def test_delete_obrigacao(client: TestClient, db):
    empresa = create_empresa(db)
    obrigacao = Obrigacao(nome="Obrigação Teste Delete", periodicidade="Bimestral", empresa_id=empresa.id)
    db.add(obrigacao)
    db.commit()
    db.refresh(obrigacao)

    obrigacao_id = obrigacao.id

    response = client.delete(f"/obrigacoes/{obrigacao_id}")
    assert response.status_code == 200

    response_check = client.get(f"/obrigacoes/{obrigacao_id}")
    assert response_check.status_code == 404