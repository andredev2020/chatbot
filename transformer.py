

# Hugging Face PyTorch Interface for Transformers
!pip3 install -q transformers   
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import sys


class ANN_TRANSFORMER:
    
    def __init__(self):
        self.ModelName = "microsoft/DialoGPT-medium"
        self.Tokenizer = AutoTokenizer.from_pretrained(self.ModelName)
        self.Model = AutoModelForCausalLM.from_pretrained(self.ModelName)
        
    def answer(self, response, history):
        # encode the user input (response) and add end of string token, return pytorch tensor
        input_ids = self.Tokenizer.encode(response + self.Tokenizer.eos_token, return_tensors="pt")
        # concatenate new user input with chat history (if there is)
        # ---> TODO: set chat_history_ids properly !!!
        chat_history_ids = self.Tokenizer.encode(history, return_tensors="pt")
        bot_input_ids = torch.cat([chat_history_ids, input_ids], dim=-1) 
        # generate the bot response
        chat_history_ids = self.Model.generate(
                bot_input_ids,
                max_length=1000,
                do_sample=True,  # strategy to choose response (do_sample, top_p, top_k, temperature)
                top_p=0.95,
                top_k=0,
                temperature=0.75,
                pad_token_id=self.Tokenizer.eos_token_id
        )
        #print the output
        text = self.Tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        sys.stdout.write("Chatbot: " + text)
        # ---> TODO: deal with chat history 