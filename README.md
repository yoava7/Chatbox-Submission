***The following project was done as a part of a company's hiring process. It remains operational, though no further progress will likely be made on it.***

***A technical document reflecting on the project- consisting of architecture diagrams, choices made along development, and potential ways to continue the project- is alvailable upon request.***

---

# Chatbox-Submission
Self-Correcting AI Chatbot Development
## Setup Instructions
To run the Minstral.py program, first create a new project in an IDE or create a virtual environment, and install the following:

The Transformers library:
```
pip install transformers datasets
```
PyTorch (with CUDA):
- Note: this command forcefully reinstalls PyTorch fully, this may not be necessary but may help if CUDA is not working properly
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117 --upgrade --force-reinstall
```
---

On the first run, Transformers should automatically install [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2). This model is quite large (7.24B params), if you wish to swap to a different model do so in lines 5 and 6 before running the program. You will also need to change line 39 if using a model with a different chat template (change the split method to however your model separates interactions with Transformer's chat template functionality).

## Execution Instructions 
Once all the dependencies are installed, simply run the file (**do not attempt to import to another file, there is no main guard!**)
You should then use the standard IO to interact with the program. Instructions are printed when you first run the file and can be seen again at any point by inputting "h" into the IO.
