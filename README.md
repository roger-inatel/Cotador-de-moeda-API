<<<<<<< HEAD
# 💰 Sistema de Cotação de Moedas com CI/CD

[![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen)](https://github.com/roger-inatel/Testes_cotacao/actions)
[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-45-success)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-Relatório%20Gerado-brightgreen)](htmlcov/)

Sistema completo de cotação e conversão de moedas desenvolvido com foco em qualidade, testes abrangentes e pipeline CI/CD profissional.

## 🎯 Sobre o Projeto

Este projeto implementa um **sistema de cotação de moedas** com arquitetura limpa, separação de responsabilidades e cobertura completa de testes. Desenvolvido como parte da disciplina **C14 - Engenharia de Software** do Inatel.

### ✨ Funcionalidades

- 🔄 **Conversão entre moedas:** DOLLAR, EURO, REAL
- ✅ **Validação robusta** de entradas
- 🧮 **Cálculos precisos** de conversão
- 📊 **Interface de linha de comando** interativa
- 🔧 **Arquitetura modular** com classes especializadas

### 🏗️ Arquitetura

```
📁 Sistema de Cotação
├── 📄 CotacaoService      # Cotações das moedas
├── 📄 ConversorMoeda      # Lógica de conversão
├── 📄 ValidadorEntrada    # Validação de dados
└── 📄 CotadorApp          # Orquestração principal
```

## 🚀 Pipeline CI/CD

Sistema completo de **Continuous Integration/Continuous Deployment** implementado com **GitHub Actions**.

### 🔄 Jobs do Pipeline

