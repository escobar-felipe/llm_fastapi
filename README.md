# THERAPEUTIC GUIDELINES SMOKING

## Como rodar

```bash
docker compose up -d --build
```

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
