# MAC — MBM AI Cloud Documentation

Official documentation for the **MAC (MBM AI Cloud)** platform — a self-hosted AI platform built by the CSE Department of MBM University, Jodhpur.

## Live Documentation

📖 **[View Documentation →](https://mbmuniversity2026.github.io/MACdoc/)**

## Building Locally

```bash
pip install -r requirements.txt
python -m sphinx -b html . _build/html
```

Then open `_build/html/index.html` in your browser.

## Deployment

This repository is automatically deployed to **GitHub Pages** via GitHub Actions.

Every push to `main` triggers a build and deploy cycle.

## License

MBM Open License v1.0 — See [LICENSE](LICENSE) for details.
