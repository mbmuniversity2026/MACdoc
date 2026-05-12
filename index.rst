.. MAC documentation master file

===================================
MAC -- MBM AI Cloud Documentation
===================================

.. image:: _static/screenshots/mac_logo.png
   :width: 150px
   :align: center
   :alt: MAC Logo

|

**Self-Hosted AI Platform for MBM University, Jodhpur**

*Runs fully on the campus LAN -- No internet required -- No data leaves the institution*

.. note::

   **MAC** (MBM AI Cloud) is an open, on-premise AI platform built by the CSE Department
   of MBM University (Mugneeram Bangur Memorial University), Jodhpur, Rajasthan, India.
   It provides every student and faculty member access to large language models, a cloud IDE,
   document-aware AI chat, computational notebooks, and academic tools -- all running on
   hardware inside the campus, with zero subscription fees and no data sent outside.

----

.. toctree::
   :maxdepth: 3
   :caption: User Guide
   :numbered:

   getting_started
   authentication
   features
   student_guide
   faculty_guide
   admin_guide

.. toctree::
   :maxdepth: 3
   :caption: Technical Reference
   :numbered:

   architecture
   api_reference
   deployment
   configuration

.. toctree::
   :maxdepth: 2
   :caption: Appendices

   faq
   changelog
   license

----

Quick Reference
===============

.. list-table:: Default Development Credentials
   :header-rows: 1
   :widths: 15 30 25 30

   * - Role
     - Username / Roll No.
     - Password
     - DOB (for Verification)
   * - **Admin**
     - ``abhisek.cse@mbm.ac.in``
     - ``Admin@1234``
     - ``01011990``
   * - **Faculty**
     - ``raj.cse@mbm.ac.in``
     - ``Faculty@1234``
     - ``15061985``
   * - **Student**
     - ``21CS045``
     - ``Student@1234``
     - ``15082003``

.. warning::

   These are **development-only** credentials. In production, change all passwords
   immediately after first login. The platform enforces password change on first login
   via the ``must_change_password`` flag.

----

Indices and Tables
==================

* :ref:`genindex`
* :ref:`search`
