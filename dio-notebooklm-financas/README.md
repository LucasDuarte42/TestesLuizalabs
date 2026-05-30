# 📚 Miniguia de Educação Financeira — Desafio NotebookLM | DIO

> **Desafio:** Criar um caderno temático no NotebookLM reunindo fontes abertas sobre finanças pessoais, elaborar perguntas estratégicas, testar variações de prompts e produzir um miniguia estruturado como resultado.
>
> **Trilha:** Python | Digital Innovation One (DIO)

---

## 🎯 Sobre o Projeto

Este repositório contém a entrega do desafio proposto pela DIO, que propõe o uso do **NotebookLM** como ferramenta de aprendizagem ativa. A ideia central é ir além da leitura passiva: organizar fontes, definir objetivos, elaborar perguntas e usar a IA para consolidar o conhecimento.

O tema escolhido foi **Educação Financeira Introdutória**, por ser relevante para qualquer pessoa — especialmente jovens em início de carreira.

---

## 📂 Estrutura do Repositório

```
dio-notebooklm-financas/
│
├── README.md                        ← você está aqui
├── miniguia_financeiro_DIO.docx     ← miniguia completo gerado
│
├── fontes/
│   └── links_fontes.md              ← fontes abertas utilizadas com descrição
│
└── prompts/
    └── prompts_estudo.md            ← biblioteca de prompts reutilizáveis
```

---

## 📖 Fontes Utilizadas

Todas as fontes são **abertas, gratuitas e em português**:

| # | Fonte | Tema Principal | Link |
|---|-------|---------------|------|
| 1 | Banco Central do Brasil — Caderno Cidadania Financeira | Orçamento, poupança, crédito | [bcb.gov.br/cidadaniafinanceira](https://www.bcb.gov.br/cidadaniafinanceira) |
| 2 | CVM — Portal do Investidor | Tipos de investimento, perfil de risco | [investidor.gov.br](https://www.investidor.gov.br) |
| 3 | ENEF — Vida e Dinheiro | Planejamento financeiro pessoal | [vidaedinheiro.gov.br](https://www.vidaedinheiro.gov.br) |
| 4 | Tesouro Direto — Como Funciona | Títulos públicos, Tesouro Selic/IPCA+ | [tesourodireto.com.br](https://www.tesourodireto.com.br/conheca/como-funciona.htm) |
| 5 | SERASA — Educação Financeira | Dívidas, score de crédito, recuperação financeira | [serasa.com.br/educacao-financeira](https://www.serasa.com.br/educacao-financeira) |

---

## 🎓 Objetivos de Estudo Definidos

- [x] Compreender os pilares da saúde financeira pessoal
- [x] Aprender a montar e seguir um orçamento mensal
- [x] Entender o que é reserva de emergência e como formá-la
- [x] Diferenciar dívida boa de dívida má
- [x] Conhecer os principais investimentos para iniciantes
- [x] Entender juros compostos e seu impacto no longo prazo
- [x] Usar IA (NotebookLM) como ferramenta de estudo ativo

---

## 🤖 Prompts Estratégicos Testados no NotebookLM

### Perguntas feitas ao caderno:

**1. Resumo inicial**
```
Com base nas fontes carregadas, quais são os 5 conceitos mais importantes
de educação financeira para um iniciante? Use linguagem simples.
```

**2. Comparativo entre fontes**
```
O que as fontes dizem sobre a poupança como investimento?
Há divergências entre elas?
```

**3. Aplicação prática**
```
Com base nas fontes, qual é o passo a passo recomendado para quem
quer começar a organizar as finanças do zero?
```

**4. Pensamento crítico**
```
Identifique possíveis limitações ou vieses nas fontes carregadas
sobre o tema de investimentos.
```

**5. Glossário**
```
Liste os 10 termos técnicos mais usados nas fontes e explique
cada um em uma frase simples.
```

---

## 📊 Variações de Prompts — O Que Funcionou Melhor

| Tipo de Prompt | Exemplo | Qualidade da Resposta |
|---|---|---|
| ❌ Genérico | "Explique educação financeira." | Superficial, sem aplicação |
| ✅ Com contexto | "Explique para um jovem de 20 anos com renda de R$ 2.000/mês." | Focada e prática |
| ✅ Com restrição | "Em 5 tópicos, sem jargão técnico." | Estruturada e acessível |
| ✅ Comparativo | "Compare o que as fontes dizem sobre poupança." | Gera análise crítica |
| ✅ Roleplay | "Você é um consultor financeiro gratuito. Me dê 3 dicas práticas." | Diretiva e contextualizada |

**Conclusão:** Prompts com **contexto + restrição de formato** geraram as melhores respostas. Prompts genéricos produziram respostas vagas e pouco úteis para o estudo.

---

## 📋 Miniguia — Conteúdo Produzido

O arquivo [`miniguia_financeiro_DIO.docx`](./miniguia_financeiro_DIO.docx) contém:

- **5 resumos estruturados** por tema (orçamento, reserva de emergência, dívidas, investimentos, juros compostos)
- **Glossário com 20 termos** explicados em linguagem simples
- **Biblioteca de 15+ prompts** organizados em 5 categorias
- **Plano de estudos de 4 semanas** com prompts por semana
- **Registro de variações de prompts** com análise de resultados

---

## 💡 Aprendizados do Desafio

1. **Qualidade das fontes importa muito** — fontes governamentais tendem a ser mais precisas, mas menos dinâmicas
2. **Prompt engineering faz diferença real** — a mesma pergunta com contexto diferente gera respostas completamente diferentes
3. **IA não substitui leitura** — o NotebookLM é mais útil para quem já leu as fontes e quer aprofundar
4. **Pensamento crítico é essencial** — a IA pode reproduzir limitações e vieses das próprias fontes
5. **Organização prévia acelera o estudo** — definir objetivos antes de usar a IA torna o processo muito mais produtivo

---

## 🛠️ Tecnologias e Ferramentas

![NotebookLM](https://img.shields.io/badge/NotebookLM-Google-4285F4?style=flat&logo=google)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=flat&logo=github)

- **NotebookLM** (Google) — caderno de IA com fontes carregadas
- **Python** — geração automatizada do miniguia em .docx
- **GitHub** — versionamento e entrega do projeto

---

## 🔗 Links do Projeto

- 📓 [Caderno no NotebookLM](https://notebooklm.google.com/notebook/63bf9276-f75d-4ce3-a6d6-e112cd9282e9)
- 📄 [Miniguia (.docx)](./miniguia_financeiro_DIO.docx)
- 🏫 [Repositório da trilha original — DIO](https://github.com/digitalinnovationone/trilha-python-dio)

---

## 👤 Autor

Feito com 💙 durante a **Trilha de Python da DIO**

[![GitHub](https://img.shields.io/badge/GitHub-seu--usuario-181717?style=flat&logo=github)](https://github.com/seu-usuario)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-seu--perfil-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/seu-perfil)

---

> *"A melhor hora para começar a cuidar do seu dinheiro foi ontem. A segunda melhor hora é agora."*
