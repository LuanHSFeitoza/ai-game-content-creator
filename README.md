🎮 Desafio Agentes IA | Geração de Roteiros e Thumbnails

Este repositório apresenta um desafio prático de IA para geração automática de roteiros e thumbnails para vídeos de videogames usando Crew AI e LangChain.

O objetivo é criar um sistema automatizado que:

Gere roteiros detalhados para vídeos de games.

Produza três opções de thumbnails inspiradas no roteiro.

Selecione a melhor thumbnail para cada vídeo.

🚀 Agentes e Funções
Agente	Função	Objetivo
Roteirista de Vídeo 📝	Pesquisa e elabora o roteiro do vídeo	Criação de roteiro completo para YouTube com storytelling, emojis e elementos criativos
Criador de Thumbnail 🎨	Gera 3 opções de thumbnails	Produzir thumbnails atrativas inspiradas no conteúdo do vídeo, focadas em público jovem
Revisor ✅	Integra e revisa roteiro + thumbnails	Ajusta inconsistências, melhora clareza e impacto, entrega versão final pronta para publicação
🛠️ Tecnologias usadas

Crew AI
 – Orquestração de múltiplos agentes com tarefas específicas

LangChain
 – Integração com LLM e ferramentas de busca

OpenAI API
 – Modelo de linguagem GPT-4o-mini

Streamlit
 – Interface web para entrada de usuário e visualização de resultados

📂 Estrutura do projeto
ai-game-content-creator/
│── app.py             # Interface Streamlit e kickoff do Crew
│── agents.py          # Definição dos agentes: Roteirista, Thumbnail, Revisor
│── tasks.py           # Tasks de criação de roteiro, thumbnails e integração
│── tools.py           # Ferramentas auxiliares (YouTube search, DuckDuckGo)
│── requirements.txt   # Dependências do projeto
│── README.md          # Este arquivo

▶️ Como executar

Clone o repositório:

git clone https://github.com/seuusuario/ai-game-content-creator.git
cd ai-game-content-creator


Configure as chaves de API:

export OPENAI_API_KEY="sua_chave_openai"


Execute o aplicativo:

streamlit run app.py


Digite o tema ou jogo desejado, por exemplo:

inputs = {'query': 'Melhores jogos de 2020'}

📌 Exemplo de fluxo

Entrada do usuário: "Melhores jogos de 2020"

Roteirista: Pesquisa vídeos e web, gera 3 roteiros criativos

Criador de Thumbnail: Produz 3 thumbnails inspiradas em cada roteiro

Revisor: Seleciona o roteiro final e a melhor thumbnail

Saída final: Roteiro + Thumbnail prontos para publicação no YouTube

💡 Observações

O sistema é modular: você pode adicionar novos agentes ou tarefas facilmente

A integração com Crew AI permite paralelizar tarefas e delegar responsabilidades

Pode ser expandido para incluir análise de SEO, títulos e descrições otimizadas
