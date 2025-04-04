import os
from pathlib import Path

def create_structure(base_path, structure):
    for item in structure:
        full_path = os.path.join(base_path, item)
        if item.endswith('/'):
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
        else:
            dir_name = os.path.dirname(full_path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
            Path(full_path).touch()
            print(f"Created file: {full_path}")

project_structure = [
    # Root
    'resume-matching-system/',
    
    # Services
    'resume-matching-system/services/',
    'resume-matching-system/services/resume_parser/',
    'resume-matching-system/services/resume_parser/src/',
    'resume-matching-system/services/resume_parser/src/core/',
    'resume-matching-system/services/resume_parser/src/core/parsing/',
    'resume-matching-system/services/resume_parser/src/core/parsing/pdf_processor.py',
    'resume-matching-system/services/resume_parser/src/core/parsing/docx_processor.py',
    'resume-matching-system/services/resume_parser/src/core/parsing/file_validator.py',
    'resume-matching-system/services/resume_parser/src/core/entities/',
    'resume-matching-system/services/resume_parser/src/core/entities/resume_entities.py',
    'resume-matching-system/services/resume_parser/src/core/entities/entity_extractor.py',
    'resume-matching-system/services/resume_parser/src/core/exceptions/',
    'resume-matching-system/services/resume_parser/src/core/exceptions/parsing_errors.py',
    'resume-matching-system/services/resume_parser/src/core/parser.py',
    'resume-matching-system/services/resume_parser/src/api/',
    'resume-matching-system/services/resume_parser/src/api/routers/',
    'resume-matching-system/services/resume_parser/src/api/routers/parsing_router.py',
    'resume-matching-system/services/resume_parser/src/api/middleware/',
    'resume-matching-system/services/resume_parser/src/api/middleware/auth.py',
    'resume-matching-system/services/resume_parser/src/api/middleware/azure_ad_auth.py',
    'resume-matching-system/services/resume_parser/src/api/middleware/error_handler.py',
    'resume-matching-system/services/resume_parser/src/api/schemas/',
    'resume-matching-system/services/resume_parser/src/api/schemas/parsing_schemas.py',
    'resume-matching-system/services/resume_parser/src/api/dependencies.py',
    'resume-matching-system/services/resume_parser/src/config/',
    'resume-matching-system/services/resume_parser/src/config/settings.py',
    'resume-matching-system/services/resume_parser/src/config/constants.py',
    'resume-matching-system/services/resume_parser/src/azure/',
    'resume-matching-system/services/resume_parser/src/azure/blob_storage.py',
    'resume-matching-system/services/resume_parser/src/azure/telemetry.py',
    'resume-matching-system/services/resume_parser/src/__init__.py',
    'resume-matching-system/services/resume_parser/src/main.py',
    'resume-matching-system/services/resume_parser/tests/',
    'resume-matching-system/services/resume_parser/tests/unit/',
    'resume-matching-system/services/resume_parser/tests/unit/test_pdf_processor.py',
    'resume-matching-system/services/resume_parser/tests/unit/test_entity_extractor.py',
    'resume-matching-system/services/resume_parser/tests/integration/',
    'resume-matching-system/services/resume_parser/tests/integration/test_api_endpoints.py',
    'resume-matching-system/services/resume_parser/tests/conftest.py',
    'resume-matching-system/services/resume_parser/Dockerfile',
    'resume-matching-system/services/resume_parser/requirements.txt',
    'resume-matching-system/services/resume_parser/entrypoint.sh',
    
    # Other services
    'resume-matching-system/services/job_processor/',
    'resume-matching-system/services/embedding_service/',
    'resume-matching-system/services/embedding_service/src/',
    'resume-matching-system/services/embedding_service/src/core/',
    'resume-matching-system/services/embedding_service/src/core/embedders/',
    'resume-matching-system/services/embedding_service/src/core/embedders/sentence_embedder.py',
    'resume-matching-system/services/embedding_service/src/core/embedders/transformer_embedder.py',
    'resume-matching-system/services/embedding_service/src/core/embedders/azure_openai_embedder.py',
    'resume-matching-system/services/embedding_service/src/core/cache/',
    'resume-matching-system/services/embedding_service/src/core/cache/redis_cache.py',
    'resume-matching-system/services/embedding_service/src/core/cache/azure_cache_for_redis.py',
    'resume-matching-system/services/embedding_service/src/core/embedding_manager.py',
    
    # Infrastructure
    'resume-matching-system/infrastructure/docker/compose/dev/docker-compose.dev.yml',
    'resume-matching-system/infrastructure/docker/compose/prod/docker-compose.prod.yml',
    'resume-matching-system/infrastructure/docker/nginx/nginx.conf',
    'resume-matching-system/infrastructure/k8s/base/orchestrator/deployment.yaml',
    'resume-matching-system/infrastructure/azure/arm-templates/networking/vnet.json',
    
    # Libs
    'resume-matching-system/libs/database/postgres/connection_pool.py',
    'resume-matching-system/libs/llm/clients/azure_openai_client.py',
    
    # Models
    'resume-matching-system/models/resume/resume_model.py',
    
    # Tests
    'resume-matching-system/tests/e2e/test_full_workflow.py',
    
    # Scripts
    'resume-matching-system/scripts/deployment/deploy_to_aks.sh',
    
    # Documentation
    'resume-matching-system/docs/architecture/decisions/001-why-redis-for-caching.md',
    
    # Root files
    'resume-matching-system/.env',
    'resume-matching-system/pyproject.toml',
    'resume-matching-system/Makefile',
    'resume-matching-system/README.md',
    
    # Add all remaining files following the same pattern...
]

if __name__ == '__main__':
    base_dir = os.getcwd()
    create_structure(base_dir, project_structure)
    print("Project structure created successfully!")