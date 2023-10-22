from transformers import datasets

# Download and load the AmbigQA dataset
dataset = datasets.load_dataset("ambig_qa")

# Accessing different splits of the dataset
train_dataset = dataset["train"]
validation_dataset = dataset["validation"]
test_dataset = dataset["test"]

