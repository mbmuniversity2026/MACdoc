.. _architecture:

============
Architecture
============

MAC is built as a modern, containerised web application using a microservices
architecture. All services communicate over a shared Docker network.


Technology Stack
================

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Layer
     - Technology
   * - **Backend API**
     - Python 3.11, FastAPI 0.115, Uvicorn (async)
   * - **Database**
     - PostgreSQL 16 via SQLAlchemy 2.0 async (asyncpg)
   * - **Cache / Rate-limit**
     - Redis 7
   * - **Vector DB (RAG)**
     - Qdrant
   * - **Web Search**
     - SearXNG (self-hosted)
   * - **LLM Inference**
     - vLLM (GPU) -- primary; Ollama fallback
   * - **STT**
     - faster-whisper (CPU)
   * - **TTS**
     - Piper TTS via openedai-speech (CPU)
   * - **Frontend**
     - Vanilla JS SPA -- no build step, no framework
   * - **Code Editor**
     - Monaco Editor 0.52.2 (VS Code engine)
   * - **Reverse Proxy**
     - Nginx Alpine
   * - **Containerisation**
     - Docker Compose
   * - **Migrations**
     - Alembic
   * - **Authentication**
     - JWT (HS256) + bcrypt + scoped API keys


Docker Services
===============

All services run on a shared Docker network ``mac-net``:

.. list-table::
   :header-rows: 1
   :widths: 18 22 20 40

   * - Container
     - Image
     - Port
     - Purpose
   * - ``mac-api``
     - ``Dockerfile``
     - ``8001:8000``
     - FastAPI backend
   * - ``mac-nginx``
     - ``nginx:alpine``
     - ``80:80``
     - Reverse proxy + static frontend
   * - ``mac-postgres``
     - ``postgres:16-alpine``
     - ``5433:5432``
     - PostgreSQL database
   * - ``mac-redis``
     - ``redis:7-alpine``
     - ``6380:6379``
     - Redis cache
   * - ``mac-qdrant``
     - ``qdrant/qdrant``
     - ``6333:6333``
     - Vector database
   * - ``mac-searxng``
     - ``searxng/searxng``
     - ``8888:8080``
     - Web search engine
   * - ``mac-vllm-speed``
     - ``vllm/vllm-openai``
     - ``8001:8001``
     - GPU inference
   * - ``mac-whisper``
     - ``faster-whisper-server``
     - ``8005:8000``
     - Speech-to-text


Project Structure
=================

.. code-block:: text

   MAC/
   ├── mac/                        # FastAPI backend
   │   ├── main.py                 # App factory, 30+ routers
   │   ├── config.py               # Pydantic Settings (env vars)
   │   ├── database.py             # SQLAlchemy async engine
   │   ├── middleware/              # Auth, feature gates, rate limiting
   │   ├── models/                 # SQLAlchemy ORM models
   │   ├── routers/                # REST + WebSocket route modules
   │   ├── services/               # Business logic
   │   ├── schemas/                # Pydantic request/response schemas
   │   └── utils/                  # Security utilities
   ├── frontend/                   # Vanilla JS SPA (no build step)
   │   ├── index.html              # Entry point
   │   ├── style.css               # All CSS (~109 KB)
   │   ├── js/                     # Modular JS files
   │   │   ├── core.js             # Router, state management
   │   │   ├── auth.js             # Login/signup UI
   │   │   ├── chat.js             # AI Chat interface
   │   │   ├── notebooks.js        # Notebook functionality
   │   │   ├── mbmbook.js          # MBM Book IDE
   │   │   ├── admin.js            # Admin panel (part 1)
   │   │   ├── admin2.js           # Admin panel (part 2)
   │   │   ├── shell.js            # App chrome (sidebar, header)
   │   │   ├── dashboard.js        # Dashboard rendering
   │   │   ├── settings.js         # User settings
   │   │   ├── i18n.js             # 19-language translations
   │   │   └── ...                 # 19 total JS modules
   │   ├── libs/                   # Bundled JS libraries (offline-ready)
   │   ├── sw.js                   # Service worker (PWA)
   │   └── manifest.json           # PWA manifest
   ├── docker/
   │   └── workspace/              # MBM Book Docker image
   ├── alembic/                    # Database migrations
   ├── nginx/                      # Nginx configuration
   ├── docker-compose.yml          # Production compose file
   ├── docker-compose.worker.yml   # Worker node compose file
   ├── Dockerfile                  # Backend image
   ├── .env.example                # Configuration template
   ├── start-mac.bat               # Windows startup script
   └── mac-installer.iss           # Inno Setup installer script


Database Schema
===============

MAC uses PostgreSQL 16 with the following tables:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Table
     - Model File
     - Description
   * - ``users``
     - ``user.py``
     - Core user accounts with roles and quotas
   * - ``student_registry``
     - ``user.py``
     - Pre-registered student/faculty/admin entries
   * - ``refresh_tokens``
     - ``user.py``
     - JWT refresh token storage
   * - ``usage_logs``
     - ``user.py``
     - Per-request token usage logging
   * - ``rag_collections``
     - ``rag.py``
     - RAG document collections
   * - ``rag_documents``
     - ``rag.py``
     - Individual uploaded documents
   * - ``notebooks``
     - ``notebook.py``
     - Notebook metadata
   * - ``notebook_cells``
     - ``notebook.py``
     - Individual notebook cells
   * - ``doubt_posts``
     - ``doubt.py``
     - Forum questions
   * - ``doubt_answers``
     - ``doubt.py``
     - Forum answers
   * - ``shared_files``
     - ``file_share.py``
     - Uploaded shared files
   * - ``feature_flags``
     - ``feature_flag.py``
     - Feature toggle configuration
   * - ``guardrail_rules``
     - ``guardrail.py``
     - Content safety rules
   * - ``worker_nodes``
     - ``node.py``
     - Cluster worker nodes
   * - ``notifications``
     - ``notification.py``
     - User notifications
   * - ``audit_logs``
     - ``notification.py``
     - Administrative audit trail


Nginx Routing
=============

.. code-block:: nginx

   # Frontend SPA
   /                  → /app (index.html fallback)
   /static/*          → /app/ (7-day cache)
   /static/libs/*     → /app/libs/ (1-year immutable cache)
   /sw.js             → no-cache service worker

   # Backend API
   /api/*             → proxy_pass mac:8000 (rate-limited 10 req/s)
   /ws/*              → WebSocket proxy_pass mac:8000 (1h timeout)
   /docs              → FastAPI Swagger UI
   /redoc             → FastAPI ReDoc


Security Architecture
=====================

- **JWT Authentication**: HS256 algorithm, 24-hour access tokens, 30-day refresh tokens
- **Password Hashing**: bcrypt with automatic salt generation
- **Account Lockout**: Progressive lockout after failed login attempts
- **Rate Limiting**: Redis sliding window -- 100 requests/hour, 50K tokens/day per user
- **Scoped API Keys**: ``mac_sk_<hex>`` -- limited scope, individually revocable
- **Content Guardrails**: Admin-configurable rules checked before LLM calls
- **Kernel Isolation**: Code cells execute in Docker containers with resource limits
- **CORS**: Configurable via ``MAC_CORS_ORIGINS`` environment variable
- **XSS Protection**: HTML escaping via ``esc()`` helper throughout the frontend
