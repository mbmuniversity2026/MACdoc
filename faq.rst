.. _faq:

==========================
Frequently Asked Questions
==========================


General
=======

**What is MAC?**
   MAC (MBM AI Cloud) is a self-hosted AI platform that runs entirely on campus
   hardware. It provides AI chat, code notebooks, document analysis, and academic
   tools without requiring internet access or external cloud services.

**Does MAC require an internet connection?**
   No. After initial setup and model downloads, MAC runs entirely on the campus LAN.
   No data leaves the institution.

**What GPU do I need?**
   An NVIDIA GPU with 8+ GB VRAM is recommended (e.g., RTX 3060 12 GB).
   MAC also works in CPU-only mode, though inference will be slower.

**Can other institutions use MAC?**
   Yes! MAC is released under the MBM Open License. Any educational institution
   can fork, deploy, and customise it for their needs.


Authentication
==============

**I forgot my password. How do I reset it?**
   Contact your administrator. They can reset your password from the Admin Panel
   under the Users tab.

**What is the DOB verification?**
   New users must verify their identity using their Registration Number and
   Date of Birth (in DDMMYYYY format) before creating an account. This ensures
   only registered students and faculty can access the platform.

**What happens if I enter the wrong password too many times?**
   Your account will be temporarily locked. Contact your administrator to unlock it.


AI Chat
=======

**Which AI models are available?**
   The default deployment includes Qwen2.5-7B-Instruct-AWQ. Additional models
   can be added via worker nodes (e.g., Mistral-7B, Qwen2-VL-7B for vision).

**What does "Web Search" do in the chat?**
   When enabled, the platform searches the web via SearXNG (self-hosted search)
   and includes relevant results as context for the AI's response.

**Can I upload documents to the chat?**
   Yes! Use the paperclip icon to upload PDF, DOCX, or TXT files. The AI will
   use the document content as context for its responses.

**What are the usage limits?**
   Default limits are 100 API requests per hour and 50,000 tokens per day.
   Administrators can adjust these limits per user.


MBM Book
========

**What programming languages are supported?**
   Python, JavaScript, TypeScript, R, Julia, Ruby, PHP, C, C++, Java, Go, Rust,
   C#, Kotlin, Scala, Swift, Bash, SQL, Lua, Octave, Haskell, Perl, Zig, and more.

**Do I need to install anything for MBM Book?**
   No. All language runtimes are pre-installed in the Docker workspace image.
   The admin must build the workspace image once using the provided Dockerfile.


Troubleshooting
===============

**The platform is slow. What can I do?**
   - Check GPU utilisation from the Hardware page
   - Verify that the vLLM container is running: ``docker ps | grep vllm``
   - Reduce ``--gpu-memory-utilization`` if OOM errors occur
   - Add worker nodes for additional GPU capacity

**I can't access the platform from another computer.**
   Ensure you're accessing via the server's LAN IP (not ``localhost``).
   Check that port 80 is open in the firewall.

**Docker containers won't start.**
   - Verify Docker Desktop is running
   - Check available disk space (need 20+ GB free)
   - Run ``docker compose logs`` to see error messages
   - Ensure the ``.env`` file is properly configured

**The AI is not responding.**
   - Check if the vLLM container is running: ``docker logs mac-vllm-speed``
   - Verify GPU is detected: ``nvidia-smi``
   - Try enabling ``MAC_DEV_MODE=true`` for mock responses (debugging)
