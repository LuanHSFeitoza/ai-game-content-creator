

import os
import streamlit as st


from crewai import Agent, Task, Crew, Process
from crewai.tools import BaseTool

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

# =====================================================
# --- Configurações Globais ---
# =====================================================
# Verifica a chave de API do OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("A variável de ambiente OPENAI_API_KEY não foi encontrada.")
os.environ["OPENAI_API_KEY"] = api_key

# Inicializa o modelo de linguagem
llm = ChatOpenAI(model="gpt-4o-mini")

# =====================================================
# --- Agents ---
# =====================================================

# --- Agent: Criação de Roteiros ---
createRoteiro = Agent(
    role="Especialista na criação de roteiros para vídeos de videogames",
    goal="Pesquise sobre {query} e crie roteiros detalhados para vídeos de games",
    backstory="""
        Você é um especialista em criação de roteiros de games. 
        Consulta vídeos, sites e ecossistemas de jogos. Cria roteiros criativos e descontraídos, 
        com storytelling e emojis, sempre embasados em pesquisa.
    """,
    verbose=True,
    llm=llm,
    max_iter=5,
    allow_delegation=False,
    memory=True
)

# --- Ferramentas de busca --- 

# Ferramenta para buscar vídeos do YouTube usando DuckDuckGo
class YouTubeSearchOnlyTool(BaseTool):
    name: str = "YouTube Search Tool"
    description: str = "Busca vídeos no YouTube apenas com search_query."

    def _run(self, query: str):
        search = DuckDuckGoSearchRun()
        results = search.run(f"site:youtube.com/ {query}")
        return results

youtube_search_tool = YouTubeSearchOnlyTool()

# Ferramenta para buscar notícias ou informações sobre jogos
class DuckSearchTool(BaseTool):
    name: str = "DuckDuckGo News Tool"
    description: str = "Busca notícias relacionadas a jogos usando DuckDuckGo"

    def _run(self, query: str):
        search = DuckDuckGoSearchRun(backend="news", num_results=10)
        results = search.run(query)
        return results

duck_search_tool = DuckSearchTool()

# =====================================================
# --- Tasks ---
# =====================================================

# Task: Gerar roteiros
generateRoteiros = Task(
    description="""
       Pesquisa vídeos e informações sobre o jogo. Seleciona 3 vídeos mais relevantes
       e realiza pesquisa adicional na web. Gera 3 opções de roteiro.
    """,
    expected_output="""
        Documento estruturado com:
        1. Resumo dos 3 vídeos (título, link, insights)
        2. Resumo da pesquisa web adicional
        3. Três roteiros distintos (título, estrutura narrativa, tom, duração)
    """,
    tools=[youtube_search_tool, duck_search_tool],
    agent=createRoteiro
)

# Agent: Criador de Thumbnails
createThumbnails = Agent(
    role="Especialista na criação de Thumbnails",
    goal="Transformar roteiros em thumbnails atrativas e criativas",
    backstory="""
        Designer especializado em Thumbnails de YouTube e redes sociais para público jovem.
        Foca em cores vibrantes, storytelling visual e uso de emojis estratégicos.
    """,
    verbose=True,
    llm=llm,
    max_iter=5,
    allow_delegation=False,
    memory=True
)

# Task: Gerar Thumbnails
generateThumbnails = Task(
    description="""
        Recebe roteiros e gera sugestões de thumbnails criativas, descontraídas e
        atrativas para público jovem.
    """,
    expected_output="""
        Lista de 3 thumbnails por roteiro, contendo:
        - Texto principal
        - Elementos visuais (cores, símbolos)
        - Emojis sugeridos
        - Estilo do design
        - Justificativa de atração
    """,
    agent=createThumbnails, 
    context=[generateRoteiros]
)

# Agent: Revisor e Integrador
agentRevisor = Agent(
    role="Gerente Revisor e Criador de Roteiro e Thumbnails",
    goal="Revisar e integrar roteiros e thumbnails em versão final pronta",
    backstory="""
        Gerente criativo especializado em revisão e unificação de conteúdos digitais.
        Alinha roteiros e thumbnails para clareza, coesão e engajamento.
    """,
    verbose=True,
    llm=llm,
    max_iter=5,
    allow_delegation=False,
    memory=True
)

# Task: Revisar e integrar Roteiros + Thumbnails
generateRoteiroEThumbnails = Task(
    description="""
        Recebe roteiros e thumbnails, ajusta inconsistências, melhora clareza e impacto,
        e unifica em documento final coerente.
    """,
    expected_output="""
         Documento final contendo:
         1. Roteiro revisado e aprimorado
         2. Thumbnails revisadas e finalizadas
    """,
    agent=agentRevisor, 
    context=[generateRoteiros, generateThumbnails]
)

# =====================================================
# --- Crew ---
# =====================================================
crew = Crew(
    agents=[createRoteiro, createThumbnails, agentRevisor],
    tasks=[generateRoteiros, generateThumbnails, generateRoteiroEThumbnails],
    verbose=True,
    process=Process.sequential,
    full_output=True,
    share_crew=False,
    manager_llm=llm,
    max_iter=10
)

# =====================================================
# --- Streamlit Interface ---
# =====================================================
query = st.text_input("Digite o nome do jogo ou tema:")

if st.button("Gerar conteúdo"):
    kickoff_args = {
        "query": query,  # usado pelo agent
        "youtube_search_tool": {"search_query": query}
    }

    with st.spinner("Gerando roteiros e thumbnails... Isso pode levar alguns segundos..."):
        result = crew.kickoff(kickoff_args)
        st.success("Conteúdo gerado com sucesso!")
        st.markdown(result.raw)
