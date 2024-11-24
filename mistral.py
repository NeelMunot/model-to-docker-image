from huggingface_hub import snapshot_download
from pathlib import Path

def download_model(repo_id, save_directory, allow_patterns):
    snapshot_download(repo_id=repo_id, allow_patterns=allow_patterns, local_dir=save_directory)

if __name__ == "__main__":
    repo_id = "mistralai/Mistral-Nemo-Instruct-2407"
    save_directory = Path.home().joinpath('mistral_models', 'Nemo-Instruct')
    save_directory.mkdir(parents=True, exist_ok=True)
    allow_patterns = ["params.json", "consolidated.safetensors", "tekken.json"]
    download_model(repo_id, save_directory, allow_patterns)