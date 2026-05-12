.. _getting-started:

===============
Getting Started
===============

System Requirements
===================

Before deploying MAC, ensure your system meets the following requirements:

.. list-table:: Minimum Requirements
   :header-rows: 1
   :widths: 30 70

   * - Component
     - Requirement
   * - **Operating System**
     - Windows 10/11, Ubuntu 20.04+, or macOS 12+
   * - **Docker Desktop**
     - Version 4.0+ with Docker Compose v2
   * - **RAM**
     - 8 GB minimum (16 GB recommended for LLM inference)
   * - **Storage**
     - 20 GB free disk space (50 GB with models)
   * - **GPU** *(optional)*
     - NVIDIA GPU with 8+ GB VRAM (e.g., RTX 3060 12 GB)
   * - **Network**
     - Campus LAN access (no internet required after initial setup)

.. tip::

   MAC runs in **CPU-only mode** without a GPU. All AI features remain functional,
   though inference will be slower. For production use with 50+ concurrent users,
   an NVIDIA RTX 3060 12 GB or better is strongly recommended.


Installation
============

Step 1: Clone the Repository
-----------------------------

.. code-block:: bash

   git clone https://github.com/mbmuniversity2026/MAC.git
   cd MAC

Step 2: Configure Environment
------------------------------

.. code-block:: bash

   cp .env.example .env

Edit the ``.env`` file and set at minimum:

.. code-block:: ini

   MAC_SECRET_KEY=<your-random-64-char-hex-string>
   MAC_ENV=development

.. important::

   The ``MAC_SECRET_KEY`` is used for JWT token signing. Generate a strong random
   key using: ``python -c "import secrets; print(secrets.token_hex(32))"``

Step 3: Start the Platform
---------------------------

**Windows (recommended):**

.. code-block:: batch

   start-mac.bat

**Linux / macOS:**

.. code-block:: bash

   docker compose up -d

This starts all services:

- ``mac-api`` -- FastAPI backend
- ``mac-nginx`` -- Reverse proxy + static frontend
- ``mac-postgres`` -- PostgreSQL 16 database
- ``mac-redis`` -- Redis 7 cache
- ``mac-qdrant`` -- Vector database for RAG
- ``mac-searxng`` -- Self-hosted web search
- ``mac-vllm-speed`` -- GPU inference engine (if GPU available)
- ``mac-whisper`` -- Speech-to-text engine

Step 4: Open in Browser
-------------------------

Navigate to:

.. code-block:: text

   http://localhost

You will see the MAC login page:

.. figure:: _static/screenshots/login_page.png
   :width: 100%
   :align: center
   :alt: MAC Login Page

   *The MAC login page with Sign In form, DOB verification link, and multi-language support.*

Step 5: First Login
--------------------

Use the development credentials to log in:

.. list-table::
   :header-rows: 1

   * - Role
     - Username
     - Password
   * - Admin
     - ``abhisek.cse@mbm.ac.in``
     - ``Admin@1234``
   * - Faculty
     - ``raj.cse@mbm.ac.in``
     - ``Faculty@1234``
   * - Student
     - ``21CS045``
     - ``Student@1234``


Building the MBM Book Workspace Image
======================================

If you plan to use the MBM Book cloud IDE, build the workspace image:

.. code-block:: bash

   docker build -t mbmbook-workspace:latest \
       -f docker/workspace/Dockerfile.lite docker/workspace/

This creates a ~6 GB image with runtimes for Python 3.11, Node.js 20, Java 17,
Go 1.22, Rust 1.95, C/C++, Ruby, and PHP. Build time is approximately 5 minutes.


Stopping the Platform
======================

**Windows:**

.. code-block:: batch

   stop-mac.bat

**Linux / macOS:**

.. code-block:: bash

   docker compose down

.. note::

   Data is persisted in Docker volumes (``pgdata``, ``redisdata``, ``qdrantdata``).
   Stopping and restarting the platform does not lose any data.
