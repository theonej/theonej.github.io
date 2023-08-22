mkdir -p ~/data/milvus/conf
wget https://github.com/milvus-io/milvus/releases/download/v2.2.13/milvus-standalone-docker-compose.yml -O docker-compose.yml

docker-compose up -d
