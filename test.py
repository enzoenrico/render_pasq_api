import requests

def make_post_request_with_pdf(filepath):
    url = "http://localhost:8080/process"
    # url = "https://render-pasq-api.onrender.com/ponga"
    print(url)
    # files = {'post_file': open(filepath, 'rb')}
    with open(filepath, "rb") as f:
        # r = requests.post(url, files={"post_file": f})
        r = requests.get(url, files={"post_file": f})
        print(r.json())

make_post_request_with_pdf("./Relatório_de_fabricação_por_módulo_Projeto_Balcao.pdf")
