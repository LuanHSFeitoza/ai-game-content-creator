# 🎮 Desafio Agentes IA | Geração de Roteiros e Thumbnails

Este repositório apresenta um **desafio prático de IA** para geração automática de roteiros e thumbnails para vídeos de videogames usando **Crew AI** e **LangChain**.

O objetivo é criar um sistema automatizado que:  
1. Gere roteiros detalhados para vídeos de games.  
2. Produza **três opções de thumbnails** inspiradas no roteiro.  
3. Selecione a melhor thumbnail para cada vídeo.

---

## 🚀 Agentes e Funções

| Agente | Função | Objetivo |
|--------|--------|----------|
| **Roteirista de Vídeo** 📝 | Pesquisa e elabora o roteiro do vídeo | Criação de roteiro completo para YouTube com storytelling, emojis e elementos criativos |
| **Criador de Thumbnail** 🎨 | Gera 3 opções de thumbnails | Produzir thumbnails atrativas inspiradas no conteúdo do vídeo, focadas em público jovem |
| **Revisor** ✅ | Integra e revisa roteiro + thumbnails | Ajusta inconsistências, melhora clareza e impacto, entrega versão final pronta para publicação |

---

## 🛠️ Tecnologias usadas

- [Crew AI](https://www.crewai.ai/) – Orquestração de múltiplos agentes com tarefas específicas  
- [LangChain](https://www.langchain.com/) – Integração com LLM e ferramentas de busca  
- [OpenAI API](https://platform.openai.com/) – Modelo de linguagem GPT-4o-mini  
- [Streamlit](https://streamlit.io/) – Interface web para entrada de usuário e visualização de resultados  

---

## 📂 Estrutura do projeto

```plaintext
ai-game-content-creator/
│── app.py             # Interface Streamlit e kickoff do Crew
│── agents.py          # Definição dos agentes: Roteirista, Thumbnail, Revisor
│── tasks.py           # Tasks de criação de roteiro, thumbnails e integração
│── tools.py           # Ferramentas auxiliares (YouTube search, DuckDuckGo)
│── requirements.txt   # Dependências do projeto
│── README.md          # Este arquivo
