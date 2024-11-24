from huggingface_hub import snapshot_download, login
from pathlib import Path

login(token="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")
mistral_models_path = Path.home().joinpath('mistral_models', 'Nemo-Instruct')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-Nemo-Instruct-2407", allow_patterns=["params.json", "consolidated.safetensors", "tekken.json"], local_dir=mistral_models_path)
