from transformers import AutoModelForCausalLM, AutoTokenizer

def download_model(model_name, save_directory):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer.save_pretrained(save_directory)
    model.save_pretrained(save_directory)

if __name__ == "__main__":
    model_name = "mistralai/Mistral-Nemo-Instruct-2407"
    save_directory = "models/mistral-nemo-instruct-2407"
    download_model(model_name, save_directory)