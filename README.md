# wttd - eventex-darwin

Projeto para acompanhamento do curso Welcome to the Django e para algumas experiências malucas...

Sim isso é uma área de prototipação, não garanto nada aqui.

---
Sistema de eventos

[![Build Status](https://travis-ci.org/hugopenna/wttd.svg?branch=master)](https://travis-ci.org/hugopenna/wttd)

### Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.8+
3. Ative o virtualenv
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes


```console
git clone git@github.com:hugopenna/wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

### Como fazer deploy?

1. Crie uma instancia no heroku.
2. Envie as confiogurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minha instancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```