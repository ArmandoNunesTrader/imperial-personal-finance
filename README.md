# Aplicativo Imperial Personal Finance
    Aplicativo de Finanças Pessoais desenvolvido em Python 
        utilizando Clean Architectureeze

## 1. Configurações Iniciais
    Criando o ambiente virtual
        python.exe -m venv venv
    Criar o arquivo .gitignore padrão
    Criar o arquivo .flake8 padrão
    Criar e configurar o arquivo .vscode/settings.json
    Criar o arquivo .pre-commit-config.yaml padrão

## 2. Pacotes Inicias Padrão
    pip install flake8
    python.exe -m pip install --upgrade pip (vai pedir após 1ª instalação)
    pip install pre-commit
    pre-commit install

## 3. Exportar dependências
    pip freeze > requirements.txt

## 4. Testes
    pytest -s -v <DIR>\SUBDIR\FILE.PY 

    pytest (varre todos os subdiretórios)