# HackatonCodeML — Emotion Recognition

Projet de reconnaissance d'émotions à partir d'images utilisant PyTorch et ResNet18 fine-tuning.

**Dataset:** ~29k images d'entraînement / ~7k images de test

## 🚧 Status

Work in progress — le pipeline d'entraînement et l'évaluation évoluent encore.

## Quickstart

### 1. Créer un environnement virtuel (Python 3.12)

**Windows:**
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\activate
python -m pip install -U pip setuptools wheel
```

**macOS:**
```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
```

### 2. Installer les dépendances communes

```bash
pip install -r requirements.txt
```

### 3. Installer PyTorch (selon votre machine)

**Windows avec GPU NVIDIA (CUDA):**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**macOS (M1/M2/Intel):**
```bash
pip install torch torchvision torchaudio
```

## Règles d'équipe

- **Branches:** Travailler sur une branche par personne
- **Commits:** 1 changement par push
- **Format des messages de commit:**
  ```
  [old acc/loss] description du changement -> [new acc/loss]
  ```

## Documentation

- **Setup détaillé** (Jupyter kernel, environnements, GPU): [`docs/SETUP.md`](docs/SETUP.md)
- **Entraînement & comparaison**: [`docs/TRAINING.md`](docs/TRAINING.md)