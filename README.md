# recuperacao_consumo_api


Este repositorio foi criado com a finalidade de avaliação pratica sobre consumos de api.
Para a sua realização foram consultados diferentes arquivos disponibilizados pelo professor.
Para rodar o mesmo, deve-se realizar os seguintes passos:
 -a clonagem do repositorio, 
 -certificar-se que ele esta aberto no terminal, 
 -a preparação do ambiente virtual com o comando python -m venv .venv,
 -ativação do ambiente virtual com o comando .\.venv\Scripts\Activate.ps1,
 -com o ambiente ativado, instale as dependências registradas no projeto com o comando pip install -r requirements.txt
 -Para iniciar a API, execute: uvicorn app.main:app --reload
-Após a inicialização, o serviço estará disponível em:http://127.0.0.1:8000
-Para rodar o frontend deve-se utilizar o seguinte comando no terminal: python -m streamlit run frontend.py
