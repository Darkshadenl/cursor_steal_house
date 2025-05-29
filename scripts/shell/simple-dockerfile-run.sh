docker run --rm -it \
  --name stealhouse-crawler \
  --env-file ../../.env_docker \
  -e POSTGRES_USER="${POSTGRES_USER:?error}" \
  -e POSTGRES_PASSWORD="${POSTGRES_PASSWORD:?error}" \
  -e POSTGRES_DB="${POSTGRES_DB:?error}" \
  -e POSTGRES_PORT="${POSTGRES_PORT:?error}" \
  -e POSTGRES_HOST=db \
  -e VESTEDA_EMAIL="${VESTEDA_EMAIL:?error}" \
  -e VESTEDA_PASSWORD="${VESTEDA_PASSWORD:?error}" \
  -e DEEPSEEK_API_KEY="${DEEPSEEK_API_KEY}" \
  -e GOOGLE_API_KEY="${GOOGLE_API_KEY}" \
  -e CRAWLER_VERBOSE="${CRAWLER_VERBOSE}" \
  --network cursor_steal_house_default \
  stealhouse-crawler:latest