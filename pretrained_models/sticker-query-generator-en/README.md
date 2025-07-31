---
library_name: peft
license: other
base_model: llava-hf/llava-1.5-7b-hf
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: train_k_folds_4_4_epochs
  results: []
---

Sticker Query Generator (English)
The **Sticker Query Generator** is a vision-language model that generates culturally and emotionally resonant search queries given a sticker image. These queries are typically used in chat apps to retrieve and recommend stickers during conversations.
For Chinese, see [here](https://huggingface.co/metchee/sticker-query-generator-zh).

## 🧠 What It Does

Given a sticker image (e.g., a cartoon character shrugging, laughing, or making a gesture), the model outputs **search queries** that people might use to find or express the intent behind that sticker—such as:
- "whatever"
- "ugh not again"
- "mood"
- "shrug"

It captures subtle **social**, **emotional**, and **contextual** cues—something that traditional vision-language models often fail to represent due to lack of cultural grounding.

## 🔍 Use Cases

- Improving sticker search and retrieval in chat apps
- Enhancing semantic understanding in multimodal recommendation systems
- Cultural and emotional alignment in vision-language modeling
- Dataset pre-labeling or enrichment

## 🗂 Dataset

This model was trained on [StickerQueries](https://huggingface.co/datasets/metchee/sticker-queries), a multilingual dataset of over **60 hours** of human-annotated sticker-query pairs in **English** and **Chinese**. Each annotation was reviewed by at least **two people** to ensure quality and consistency.

## 🚀 Inference

```python
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import requests

# Load model
processor = AutoProcessor.from_pretrained("metchee/sticker-query-generator-en")
model = AutoModelForVision2Seq.from_pretrained("metchee/sticker-query-generator-en")

# Run inference
image = Image.open("sticker.png")
inputs = processor(images=image, return_tensors="pt")
output = model.generate(**inputs)
query = processor.decode(output[0], skip_special_tokens=True)
print(query)
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- total_eval_batch_size: 16
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 4.0

### Framework versions

- PEFT 0.15.2
- Transformers 4.52.1
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1

## Citations 
```
@misc{huggingface-sticker-queries,
  author = {Heng Er Metilda Chee, et al.},
  title = {Small Stickers, Big Meanings: A Multilingual Sticker Semantic Understanding Dataset with a Gamified Approach},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/metchee/sticker-queries}},
}
```