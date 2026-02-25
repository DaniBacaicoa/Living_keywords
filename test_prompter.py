from src.prompter import Prompter

prompter = Prompter(config_path="./config.yaml", model_type="qwen2.5:0.5b")

print(prompter.prompt("What is the capital of France?"))