# THERAPEUTIC GUIDELINES SMOKING

## Como rodar

### Crie uma network com nome net-host

```bash
docker network create \
--driver=bridge \
--subnet=172.35.0.0/24 \
--gateway=172.35.0.254 \
net-host
```

### Crie o arquivo .env como no exemplo abaixo

### Comando para criar os containers

```bash
docker compose up -d --build
```

### utilize o arquivo docs_summurize_retriever.ipynb para criar a coleção de vetores

## Logs

```bash
docker compose logs -f
```

## Shell python

```bash
docker compose exec api bash
Ipython
```

## Precommit

```bash
pre-commit run --all-files
```

## Bash do container

```bash
docker compose exec api bash
```

## dot env

```
APP_ENV="local"
USER_DOCS="docsdev"
PASSWORD_DOCS="ojdiqDwq5W%8j11M2@WNNIiAdsawe"

QDRANT_APIKEY="woXKPNeAD8uq1fVpLLPrDMX5AM4xyjAnLDPzszQuzZKFn"
QDRANT_HOST="tgs-qdrant"
QDRANT_HTTPS="0"
QDRANT_PORT="6333"

SECRET_KEY="OulLJiqkldb436-X6M11hKvr7wvLyG8TPi5PkLf4"

OPENAI_API_KEY=""
```
