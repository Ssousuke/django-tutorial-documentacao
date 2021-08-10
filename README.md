## Seguindo o tutorial do django
### Criando um app de votação
#### Porque fiz esse tutorial?

Bom, já venho estudando django a alguns meses e todo conhecimento que vinha adiquirindo era de fontes como youtube ou tutoriais na internet. 
Após aprender o básico (criar um model, criar um crud, urls etc..) comecei a sentir bastante dificuldades quando queria fazer projetos mais avançados
como por exemplo meu projeto de faculdade [Info-Séries](https://github.com/Ssousuke/info-series/).
E com o objetivo de preencher as lacunas das informações que eu "pulei" eu resolvi ler a documentação do inicio e seguir o passo a paso fazendo anotações sobre cada detalhe importate do django.

## Importante

Nesse tutorial eu estou utilizando a versão de desenvolvimento do Django == 3.2.6

## Development

Ok, se quer testar o projeto, siga os próximos passos:

Crie um ambiente virtual:

```sh
python -m venv venv
```

Ative o ambiente virtual:

```sh
\venv\Scripts\Activate
```

Faça a instalação das dependências:

```sh
pip install -r requirements.txt
```

#### Crie as tabelas e runserver!

Crie as tabelas:

```sh
py manage.py makemigrations
```

Crie as migrações

```sh
py manage.py migrate
```
Runserver!

```sh
py manage.py runserver
```

## É isso, continua...

Vou continuar fazendo atualizações nesse codigo, adicionar testes e um template mais "amigavel". Certamente ainda tenho muito a aprender!
