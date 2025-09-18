# Projeto Kafka com Docker

Este projeto demonstra como configurar e executar um ambiente Apache Kafka utilizando Docker Compose, incluindo um produtor, consumidor e interface gráfica para monitoramento.

## Estrutura dos Serviços

- **Kafka**: Broker principal para publicação e consumo de mensagens.
- **ZooKeeper**: Serviço de coordenação necessário para o funcionamento do Kafka.
- **Kafka UI**: Interface web para monitorar tópicos, mensagens e consumidores.
- **Producer**: Serviço Python que gera dados fictícios e envia para um tópico Kafka.
- **Consumer**: Serviço Python que consome dados do tópico Kafka.

## Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Manduc4/kafka.git
   cd kafka
   ```

2. **Suba os containers:**
   ```bash
   docker-compose up -d
   ```

3. **Acesse a interface Kafka UI:**
   Abra o navegador em [http://localhost:8080](http://localhost:8080)

4. **Produtor e consumidor:**
   - O producer envia dados fictícios de temperatura para o tópico `temperature_sensor_topic`.
   - O consumer lê e exibe os dados recebidos.

## Configuração dos serviços

Veja o arquivo `docker-compose.yml` para detalhes das variáveis de ambiente e portas utilizadas.

## Requisitos

- Docker
- Docker Compose

## Exemplos de uso

- Monitorar tópicos e mensagens via Kafka UI
- Testar aplicações que dependem de mensageria
- Aprender sobre integração entre Python e Kafka

## Referências

- [Apache Kafka](https://kafka.apache.org/)
- [Bitnami Kafka Docker](https://hub.docker.com/r/bitnami/kafka)
- [Kafka UI](https://github.com/provectus/kafka-ui)
- [Faker](https://faker.readthedocs.io/en/master/)
- [kafka-python](https://github.com/dpkp/kafka-python)

---
