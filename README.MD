🧬 COVID-19 Data Pipeline
📌 Visão Geral

Este projeto implementa um pipeline de dados completo para coletar, processar e analisar informações sobre casos de COVID-19.
O objetivo é demonstrar habilidades práticas de engenharia de dados, incluindo:

    Coleta automatizada de dados de fontes públicas (APIs e CSVs)

    Limpeza, transformação e enriquecimento dos dados

    Armazenamento otimizado em banco de dados relacional e/ou data lake

    Criação de relatórios e dashboards para análise exploratória

🧠 Objetivo do Projeto

O projeto foi desenvolvido para:

    Praticar conceitos fundamentais de ETL/ELT

    Aplicar boas práticas de modelagem e versionamento de dados

    Aprender a orquestrar tarefas de dados de forma automatizada

    Servir como base para futuros pipelines em escala

⚙️ Arquitetura do Pipeline
    A[📥 Coleta de Dados API / CSV] --> B[🧹 Limpeza e Transformação (Pandas / PySpark)]
    B --> C[(💾 Armazenamento PostgreSQL / Data Lake)]
    C --> D[📊 Visualização Power BI / Metabase / Tableau]


Etapas:
    Ingestão: dados coletados diariamente da API COVID-19 Dataset (https://www.kaggle.com/datasets/imdevskp/corona-virus-report)

    Transformação: padronização de nomes, datas, países e cálculo de métricas derivadas (médias móveis, taxa de mortalidade, etc).

    Carga: dados salvos em banco relacional (ex: PostgreSQL) e exportados para formato parquet no Data Lake.

    Visualização: criação de painéis interativos para acompanhamento da evolução global da pandemia.

🧰 Tecnologias Utilizadas
Linguagem:	Python
Coleta:	requests, pandas
Transformação:	pandas, numpy
<!-- Orquestração:	Apache Airflow  - futuramente -->
Armazenamento:	PostgreSQL / SQLite 
Visualização:	Power BI / Tableau
Controle de versão:	Git + GitHub
<!-- Ambiente	Docker - futuramente -->
🧩 Estrutura do Projeto
covid19-pipeline/
│

├── data/                  # Dados brutos e transformados

├── dags/                  # (futuramente) DAGs do Airflow

├── notebooks/             # Jupyter notebooks de exploração

├── src/

│   ├── extract.py         # Coleta e ingestão dos dados

│   ├── transform.py       # Limpeza e transformação

│   ├── load.py            # Armazenamento e carga final

│   └── utils.py           # Funções auxiliares

├── venv/                  # Configuração do ambiente virtual

├── requirements.txt       # Dependências do projeto

├── Dockerfile             # (futuramente) Configuração do container

├── README.md              # Documentação

└── dashboard.pbix         # Painel (Power BI ou Metabase export)

🚀 Como Executar Localmente
# 1. Clone o repositório
git clone https://github.com/mlugard/covid19-pipeline.git
cd covid19-pipeline

# 2. Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o pipeline
python src/extract.py
python src/transform.py
python src/load.py


💡 Caso utilize o Airflow, configure as DAGs no diretório dags/ e execute airflow webserver para orquestrar o pipeline.

📈 Exemplo de Resultados

Média móvel de novos casos por país

Taxa de mortalidade ao longo do tempo

Ranking de países por vacinação

Dashboard interativo (Power BI ou Metabase)

🧾 Próximos Passos

 Adicionar integração com API de vacinação

 Automatizar execução diária via Airflow

 Migrar armazenamento para AWS S3 + Redshift

 Disponibilizar API de consulta de dados tratados

👨‍💻 Autor

Marcelo Cabral
📍 Engenharia de Dados | Foco em Projetos Reais e Cloud

# 🔗 LinkedIn
