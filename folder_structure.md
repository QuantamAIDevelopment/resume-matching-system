resume-matching-system/
│
├── services/
│   ├── resume_parser/
│   │   ├── src/
│   │   │   ├── core/
│   │   │   │   ├── parsing/
│   │   │   │   │   ├── pdf_processor.py
│   │   │   │   │   ├── docx_processor.py
│   │   │   │   │   └── file_validator.py
│   │   │   │   ├── entities/
│   │   │   │   │   ├── resume_entities.py
│   │   │   │   │   └── entity_extractor.py
│   │   │   │   ├── exceptions/
│   │   │   │   │   └── parsing_errors.py
│   │   │   │   └── parser.py
│   │   │   ├── api/
│   │   │   │   ├── routers/
│   │   │   │   │   └── parsing_router.py
│   │   │   │   ├── middleware/
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── azure_ad_auth.py       # New: Azure AD integration
│   │   │   │   │   └── error_handler.py
│   │   │   │   ├── schemas/
│   │   │   │   │   └── parsing_schemas.py
│   │   │   │   └── dependencies.py
│   │   │   ├── config/
│   │   │   │   ├── settings.py
│   │   │   │   └── constants.py
│   │   │   ├── azure/                         # New: Azure-specific code
│   │   │   │   ├── blob_storage.py
│   │   │   │   └── telemetry.py
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   │   ├── test_pdf_processor.py
│   │   │   │   └── test_entity_extractor.py
│   │   │   ├── integration/
│   │   │   │   └── test_api_endpoints.py
│   │   │   └── conftest.py
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── entrypoint.sh
│   │
│   ├── job_processor/          # Similar structure to resume_parser
│   ├── embedding_service/
│   │   ├── src/
│   │   │   ├── core/
│   │   │   │   ├── embedders/
│   │   │   │   │   ├── sentence_embedder.py
│   │   │   │   │   ├── transformer_embedder.py
│   │   │   │   │   └── azure_openai_embedder.py      # New: Azure OpenAI embeddings
│   │   │   │   ├── cache/
│   │   │   │   │   ├── redis_cache.py
│   │   │   │   │   └── azure_cache_for_redis.py      # New: Azure Cache for Redis
│   │   │   │   └── embedding_manager.py
│   │   │   └── api/            # FastAPI components
│   ├── matching_service/
│   │   ├── src/
│   │   │   ├── core/
│   │   │   │   ├── similarity/
│   │   │   │   │   ├── faiss_manager.py
│   │   │   │   │   ├── azure_vector_search.py        # New: Azure Vector Search
│   │   │   │   │   └── hybrid_matcher.py
│   │   │   │   └── ranking/
│   │   │   │       └── score_calculator.py
│   ├── scoring_service/
│   │   ├── src/
│   │   │   ├── core/
│   │   │   │   ├── explainability/
│   │   │   │   │   └── score_explainer.py
│   │   │   │   └── validation/
│   │   │   │       └── score_validator.py
│   └── orchestrator/
│       ├── src/
│       │   ├── core/
│       │   │   ├── workflows/
│       │   │   │   ├── resume_matching_flow.py
│       │   │   │   └── error_handling.py
│       │   │   ├── agents/
│       │   │   │   └── agent_manager.py
│       │   │   └── message_bus/
│       │   │       ├── redis_pubsub.py
│       │   │       └── azure_service_bus.py          # New: Azure Service Bus
│       │   ├── api/
│       │   │   └── routers/
│       │   │       └── orchestration_router.py
│
├── infrastructure/
│   ├── docker/
│   │   ├── compose/
│   │   │   ├── dev/
│   │   │   │   └── docker-compose.dev.yml
│   │   │   ├── prod/
│   │   │   │   └── docker-compose.prod.yml
│   │   │   └── common/
│   │   │       └── .env.template
│   │   └── nginx/
│   │       ├── nginx.conf
│   │       └── ssl/
│   ├── k8s/
│   │   ├── base/
│   │   │   ├── orchestrator/
│   │   │   │   ├── deployment.yaml
│   │   │   │   └── service.yaml
│   │   │   ├── redis/
│   │   │   │   └── statefulset.yaml
│   │   │   └── kustomization.yaml
│   │   └── overlays/
│   │       ├── production/
│   │       │   ├── ingress/
│   │       │   │   └── ingress.yaml
│   │       │   └── kustomization.yaml
│   │       └── staging/
│   ├── azure/                                # New: Azure-specific infrastructure
│   │   ├── arm-templates/                    # Azure Resource Manager templates
│   │   │   ├── networking/
│   │   │   │   └── vnet.json
│   │   │   ├── container-apps/
│   │   │   │   └── service-deployment.json
│   │   │   ├── databases/
│   │   │   │   ├── cosmosdb.json
│   │   │   │   └── azure-postgresql.json
│   │   │   └── security/
│   │   │       └── keyvault.json
│   │   ├── bicep/                            # Modern alternative to ARM templates
│   │   │   ├── main.bicep
│   │   │   ├── modules/
│   │   │   │   ├── aks.bicep
│   │   │   │   ├── storage.bicep
│   │   │   │   └── networking.bicep
│   │   │   └── environments/
│   │   │       ├── dev.parameters.json
│   │   │       └── prod.parameters.json
│   │   └── scripts/
│   │       ├── deploy-azure-resources.ps1
│   │       └── create-service-principal.sh
│   ├── monitoring/
│   │   ├── prometheus/
│   │   │   ├── prometheus.yml
│   │   │   └── alert_rules.yml
│   │   ├── grafana/
│   │   │   ├── dashboards/
│   │   │   │   └── matching_dashboard.json
│   │   │   └── datasources/
│   │   │       └── prometheus.yaml
│   │   ├── azure-monitor/                    # New: Azure Monitor configuration
│   │   │   ├── dashboards/
│   │   │   │   └── matching_services_dashboard.json
│   │   │   ├── alerts/
│   │   │   │   └── service_health_alerts.json
│   │   │   └── log-analytics/
│   │   │       └── queries/
│   │   │           ├── performance_queries.kql
│   │   │           └── error_queries.kql
│   │   └── loki/
│   │       └── loki-config.yaml
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── aks/
│   │   │   ├── redis/
│   │   │   ├── azure_container_apps/         # New: Azure Container Apps
│   │   │   ├── azure_openai/                 # New: Azure OpenAI
│   │   │   ├── azure_key_vault/              # New: Azure Key Vault
│   │   │   └── monitoring/
│   │   ├── environments/
│   │   │   ├── prod/
│   │   │   │   ├── main.tf
│   │   │   │   └── variables.tf
│   │   │   └── dev/
│   │   └── providers.tf
│   └── iac-pipeline/                         # New: Infrastructure as Code pipelines
│       ├── azure-pipelines/
│       │   ├── terraform-pipeline.yml
│       │   └── bicep-pipeline.yml
│       └── github-actions/
│           └── terraform-deploy.yml
│
├── libs/
│   ├── database/
│   │   ├── postgres/
│   │   │   ├── connection_pool.py
│   │   │   └── migrations/
│   │   ├── azure_cosmos/                     # New: Azure Cosmos DB
│   │   │   ├── connection_manager.py
│   │   │   └── query_builder.py
│   │   ├── azure_sql/                        # New: Azure SQL Database
│   │   │   └── connection_manager.py
│   │   └── redis/
│   │       └── connection_manager.py
│   ├── llm/
│   │   ├── clients/
│   │   │   ├── mistral_client.py
│   │   │   ├── openai_client.py
│   │   │   └── azure_openai_client.py        # New: Azure OpenAI client
│   │   └── prompt_templates/
│   │       └── entity_extraction.jinja2
│   ├── cloud/                                # New: Cloud utilities
│   │   ├── azure/
│   │   │   ├── blob_storage.py
│   │   │   ├── key_vault.py
│   │   │   ├── container_registry.py
│   │   │   └── cognitive_services.py
│   │   └── common/
│   │       └── cloud_provider.py
│   └── utils/
│       ├── logging/
│       │   ├── structured_logger.py
│       │   ├── log_formatters.py
│       │   └── azure_app_insights.py         # New: Azure App Insights
│       ├── security/
│       │   ├── vault_integration.py
│       │   └── azure_key_vault.py            # New: Azure Key Vault integration
│       ├── tracing/                          # New: Distributed tracing
│       │   ├── open_telemetry.py
│       │   └── azure_app_insights_tracer.py
│       └── helpers.py
│
├── models/
│   ├── resume/
│   │   ├── resume_model.py
│   │   └── resume_schema.py
│   ├── job/
│   │   └── job_description_schema.py
│   └── matching/
│       └── score_model.py
│
├── docs/
│   ├── architecture/
│   │   ├── decisions/
│   │   │   ├── 001-why-redis-for-caching.md
│   │   │   └── 002-azure-services-selection.md   # New: Azure decisions
│   │   ├── diagrams/
│   │   │   ├── system_flow.puml
│   │   │   └── azure_architecture.puml           # New: Azure architecture diagram
│   │   └── style_guide.md
│   ├── azure/                                # New: Azure documentation
│   │   ├── cost-optimization.md
│   │   ├── security-compliance.md
│   │   └── scaling-strategy.md
│   ├── api/
│   │   └── openapi.yaml
│   └── deployment/
│       ├── aks_setup.md
│       ├── azure_container_apps_setup.md     # New: ACA documentation
│       └── disaster_recovery.md              # New: DR documentation
│
├── tests/
│   ├── e2e/
│   │   ├── test_full_workflow.py
│   │   └── data/
│   │       ├── sample_resumes/
│   │       └── sample_jds/
│   ├── performance/
│   │   ├── load_test.py
│   │   └── azure_load_testing/               # New: Azure Load Testing
│   │       ├── test_plan.jmx
│   │       └── azure_load_test_config.json
│   ├── integration/                          # New: Specific integration tests
│   │   └── azure/
│   │       ├── test_azure_openai.py
│   │       └── test_azure_storage.py
│   └── conftest.py
│
├── scripts/
│   ├── deployment/
│   │   ├── deploy_to_aks.sh
│   │   ├── deploy_to_azure_container_apps.sh  # New: ACA deployment
│   │   └── migrate_database.py
│   ├── data_processing/
│   │   └── seed_test_data.py
│   ├── monitoring/
│   │   ├── generate_metrics.sh
│   │   └── setup_azure_monitor_alerts.ps1     # New: Azure Monitor setup
│   └── security/                             # New: Security scripts
│       ├── rotate_secrets.sh
│       └── setup_managed_identities.ps1
│
├── .github/
│   └── workflows/
│       ├── ci-cd.yaml
│       ├── security-scan.yaml
│       ├── performance-test.yaml
│       └── azure-deployment.yaml              # New: Azure-specific workflow
│
├── azure-pipelines/                           # New: Azure DevOps pipelines
│   ├── build-pipeline.yml
│   ├── release-pipeline.yml
│   ├── infrastructure-pipeline.yml
│   └── templates/
│       ├── build-steps.yml
│       └── deploy-steps.yml
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── environment/
│       ├── .env.dev
│       └── .env.prod
│
├── .azure/                                    # New: Azure CLI configuration
│   └── config
│
├── .env
├── pyproject.toml
├── Makefile
├── README.md
└── requirements/
    ├── base.txt
    ├── azure.txt                              # New: Azure-specific packages
    └── service-requirements/
        ├── resume_parser.txt
        └── embedding_service.txt