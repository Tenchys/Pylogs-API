# Repository Overview

## Project Description
- **Purpose**: Centralized log and client management API.
- **Main goal**: Expose CRUD endpoints for logs and client data, persist them in PostgreSQL, and provide health checks.
- **Key technologies**: FastAPI, SQLAlchemy, PostgreSQL, Uvicorn, Pydantic.

## Architecture Overview
- **FastAPI**: Entry point handling all HTTP traffic.
- **Router layer**: Separates routes into `health`, `log`, and `cliente` modules.
- **Service layer**: Encapsulates business logic and async calls to data access.
- **Infrastructure layer**: ORM entities and data‑access helpers that directly interact with SQLAlchemy sessions.
- **Database**: PostgreSQL accessed via SQLAlchemy.
- **Health endpoint**: Simple status check.

Data flow: HTTP request → router → service (business logic) → infra (DB operations) → response.

## Directory Structure
- `src/` – Core application code.
  - `app.py`: FastAPI app bootstrap.
  - `config/`: DB configuration, startup helpers.
  - `health/`: Health check endpoint and model.
  - `log/`: Log CRUD – router, service, infra, models.
  - `Cliente/`: Client CRUD – router, service, infra, models.
- `requirements.txt`: Python dependencies.
- `dependencies.txt`: Same list for `pip install -r`.
- `README.md`: High‑level documentation.
- `LICENSE`: MIT license.
- `AGENTS.md`: This guide.

## IA Rules
1. **Lenguage**: IA will response to user in Spanish.
2. **Environment**: the bash session always set the python virtual environment run the next command "source .venv/bin/activate"

## Subagents (YAML List)
- id: QATecnico
  description: QA Tecnico que revisara todo el proyecto.
  prompt: Actua como un senior developer y entregas un informe en formato yaml que contenga:
    - malas parcticas en el proyecto
    - que no respete el pep 8 sobre el acuerdo de nombres (clases,metodos, variables)
    - codigo que tenga mucha complejidad.

- id: GeneraPlanTecnico
  description: Genera un plan de trabajo segun lo respondido por el subagente QATecnico
  prompt: Actua como un senior developer y segun el el informe del QATecnico (-{QATecnico}) genera un plan de trabajo que este dividido en pequeñas tareas que cubra todos los fallos que aparecen en el informe del QATecnico, el formato del plan debe ser un yaml y este debe ser guardado en el directorio IA que se encuentra en la raiz del proyecto y el nombre del archivo debe ser plan.yaml (IA/plan.yaml), si la carpeta no existe, creala, cada tarea debe tener un id de tarea, la descripcion de la tarea, los pasos para llevar a cabo la tarea, y el estado de la tarea ("porHacer", "completado").

- id: ReviewPlan
  description: Revisa el IA/plan.yaml y ve cuales son las tareas que estan completadas, actualizando el estado de las tareas
  prompt: Actua como un senior developer y revisa el IA/plan.yaml y ve cuales son las tareas que estan completadas, actualizando el estado de la tareas en el archivo IA/plan.yaml.

## Development Workflow
1. **Environment**
   ```bash
   pip install -r dependencies.txt
   ```
2. **Run**
   ```bash
   uvicorn src.app:app --reload
   ```
3. **Tests** – *(not yet implemented)*
4. **Linting**
   ```bash
   pre-commit run --all-files
   ```
5. **Formatting** – Uses black via pre‑commit.

All changes should pass lint and tests before merging.

