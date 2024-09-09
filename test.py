from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # Create the TestClient with the defined app

def test_process():
    with open("Relatório_de_fabricação_por_módulo_Projeto_Balcao.pdf", "rb") as file:  # Ensure you have a test.pdf file in the same directory
        response = client.post("/process", files={"post_file": file})

    print("Status Code:", response.status_code)  # Print the status code
    print("Response JSON:", response.json())  # Print the response JSON

    assert response.status_code == 200
    assert "parts" in response.json()
