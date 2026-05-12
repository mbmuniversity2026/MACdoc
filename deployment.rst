.. _deployment:

==========
Deployment
==========

This section covers production deployment, worker node setup, and
the Windows installer.


Production Deployment
=====================

Step 1: Environment Configuration
-----------------------------------

.. code-block:: bash

   cp .env.example .env

Key production settings:

.. code-block:: ini

   MAC_ENV=production
   MAC_SECRET_KEY=<random-64-char-hex>        # REQUIRED: Change this!
   DATABASE_URL=postgresql+asyncpg://mac:mac_password@postgres:5432/mac_db
   REDIS_URL=redis://redis:6379/0

   # LLM Inference
   VLLM_BASE_URL=http://vllm-speed:8001
   VLLM_SPEED_MODEL=Qwen/Qwen2.5-7B-Instruct-AWQ

   # Optional services
   WHISPER_URL=http://whisper:8000
   QDRANT_URL=http://qdrant:6333
   SEARXNG_URL=http://searxng:8080

   # Rate limits
   RATE_LIMIT_REQUESTS_PER_HOUR=100
   RATE_LIMIT_TOKENS_PER_DAY=50000

Step 2: Start All Services
----------------------------

.. code-block:: bash

   docker compose up -d

Step 3: Run Database Migrations
---------------------------------

.. code-block:: bash

   docker exec mac-api alembic upgrade head

Step 4: Verify Health
-----------------------

.. code-block:: bash

   curl http://localhost/api/explore/health


Worker Node Setup (Multi-PC Cluster)
=====================================

MAC supports distributing GPU inference across multiple machines.

**Architecture:**

.. code-block:: text

   ┌──────────────────────────┐
   │ PC1 (Host)               │
   │ start-mac.bat            │
   │ All services + Qwen2.5   │
   │ IP: 192.168.1.100        │
   └──────────┬───────────────┘
              │ LAN
   ┌──────────┴───────────────┐
   │ PC2 (Worker)             │ PC3 (Worker)             │
   │ start-mac-worker.bat     │ start-mac-worker.bat     │
   │ Mistral-7B               │ Qwen2-VL-7B (Vision)     │
   └──────────────────────────┘──────────────────────────┘

**Setting Up a Worker:**

1. Clone the MAC repository on the worker machine
2. Copy ``.env.example`` to ``.env``
3. Set the host IP:

   .. code-block:: ini

      CLUSTER_HOST=192.168.1.100
      CLUSTER_SECRET=<same-secret-as-host>

4. Run:

   .. code-block:: batch

      start-mac-worker.bat

5. The worker auto-registers with the host via heartbeat


Windows Installer
=================

MAC includes an Inno Setup installer (``mac-installer.iss``) for one-click
deployment on Windows:

**Features:**

- Dual-mode installation: **Host** or **Worker**
- Automatic hardware detection (CPU, GPU, RAM, LAN IP)
- SSL certificate generation and system trust
- Firewall rule automation (ports 80, 443, 8000, 8001)
- Desktop shortcuts and start menu entries
- Interactive startup sequence with mascot animation


Docker Commands Reference
==========================

.. code-block:: bash

   # Start all services
   docker compose up -d

   # Rebuild API after code changes
   docker compose build mac
   docker compose up -d mac

   # Run migrations
   docker exec mac-api alembic upgrade head

   # View API logs
   docker logs mac-api -f

   # Access PostgreSQL CLI
   docker exec -it mac-postgres psql -U mac -d mac_db

   # Stop all services
   docker compose down

   # Stop and remove volumes (DESTRUCTIVE!)
   docker compose down -v


HTTPS Configuration
===================

For HTTPS support, MAC includes an Nginx HTTPS configuration:

1. Generate or obtain SSL certificates
2. Copy certificates to ``nginx/certs/``
3. Switch to the HTTPS Nginx config:

   .. code-block:: bash

      # In docker-compose.yml, change nginx volume:
      - ./nginx/nginx.https.conf:/etc/nginx/nginx.conf:ro

4. Restart Nginx:

   .. code-block:: bash

      docker compose restart nginx


Backup and Recovery
===================

**Database Backup:**

.. code-block:: bash

   docker exec mac-postgres pg_dump -U mac mac_db > backup.sql

**Database Restore:**

.. code-block:: bash

   docker exec -i mac-postgres psql -U mac mac_db < backup.sql

**Volume Backup:**

.. code-block:: bash

   docker run --rm -v pgdata:/data -v $(pwd):/backup \
       alpine tar czf /backup/pgdata.tar.gz /data
