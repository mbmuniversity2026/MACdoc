.. _changelog:

=========
Changelog
=========

All notable changes to MAC are documented in this file.
This project follows `Semantic Versioning <https://semver.org/>`_.

----

v2.0.0 -- 2026-04-29
=====================

Added
-----

- **Worker node support**: GPU/CPU contribution to cluster via ``docker-compose.worker.yml``
- **Windows installer**: Inno Setup 6 installer with HOST / WORKER role selection
- **Hardware scan wizard**: CPU, GPU, RAM, detected LAN IP, OS detection at install
- **SSL certificate generation**: Automatic certificate generation and system trust
- **Firewall automation**: Automatic firewall rule creation for ports 80, 443, 8000, 8001
- **Interactive installer**: Startup sequence with mascot animation
- **Kernel execution engine**: Code execution for notebook cells
- **Monaco Editor**: VS Code-powered code editor for notebooks
- **Registry role separation**: Admin / Faculty / Student roles in registry
- **Admin tab persistence**: Tab state preserved across sessions
- **Fullscreen mode**: Per-cell fullscreen editing for notebooks

Changed
-------

- Installer updated from v1.0.0 to v2.0.0 branding


v1.0.0 -- 2026-04-26
=====================

Added
-----

- **Initial release** of the self-hosted AI inference platform
- FastAPI backend with async SQLAlchemy + PostgreSQL
- Alembic database migrations (4 migration files)
- JWT authentication with role-based access control (student/faculty/admin)
- AI Chat with streaming responses via vLLM
- RAG pipeline (PDF/DOCX/TXT upload, Qdrant vector search)
- MBM Book cloud IDE with 25+ language kernels
- File sharing system
- Doubts forum (Q&A)
- File sharing (admin/faculty upload, student download)
- Admin dashboard with user CRUD, quotas, feature flags
- Worker node clustering for multi-PC GPU pool
- 19-language UI localisation
- Nginx reverse proxy with HTTPS support
- Docker Compose deployment stack
- PWA support (offline-capable, installable)
- Voice chat (Whisper STT + Veena TTS)
- Web search integration via SearXNG
- Content guardrails
- Notification and audit log system
- Academic structure management (branches, sections)
- Network tools (speed test, QR Wi-Fi join)
- Hardware monitoring (GPU/CPU/RAM live stats)
