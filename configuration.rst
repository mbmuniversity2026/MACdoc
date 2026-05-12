.. _configuration:

=============
Configuration
=============

All MAC configuration is managed through environment variables in the ``.env`` file.
The configuration is validated at startup using Pydantic Settings in ``mac/config.py``.


Core Settings
=============

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Variable
     - Default
     - Description
   * - ``MAC_ENV``
     - ``development``
     - Environment mode: ``development`` or ``production``
   * - ``MAC_SECRET_KEY``
     - *(required)*
     - JWT signing key -- must be a strong random string
   * - ``MAC_DEV_MODE``
     - ``false``
     - Enable mock LLM streaming (no GPU needed)
   * - ``APP_PORT``
     - ``80``
     - Port for the web interface


Database Configuration
======================

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Variable
     - Default
     - Description
   * - ``DATABASE_URL``
     - ``postgresql+asyncpg://mac:mac@postgres:5432/mac``
     - PostgreSQL connection string
   * - ``REDIS_URL``
     - ``redis://redis:6379/0``
     - Redis connection string


Authentication Settings
=======================

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Variable
     - Default
     - Description
   * - ``JWT_SECRET_KEY``
     - *(from MAC_SECRET_KEY)*
     - JWT signing key
   * - ``JWT_ACCESS_TOKEN_EXPIRE_MINUTES``
     - ``1440``
     - Access token lifetime (24 hours)


LLM Inference Settings
=======================

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Variable
     - Default
     - Description
   * - ``VLLM_BASE_URL``
     - ``http://vllm-speed:8001``
     - vLLM API endpoint
   * - ``VLLM_SPEED_MODEL``
     - ``Qwen/Qwen2.5-7B-Instruct-AWQ``
     - Default chat model
   * - ``OLLAMA_URL``
     - ``http://ollama:11434``
     - Ollama fallback endpoint
   * - ``MAC_ENABLED_MODELS``
     - ``qwen2.5:7b,...``
     - Comma-separated list of enabled models


External Services
=================

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Variable
     - Default
     - Description
   * - ``QDRANT_URL``
     - ``http://qdrant:6333``
     - Qdrant vector database URL
   * - ``SEARXNG_URL``
     - ``http://searxng:8080``
     - SearXNG web search URL
   * - ``WHISPER_URL``
     - ``http://whisper:8000``
     - Whisper STT URL


Rate Limiting
=============

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Variable
     - Default
     - Description
   * - ``RATE_LIMIT_REQUESTS_PER_HOUR``
     - ``100``
     - Maximum API requests per hour per user
   * - ``RATE_LIMIT_TOKENS_PER_DAY``
     - ``50000``
     - Maximum AI tokens per day per user
   * - ``KERNEL_TIMEOUT``
     - ``120``
     - Code execution timeout (seconds)


Cluster Settings
================

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Variable
     - Default
     - Description
   * - ``CLUSTER_SECRET``
     - *(optional)*
     - Shared secret for worker authentication
   * - ``CLUSTER_HOST``
     - *(optional)*
     - Host IP for worker nodes to connect to


CORS Settings
=============

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Variable
     - Default
     - Description
   * - ``MAC_CORS_ORIGINS``
     - ``*``
     - Allowed CORS origins (comma-separated)


GPU Configuration
=================

The vLLM service is configured in ``docker-compose.yml`` with these key settings:

.. code-block:: yaml

   mac-vllm-speed:
     image: vllm/vllm-openai:latest
     command: >
       --model Qwen/Qwen2.5-7B-Instruct-AWQ
       --gpu-memory-utilization 0.85
       --max-model-len 8192
     deploy:
       resources:
         reservations:
           devices:
             - driver: nvidia
               count: 1
               capabilities: [gpu]

.. tip::

   For an RTX 3060 12 GB, the AWQ-quantised Qwen2.5-7B model uses approximately
   5 GB of VRAM, leaving headroom for KV cache with ``--gpu-memory-utilization 0.85``.
