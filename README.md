# Projeto Kafka - Produtor e Consumidor com Cluster de Múltiplos Nós

## Integrantes da Equipe
- Gabriel Plagens
- Kauã Blass

---

## Passos para Instalação

1. **Pré-requisitos**:
   - Docker e Docker Compose instalados.
   - Python 3.x instalado (caso queira rodar scripts localmente).
   - Biblioteca `kafka-python` instalada:
     ```bash
     pip install kafka-python
     ```

2. **Configuração do Ambiente**:
   - Clone o repositório do projeto:
     ```bash
     git clone <URL_DO_REPOSITORIO>
     cd <PASTA_DO_PROJETO>
     ```
   - Inicie os serviços com Docker Compose:
     ```bash
     docker-compose up --build
     ```

---

## Passos para Realização das Etapas

### 1. Criação do Ambiente (Nós, Partição, Fator de Replicação)
   - Inicie o cluster com três brokers e ZooKeeper:
     ```bash
     docker-compose up --build
     ```
   - Crie um tópico com partição e fator de replicação:
     ```bash
     docker exec kafka1 kafka-topics --create \
       --bootstrap-server kafka1:9092 \
       --replication-factor 3 \
       --partitions 1 \
       --topic topico
     ```
   - Liste os tópicos para confirmar:
     ```bash
     docker exec kafka1 kafka-topics --list --bootstrap-server kafka1:9092
     ```

### 2. Produtor e Consumidor Normal (Todos os Nós Ativos)
   - Execute o produtor para enviar mensagens ao tópico:
     ```bash
     docker-compose up python-producer
     ```
   - Inicie o consumidor para receber mensagens:
     ```bash
     docker-compose up python-consumer
     ```

### 3. Produtor e Consumidor com Um dos Nós Offline
   - Derrube um dos brokers (por exemplo, `kafka3`):
     ```bash
     docker stop kafka3
     ```
   - Continue utilizando o produtor e consumidor. Verifique que o cluster permanece funcional devido ao fator de replicação.

### 4. Produtor e Consumidor com Adição de um Novo Nó
   - Adicione um novo broker ao cluster:
     - Edite o `docker-compose.yml` e adicione um serviço `kafka4` similar aos outros.
     - Inicie o novo nó:
       ```bash
       docker-compose up kafka4
       ```
   - Reconfigure o cluster para incluir o novo nó (opcional).

### 5. Consumidor com Leitura em Grupo
   - Configure múltiplos consumidores com o mesmo `GROUP_ID` para processar mensagens paralelamente:
     ```bash
     docker-compose up python-consumer
     docker-compose up python-consumer
     ```

---

## Novidades em Relação ao Exemplo de Aula

1. **Cluster Kafka Multi-Nó com Alta Disponibilidade**:
   - Configuração do cluster com fator de replicação.
   - Testes com falha de um nó e recuperação de dados.

2. **Adição de um Novo Nó ao Cluster**:
   - Demonstração de como expandir o cluster dinamicamente.

3. **Leitura em Grupo**:
   - Implementação de consumidores paralelos para processar mensagens em grupos.

4. **Integração com Kafka UI**:
   - Ferramenta visual para monitorar tópicos, mensagens e configuração do cluster.

5. **Scripts Customizados**:
   - Produtor e consumidor escritos em Python com personalização via variáveis de ambiente.

---

### Observações
- Todos os scripts foram desenvolvidos com boas práticas, incluindo manuseio de exceções e configuração modular.
- Para dúvidas, entre em contato com os autores via [email/contato].
