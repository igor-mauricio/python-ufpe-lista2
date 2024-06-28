# Atividade da Lista 2 da disciplina de Python para Engenharia

## Validação
### Criação de Ambiente virtual (Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Instalação de dependências
```bash
pip install -r requirements.txt
```
### Rodar Testes
```bash
pytest
```
### Verificar Cobertura de Testes
```bash
coverage run -m pytest
coverage report -m
```

### Verificar Cobertura de testes em HTML
```bash
coverage html
```