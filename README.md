
**Roadmap Estruturado – Engenharia de Dados**

**Objetivo Geral**
Assegurar estrutura técnica, governança e acesso unificado aos dados de ferramentas externas para uso por agências, promovendo padronização, segurança e eficiência nos processos.

---

### 🧱 Fase 1 – Mapeamento e Inventário (jul/25)

#### 1. Mapear ferramentas de mídia utilizadas

* **Dificuldades técnicas**: ferramentas descentralizadas, falta de visibilidade.
* **Soluções**: levantamento via entrevistas e acessos, cronometragem dos fluxos.
* **Boas práticas**: planilha centralizada, Confluence por categoria.

#### 2. Documentar formas de ingestão (API, e-mail, manual)

* **Dificuldades**: fontes sem API ou sem padronização de envio.
* **Soluções**: classificar fontes por tipo de integração, criar plano de adequação.

#### 3. Identificar responsáveis por cada fonte

* **Dificuldades**: rotatividade de fornecedores ou contatos internos.
* **Soluções**: definir POC oficial por ferramenta.

#### 4. Criar estrutura inicial no Confluence

* **Soluções**: modelo-padrão com seções de acesso, origem, atualização, uso e exemplos.

---

### 🛠️ Fase 2 – Estrutura Técnica (ago-set/25)

#### 1. Definir arquitetura de ingestão (GCS, BigQuery, Airflow)

* **Dificuldades**: latência, custo, batch vs streaming.
* **Soluções**: Airflow com DAGs padronizadas, GCS como staging, BQ como destino final.
* **Boas práticas**: separação por ambiente e uso de labels.

#### 2. Mapear ferramentas prioritárias

* **Dificuldades**: APIs limitadas, falta de documentação.
* **Soluções**: uso de Postman, testes exploratórios, crédito de sandbox.

#### 3. Criar formato padrão de ingestão

* **Soluções**: definir schema JSON, versionamento de esquema, uso de Spark ou Pandas.
* **Boas práticas**: layout, nome de arquivo, pastas por data e origem.

#### 4. Implementar pipelines de ingestão

* **Dificuldades**: falhas silenciosas, timezones.
* **Soluções**: retries, logs detalhados, validação de "data freshness".

#### 5. Documentar estrutura de cruzamento

* **Soluções**: tabelas intermediárias, joins com ID padronizados, uso de modelo estrela.

---

### ⚙️ Fase 3 – Governança e Padronização (set-out/25)

#### 1. Definir políticas de acesso e controle

* **Soluções**: IAM com papéis restritos, uso de grupos e logging de acesso.

#### 2. Definir ciclo de vida dos dados

* **Soluções**: políticas de expurgo por tipo de dado, particionamento por data.

#### 3. Criar catálogo de dados

* **Soluções**: dbt docs, dicionário de dados no Confluence, padronização por camada (raw, refined, mart).

#### 4. Validar estrutura com stakeholders

* **Soluções**: walkthrough com time de mídia, revisão quinzenal.

---

### 🔁 Fase 4 – Automação (out-nov/25)

#### 1. Automatizar ingestão de fontes manuais

* **Soluções**: criar ingestores por e-mail (Gmail API), watchers de pasta (GCS trigger), rota de upload segura.

#### 2. Implementar monitoramento e alertas

* **Ferramentas**: Stackdriver, Cloud Logging, Slack para notificações.

#### 3. Criar testes de qualidade de dados

* **Ferramentas**: Great Expectations, validação via SQL com DAGs em Airflow.

#### 4. Automatizar rotinas de expurgo e atualização

* **Soluções**: jobs com TTL automático, DAGs semanais de limpeza.

---

### 📡 Fase 5 – Disponibilização para Agências (nov/25)

#### 1. Definir formato de entrega

* **Soluções**: BigQuery Authorized Views, arquivos com signed URL.
* **Boas práticas**: controle de granularidade e masking de dados sensíveis.

#### 2. Documentar acesso para agências

* **Soluções**: guias com screenshots, dicionário funcional.

#### 3. Implementar controle de acesso externo

* **Dificuldades**: pessoas externas acessando dados da organização.
* **Soluções**:

  * Validar com segurança se é permitido uso de contas externas.
  * Criar projeto isolado para agências.
  * Acesso somente via views ou arquivos temporários.
* **Boas práticas**: papéis restritos, auditoria ativa, uso de grupos do Google com expiração.

#### 4. Conduzir onboarding e sessões

* **Soluções**: gravação de onboarding, canal de suporte, revisão frequente do material de apoio.
