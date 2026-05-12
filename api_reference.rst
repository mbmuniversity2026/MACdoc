.. _api-reference:

=============
API Reference
=============

MAC exposes a RESTful API via FastAPI. All endpoints are prefixed with ``/api/``
in the browser (Nginx strips the prefix before proxying to FastAPI).

**Base URL:** ``http://<server-ip>/api/``

**Authentication:** Include the ``Authorization: Bearer <token>`` header on all
protected endpoints.


Authentication Endpoints
========================

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Method
     - Endpoint
     - Description
   * - ``POST``
     - ``/auth/verify``
     - Verify registration number + DOB for first-time sign-up
   * - ``POST``
     - ``/auth/login``
     - Login with roll number/email + password
   * - ``POST``
     - ``/auth/refresh``
     - Refresh an expired access token
   * - ``POST``
     - ``/auth/signup``
     - Create a new user account
   * - ``GET``
     - ``/auth/me``
     - Get current user profile
   * - ``PATCH``
     - ``/auth/me``
     - Update current user profile
   * - ``POST``
     - ``/auth/change-password``
     - Change current user's password
   * - ``POST``
     - ``/auth/logout``
     - Logout (blacklist token)


Admin User Endpoints
--------------------

.. list-table::
   :header-rows: 1
   :widths: 10 35 55

   * - Method
     - Endpoint
     - Description
   * - ``GET``
     - ``/auth/admin/users``
     - List all users (admin only)
   * - ``POST``
     - ``/auth/admin/users``
     - Create a new user (admin only)
   * - ``PATCH``
     - ``/auth/admin/users/{id}``
     - Update a user (admin only)
   * - ``PATCH``
     - ``/auth/admin/users/{id}/role``
     - Change user role (admin only)
   * - ``PATCH``
     - ``/auth/admin/users/{id}/status``
     - Toggle user active status (admin only)


Registry Endpoints
------------------

.. list-table::
   :header-rows: 1
   :widths: 10 35 55

   * - Method
     - Endpoint
     - Description
   * - ``GET``
     - ``/auth/admin/registry``
     - List all registry entries
   * - ``POST``
     - ``/auth/admin/registry``
     - Add a single registry entry
   * - ``POST``
     - ``/auth/admin/registry/bulk``
     - Bulk-add registry entries (JSON)
   * - ``POST``
     - ``/auth/admin/registry/upload``
     - Upload registry CSV file
   * - ``DELETE``
     - ``/auth/admin/registry/{id}``
     - Delete a registry entry


AI Query Endpoints
==================

.. list-table::
   :header-rows: 1
   :widths: 10 25 65

   * - Method
     - Endpoint
     - Description
   * - ``POST``
     - ``/query/chat``
     - Send a chat message (streaming or non-streaming)
   * - ``POST``
     - ``/query/completion``
     - Text completion
   * - ``POST``
     - ``/query/embed``
     - Generate text embeddings
   * - ``POST``
     - ``/query/rerank``
     - Rerank search results
   * - ``POST``
     - ``/query/stt``
     - Speech-to-text transcription
   * - ``POST``
     - ``/query/tts``
     - Text-to-speech synthesis
   * - ``GET``
     - ``/query/models``
     - List available AI models


RAG Endpoints
=============

.. list-table::
   :header-rows: 1
   :widths: 10 35 55

   * - Method
     - Endpoint
     - Description
   * - ``GET``
     - ``/rag/collections``
     - List RAG collections
   * - ``POST``
     - ``/rag/collections``
     - Create a new collection
   * - ``POST``
     - ``/rag/collections/{id}/upload``
     - Upload document to collection
   * - ``POST``
     - ``/rag/collections/{id}/search``
     - Search within a collection


Notebook Endpoints
==================

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Method
     - Endpoint
     - Description
   * - ``GET``
     - ``/notebooks``
     - List user's notebooks
   * - ``POST``
     - ``/notebooks``
     - Create a new notebook
   * - ``GET``
     - ``/notebooks/{id}``
     - Get notebook with cells
   * - ``PUT``
     - ``/notebooks/{id}``
     - Update notebook
   * - ``DELETE``
     - ``/notebooks/{id}``
     - Delete a notebook
   * - ``WS``
     - ``/ws/notebook/{id}``
     - WebSocket for code execution


WebSocket Protocol (Notebooks)
------------------------------

.. code-block:: json

   // Client → Server
   { "type": "execute", "cell_id": "uuid", "code": "...", "language": "python" }
   { "type": "interrupt", "kernel_id": "..." }
   { "type": "ping" }

   // Server → Client
   { "type": "status", "cell_id": "...", "execution_state": "busy|idle" }
   { "type": "stream", "cell_id": "...", "name": "stdout|stderr", "text": "..." }
   { "type": "error", "cell_id": "...", "ename": "...", "evalue": "...", "traceback": [] }
   { "type": "pong" }


Additional Endpoints
====================

.. list-table::
   :header-rows: 1
   :widths: 15 25 60

   * - Router
     - Prefix
     - Description
   * - ``explore``
     - ``/explore``
     - Model discovery, health checks, usage stats
   * - ``search``
     - ``/search``
     - Web search via SearXNG
   * - ``doubts``
     - ``/doubts``
     - Forum posts and answers
   * - ``files``
     - ``/files``
     - File sharing upload/download
   * - ``features``
     - ``/features``
     - Feature flag management
   * - ``guardrails``
     - ``/guardrails``
     - Content safety rules
   * - ``hardware``
     - ``/hardware``
     - System hardware metrics
   * - ``network``
     - ``/network``
     - Network info and speed test
   * - ``academic``
     - ``/academic``
     - Branches and sections
   * - ``nodes``
     - ``/nodes``
     - Worker node management
   * - ``cluster``
     - ``/cluster``
     - Cluster overview
   * - ``keys``
     - ``/keys``
     - API key management
   * - ``scoped-keys``
     - ``/scoped-keys``
     - Scoped API key management
   * - ``usage``
     - ``/usage``
     - Usage logs and analytics
   * - ``notifications``
     - ``/notifications``
     - User notifications
   * - ``system``
     - ``/system``
     - System configuration
   * - ``setup``
     - ``/setup``
     - First-boot setup


Interactive API Documentation
=============================

MAC includes built-in interactive API documentation:

- **Swagger UI**: ``http://<server-ip>/docs``
- **ReDoc**: ``http://<server-ip>/redoc``

These are served directly by FastAPI and provide a complete, interactive reference
for all API endpoints with request/response schemas.
