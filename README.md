# Invest Aê — Assistente Virtual de Investimentos com IA

1. Sobre o projeto
2. Problema que queremos resolver
3. Objetivo do assistente
4. Como o assistente se comporta
5. Princípios de segurança / anti-alucinação

6. Arquitetura
   Usuário
      ↓
   Ollama / LLM
      ↓
   InvestorNeedInterpreter
      ↓
   InvestorNeed
      ↓
   Need Assessment
      ↓
   Eligibility Gate
      ↓
   Analysis Engine
      ↓
   Evidências / resposta

7. Responsabilidade da IA
   - interpretar linguagem natural
   - NÃO inventar dados
   - NÃO fazer cálculos financeiros
   - NÃO decidir com dados inexistentes

8. Base de conhecimento
   - fixture atual
   - proveniência
   - quality gate
   - futura integração com a base real do Invest Aê

9. Tecnologias
   - Python
   - Ollama
   - Qwen3 4B
   - pytest
   - JSON Schema

10. Estrutura do projeto

11. Como instalar
    python -m venv .venv
    pip install -e .
    pip install -r requirements-dev.txt

12. Como instalar/configurar Ollama
    ollama pull qwen3:4b

13. Como executar os testes
    python -m pytest -v

14. Exemplo real
    "Tenho R$ 500..."

15. Validação
    51 testes

16. Limitações atuais

17. Roadmap
    Fundação              ✅
    Interpretação IA      ✅
    Ollama                ✅
    Orquestração          ⏳
    Interface             ⏳
    Base real Invest Aê   ⏳

18. Relação com o desafio DIO
