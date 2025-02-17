import pytest
from fastapi.testclient import TestClient
from api import app  # A aplicação FastAPI
from models.empresa_model import Empresa  # Modelo da tabela Empresa
from database_test import db  # Sessão de banco de dados de teste

@pytest.fixture(scope="module")
def client():
    """Fixture para inicializar o cliente de teste"""
    with TestClient(app) as client:
        yield client




def test_create_empresa(client: TestClient, db):
    empresa_data = {
        "nome": "Empresa Teste Create",
        "cnpj": "67954514000157",
        "endereco": "Rua Teste, 123",
        "email": "empresa@teste.com",
        "telefone": "1234567890"
    }
    
    # Realiza a requisição para criar a empresa
    response = client.post("/empresas/", json=empresa_data)
    
    
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == empresa_data["nome"]
    assert data["cnpj"] == empresa_data["cnpj"]
    assert data["endereco"] == empresa_data["endereco"]
    assert data["email"] == empresa_data["email"]
    assert data["telefone"] == empresa_data["telefone"]
    assert "id" in data


def test_get_empresas(client: TestClient, db):
    # Adiciona uma empresa de teste diretamente no banco de dados
    empresa1 = Empresa(
        nome="Empresa Teste 1",
        cnpj="12345678901234",
        endereco="Rua Teste, 123",
        email="teste1@email.com",
        telefone="1234567890"
    )
    db.add(empresa1)
    db.commit()
    db.refresh(empresa1)

    empresa2 = Empresa(
        nome="Empresa Teste 2",
        cnpj="12345678901235",
        endereco="Rua Teste, 123",
        email="teste2@email.com",
        telefone="1234567890"
    )
    db.add(empresa2)
    db.commit()
    db.refresh(empresa2)

    # Realiza a requisição para listar todas as empresas
    response = client.get("/empresas/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0  # Certifica-se de que a empresa criada está na lista



def test_get_empresa(client: TestClient, db):
    empresa = Empresa(
        nome="Empresa Teste Get Empresa",
        cnpj="55590112000131",
        endereco="Rua Teste, 123",
        email="empresa@teste.com",
        telefone="1234567890"
    )
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    
    # Realiza a requisição para buscar a empresa pelo ID
    response = client.get(f"/empresas/{empresa.id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == empresa.id
    assert data["nome"] == empresa.nome
    assert data["cnpj"] == empresa.cnpj




def test_update_empresa(client: TestClient, db):
    empresa = Empresa(
        nome="Empresa Teste Update",
        cnpj="95476105000128",
        endereco="Rua Teste, 123",
        email="empresa@teste.com",
        telefone="1234567890"
    )
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    
    # Dados de atualização
    updated_data = {
        "nome": "Empresa Atualizada",
        "cnpj": "83416821000130",
        "endereco": "Rua Atualizada, 456",
        "email": "empresa_atualizada@teste.com",
        "telefone": "0987654321"
    }

    # Realiza a requisição para atualizar a empresa
    response = client.put(f"/empresas/{empresa.id}", json=updated_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == updated_data["nome"]
    assert data["endereco"] == updated_data["endereco"]
    assert data["email"] == updated_data["email"]
    assert data["telefone"] == updated_data["telefone"]



def test_delete_empresa(client: TestClient, db):
    empresa = Empresa(
        nome="Empresa Teste Delete",
        cnpj="90496159000131",
        endereco="Rua Teste, 123",
        email="empresa@teste.com",
        telefone="1234567890"
    )
    db.add(empresa)
    db.commit()
    db.refresh(empresa)

    empresa_id = empresa.id
    
    # Realiza a requisição para excluir a empresa
    response = client.delete(f"/empresas/{empresa_id}")

    assert response.status_code == 200

    response_check = client.get(f"/empresas/{empresa_id}")
    assert response_check.status_code == 404
    
    
