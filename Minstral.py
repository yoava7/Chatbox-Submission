from transformers import AutoModelForCausalLM, AutoTokenizer

# Defining what the model is and fetching its tokenizer
# Padding is not necessary as only one prompt is handed to be generated at a time, but is still good practice
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", device_map="auto", load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2", padding_side="left")

help_text = ("Commands: \n\tq: Quit the program\n\tr: Respond to your previous prompt with a proper response to it, "
             "in case the chatbot's response is not satisfactory.\n\tc: Chat; enter a normal prompt for the chatbot to "
             "respond to.\n\th: Display this help text again.\n\nGeneral Instruction:\n\tWrite your prompt after "
             "providing the chat command, for example: \"c Is water wet?\".\n\tIf you encounter a response that you "
             "believe is either factually false or could be improved upon, provide an example of a valid response to "
             "your prompt after providing the response command, for example: \"r The novel 1984 was written by George "
             "Orwell.\"\n")
user_prompt: str = "placeholder text"
chat_log = []


print(help_text)

# MAIN LOOP

# Checks that user did not quit the program
while user_prompt[0].lower() != "q":
    user_prompt = input("\nEnter your prompt, after q/r/c/h: ")

    # Sequence for the "chat" command
    if user_prompt[0].lower() == "c" and user_prompt[1] == " ":
        # Adding the user's current prompt to the chat log, and formatting the log to be used with Mistral
        chat_log.append({"role": "user", "content": user_prompt[2:]})
        formatted_chat_log = tokenizer.apply_chat_template(chat_log, tokenize=False)
        # Applies the model's tokenizer to the user prompt, and assigns it to the GPU
        model_inputs = tokenizer([formatted_chat_log], return_tensors="pt").to("cuda")

        # Calls on the model to generate the response, and saves the first token as a string
        # NOTE: The string is split and sliced to only contain the most recent response from the model, this
        # should be changed to a different pattern if a different model is to be used.
        generated_ids = model.generate(**model_inputs, max_new_tokens=5000, pad_token_id=tokenizer.eos_token_id)
        current_response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].split("[/INST] ")[-1]
        print(current_response)
        chat_log.append({"role": "assistant", "content": current_response})
    # Sequence for the "respond" command
    elif user_prompt[0].lower() == "r" and user_prompt[1] == " ":
        user_feedback = input("Please enter an appropriate response: ")

        # Fixing the live chatbot's conversation memory with the given valid response
        chat_log.pop()
        chat_log.append({"role": "assistant", "content": user_feedback})

        # UNFINISHED SECTION

    # Sequence for the "help" command
    elif user_prompt[0].lower() == "h":
        print(help_text)
    # In case the user did not type a valid command
    else:
        print("Please enter a valid command.")

# TODO: Add ask for training with data now or not
