Para criar um script de GitHub Actions que execute os testes unitários a cada push no repositório, você deve criar um arquivo de workflow no diretório `.github/workflows` do seu projeto. Vamos criar um arquivo chamado `python-app.yml` com o seguinte conteúdo:

```yaml
name: Python application test

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install Flask
    - name: Run tests
      run: |
        python -m unittest discover -s tests
```

### Explicação do Workflow:

1. **name**: Define o nome do workflow, neste caso "Python application test".

2. **on**: Especifica os eventos que acionarão o workflow. Aqui, ele é acionado por pushes e pull requests na branch `main`.

3. **jobs**: Define os jobs a serem executados. Este exemplo tem um único job chamado `build`.

4. **runs-on**: Especifica o tipo de máquina virtual em que o job será executado, neste caso, a última versão do Ubuntu.

5. **steps**: Define os passos a serem executados no job.

   - **actions/checkout@v2**: Uma action pré-definida para checar o repositório e acessar seu código.

   - **actions/setup-python@v2**: Configura o ambiente Python na versão especificada, neste caso, Python 3.8.

   - **Install dependencies**: Instala as dependências necessárias para sua aplicação, que no caso deste exemplo é apenas o Flask.

   - **Run tests**: Executa os testes unitários usando o `unittest`.

### Como Usar

1. Salve este conteúdo em um arquivo chamado `.github/workflows/python-app.yml` no seu repositório.

2. Faça push deste arquivo para o seu repositório no GitHub.

3. Agora, a cada push ou pull request para a branch `main`, o GitHub Actions executará este workflow, que instala as dependências necessárias e roda os testes unitários.

Certifique-se de ajustar o workflow conforme as necessidades do seu projeto, por exemplo, adicionando outras dependências necessárias para a execução dos testes.
