from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

str_model = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(str_model)
model = AutoModelForCausalLM.from_pretrained(str_model)

def generate_response(prompt, history):
    curr_input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
    cons_input_ids = torch.cat([history, curr_input_ids], dim = -1) if history is not None else curr_input_ids
    bot_output_ids = model.generate(cons_input_ids, max_length = 1000, pad_token_id=tokenizer.eos_token_id)
    bot_response = tokenizer.decode(bot_output_ids[:, cons_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response, bot_output_ids

conv_history = None
while True:
    prompt1 = input("User: ")
    if (prompt1 == "exit"):
        break
    response, conv_history = generate_response(prompt1, conv_history)
    print("ChatBot: ", response)