| Job | Descrição | Duração | Status |
|-----|-----------|---------|--------|
| 🧪 **Testes** | 45 testes unitários com cobertura | ~30s | [![Tests](https://img.shields.io/badge/Status-Passing-brightgreen)](tests/) |
| 🔒 **Segurança** | Análise com Bandit + Safety | ~20s | [![Security](https://img.shields.io/badge/Status-Verified-brightgreen)](security/) |
| 📊 **Qualidade** | Black, Flake8, isort, MyPy | ~15s | [![Quality](https://img.shields.io/badge/Status-Checked-brightgreen)](quality/) |
| 🏗️ **Build** | Empacotamento e artefatos | ~25s | [![Build](https://img.shields.io/badge/Status-Success-brightgreen)](build/) |
| 📧 **Notificação** | Email automático | ~5s | [![Notification](https://img.shields.io/badge/Status-Sent-brightgreen)](notification/) |
| 🚀 **Deploy** | Simulação de deployment | ~10s | [![Deploy](https://img.shields.io/badge/Status-Ready-brightgreen)](deploy/) |

### ⚡ Características do Pipeline

- **✅ Execução Paralela:** Jobs independentes executam simultaneamente
- **📦 Artefatos:** Relatórios, pacotes e logs automaticamente salvos  
- **🔄 Cache Inteligente:** Dependências Python em cache para velocidade
- **📧 Notificações:** Email automático para roger.pereira@ges.inatel.br
- **🌍 Multi-Ambiente:** Suporte para diferentes ambientes de deploy

## 🧪 Testes

### 📊 Cobertura de Testes

- **✅ 45 Testes Unitários** implementados
- **🎯 4 Classes Testadas** completamente  
- **🔧 Mocks e Simulações** para cenários complexos
- **📈 Relatórios HTML** gerados automaticamente
- **⚡ Testes de Performance** incluídos

### 🔍 Tipos de Testes

#### **📋 Testes Básicos** (`test_cotacao.py`)
- Validação de cotações
- Conversões entre moedas  
- Validação de entradas
- Cenários positivos e negativos

#### **🚀 Testes Avançados** (`test_cotacao_avancado.py`)
- **Mocks e Patches** para simulação de APIs
- **Testes de Integração** completos
- **Cenários Extremos** (valores limites, erros)
- **Performance** e carga
- **Exception Handling** abrangente

### 🎯 Cenários Testados

```python
✅ Conversões válidas (DOLLAR ↔ EURO ↔ REAL)
✅ Valores inválidos (negativos, zero, strings)
✅ Moedas inexistentes (BITCOIN, YEN)
✅ Casos limite (valores muito grandes/pequenos)
✅ Mocks para APIs externas
✅ Tratamento de exceções
✅ Performance com 100+ conversões
✅ Integração end-to-end
```

## 🛠️ Tecnologias

### 🐍 Core
- **Python 3.13** - Linguagem principal
- **unittest** - Framework de testes nativo
- **mock/patch** - Simulação de dependências

### ⚙️ CI/CD
- **GitHub Actions** - Pipeline de automação
- **pytest** - Executor avançado de testes
- **pytest-cov** - Relatórios de cobertura
- **pytest-html** - Relatórios visuais

### 🔒 Qualidade
- **bandit** - Análise de segurança
- **safety** - Verificação de vulnerabilidades
- **black** - Formatação de código
- **flake8** - Linting
- **mypy** - Verificação de tipos

## 📁 Estrutura do Projeto

```
📁 Testes_cotacao/
├── 📁 .github/workflows/     # 🔄 Pipeline CI/CD
│   └── ci.yml                #    Configuração GitHub Actions
├── 📁 src/                   # 💻 Código fonte
│   └── cotacao.py            #    Classes principais
├── 📁 tests/                 # 🧪 Testes
│   ├── test_cotacao.py       #    Testes básicos (23 cenários)\n│   └── test_cotacao_avancado.py #  Testes avançados (22 cenários)
│   └── test_cotacao_avancado.py #  Testes avançados (mocks, integração)
├── 📁 scripts/               # 🛠️ Utilitários
│   └── send_notification.py  #    Sistema de notificação
├── 📄 README.md              # 📚 Documentação
└── 📄 .gitignore             # 🚫 Exclusões Git
```

## 🚀 Como Usar

### 1️⃣ **Instalação**

```bash
# Clone o repositório
git clone https://github.com/roger-inatel/Testes_cotacao.git
cd Testes_cotacao

# Configure ambiente virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate  # Windows
# ou: source .venv/bin/activate  # Linux/Mac

# Instale dependências de teste
pip install pytest pytest-html pytest-cov pytest-mock
```

### 2️⃣ **Executar Sistema**

```bash
# Executar aplicação interativa
python src/cotacao.py

# Exemplo de uso programático
python -c "
from src.cotacao import CotadorApp
app = CotadorApp()
app.executar('100', 'DOLLAR', 'EURO')
"
```

### 3️⃣ **Executar Testes**

```bash
# Todos os testes
python -m pytest tests/ -v

# Com relatório de cobertura
python -m pytest tests/ --cov=src --cov-report=html

# Só testes básicos
python -m pytest tests/test_cotacao.py -v

# Só testes avançados
python -m pytest tests/test_cotacao_avancado.py -v
```

### 4️⃣ **Relatórios**

```bash
# Gerar relatório HTML
python -m pytest tests/ --html=report.html --self-contained-html

# Ver cobertura no navegador
# Arquivo gerado em: htmlcov/index.html
```

## 📊 Exemplos de Uso

### 💻 **Uso Programático**

```python
from src.cotacao import CotadorApp

# Criar instância
app = CotadorApp()

# Conversões
app.executar('100', 'DOLLAR', 'EURO')    # 100 DOLLAR = 92.59 EURO
app.executar('50', 'EURO', 'REAL')       # 50 EURO = 270.00 REAL  
app.executar('200', 'REAL', 'DOLLAR')    # 200 REAL = 40.00 DOLLAR
```

### 🧪 **Testes com Mock**

```python
from unittest.mock import Mock
from src.cotacao import ConversorMoeda

# Mock do serviço de cotação
mock_service = Mock()
mock_service.buscar_cotacao.side_effect = [1.0, 1.08]

conversor = ConversorMoeda()
resultado = conversor.converter(100, 'DOLLAR', 'EURO', mock_service)
# Resultado: 92.59
```

## 📧 Sistema de Notificação

O pipeline inclui sistema completo de notificação por email:

### ✉️ **Funcionalidades**
- **📧 Email HTML** formatado profissionalmente
- **📊 Relatório detalhado** do pipeline
- **🔗 Links diretos** para GitHub Actions
- **📈 Métricas** de execução
- **⚙️ Configurável** via variáveis de ambiente

### 🔧 **Configuração** (Opcional)
```bash
# Para email real (opcional)
export SMTP_SERVER="smtp.gmail.com"
export SMTP_USER="seu-email@gmail.com"  
export SMTP_PASSWORD="sua-senha-app"
export EMAIL_DESTINO="roger.pereira@ges.inatel.br"

# Executar notificação manual
python scripts/send_notification.py
```

## 🎯 Requisitos Atendidos

### ✅ **Atividade CI/CD Completa**

| Requisito | Implementação | Status |
|-----------|---------------|--------|
| **20+ Testes Unitários** | 45 testes implementados | ✅ |
| **3+ Jobs Pipeline** | 6 jobs (testes, segurança, qualidade, build, notificação, deploy) | ✅ |
| **Empacotamento** | ZIP, TAR.GZ, relatórios | ✅ |
| **Execução Paralela** | Jobs independentes simultâneos | ✅ |
| **Notificação Email** | Sistema completo implementado | ✅ |
| **Artefatos** | Relatórios e pacotes salvos | ✅ |
| **Instalação Dependências** | Automática via pipeline | ✅ |

## 👥 Equipe

- **Roger Pereira** - roger.pereira@ges.inatel.br
  - Implementação do sistema de cotação
  - Pipeline CI/CD completo
  - Testes unitários e mocks
  - Sistema de notificação

## 🤝 Contribuição

Desenvolvido seguindo GitFlow com branches organizadas:

```bash
# Criar branch para nova feature
git checkout -b feature/nova-funcionalidade

# Fazer alterações e commits
git add .
git commit -m "feat: implementa nova funcionalidade"

# Push da branch
git push origin feature/nova-funcionalidade

# Merge no main após review
git checkout main
git merge feature/nova-funcionalidade
```

## 📜 Licença

Projeto desenvolvido para fins acadêmicos - **Inatel C14 - Engenharia de Software**
=======
# 💰 Cotador de Moedas API

Ferramenta de linha de comando para cotação de moedas e estatísticas simples usando Typer e Rich.

## 🎯 Atividade CI/CD com GitHub Actions

Este projeto foi desenvolvido para demonstrar um pipeline completo de CI/CD com as seguintes características:

### ✅ Requisitos Implementados:
- **20+ Testes Unitários** com mocks para APIs externas
- **Pipeline GitHub Actions** com 3 jobs principais:
  - 🧪 **Testes**: Execução de testes unitários com relatórios
  - 🏗️ **Build**: Empacotamento e geração de artefatos  
  - 📧 **Notificação**: Envio de email automático
- **Execução Paralela** de jobs
- **Armazenamento de Artefatos** (ZIP, TAR.GZ, relatórios)
- **Instalação Automática** de dependências no pipeline

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.13+
- pip ou poetry

### 1. Clone o repositório
```bash
git clone https://github.com/roger-inatel/Cotador-de-moeda-API.git
cd Cotador-de-moeda-API
```

### 2. Instale as dependências
```bash
# Usando pip
pip install typer rich requests pytest pytest-mock

# Ou usando poetry (se disponível)
poetry install
```

### 3. Execute os comandos

#### Cotação de Moedas
```bash
python src/cotacao.py cotacao 100 --moeda-origem USD --moeda-destino BRL
```

#### Estatísticas
```bash
python src/cotacao.py stats-cmd 1 2 3 4 5
```

#### Ajuda
```bash
python src/cotacao.py --help
```

## 🧪 Executar Testes

```bash
# Executar todos os testes
pytest tests/ -v

# Executar com relatório HTML
pytest tests/ -v --html=report.html --self-contained-html

# Executar com cobertura
pytest tests/ -v --cov=src --cov-report=html
```

## 🔄 Pipeline CI/CD

O pipeline é executado automaticamente nos pushes para `master` e inclui:

### Jobs do Pipeline:
1. **🧪 Testes Unitários**
   - Executa 22 cenários de teste
   - Gera relatórios HTML e XML
   - Calcula cobertura de código

2. **🏗️ Build e Empacotamento**
   - Cria arquivos ZIP e TAR.GZ
   - Gera artefatos para distribuição
   - Versionamento automático

3. **📧 Notificação**
   - Envia email com status do pipeline
   - Executa em paralelo com outros jobs
   - HTML e texto simples

4. **✅ Finalização**
   - Confirma sucesso de todos os jobs
   - Exibe estatísticas do pipeline

### Configuração de Email:
- **Email padrão:** roger.pereira@ges.inatel.br
- **Modo simulação** ativo por padrão
- **Secrets necessários:** SENDER_EMAIL, EMAIL_PASSWORD, EMAIL_DESTINO

## 📊 Testes Implementados

### Categorias de Teste:
- **Testes Funcionais**: Comandos de ajuda, validação de entrada
- **Testes com Mock**: Simulação de APIs externas, erros de rede
- **Testes de Estatísticas**: Cálculos matemáticos, casos extremos
- **Testes de Integração**: Fluxos completos, validação de URLs

### Cobertura:
- ✅ Cotação de moedas (USD→BRL, EUR→BRL)
- ✅ Tratamento de erros (timeout, conexão, HTTP)
- ✅ Validação de entrada (moedas inexistentes, valores especiais)
- ✅ Cálculos estatísticos (média, mediana, min, max)
- ✅ Comandos de linha (ajuda, argumentos inválidos)

## 🏗️ Estrutura do Projeto

```
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline GitHub Actions
├── src/
│   └── cotacao.py              # Código principal
├── tests/
│   └── test_cotacao_simples.py # Testes unitários
├── scripts/
│   └── send_notification.py    # Script de notificação
├── pyproject.toml              # Configuração do projeto
├── poetry.lock                 # Lock de dependências
└── README.md                   # Este arquivo
```

## 👥 Desenvolvedor

- **Implementação CI/CD:** Pipeline completo com testes, build e notificações
- **Branch:** feature/ci-cd-pipeline - Desenvolvimento seguindo GitFlow

## 📝 Notas da Atividade

Este projeto demonstra:
- ✅ **20+ cenários de teste** com mocks para APIs externas
- ✅ **3+ jobs no pipeline** (testes, build, notificação)  
- ✅ **Empacotamento automático** com artefatos
- ✅ **Execução paralela** implementada
- ✅ **Notificação por email** configurada
- ✅ **Instalação de dependências** no pipeline

### Tecnologias Utilizadas:
- **Python 3.13** - Linguagem principal
- **Typer** - Framework CLI
- **Rich** - Interface rica no terminal
- **Pytest** - Framework de testes
- **GitHub Actions** - CI/CD
- **ExchangeRate API** - Cotações de moeda

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

🚀 **Pipeline executado automaticamente a cada push!** 📧
>>>>>>> origin/master
