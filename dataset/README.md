---
license: mit
task_categories:
- text-generation
language:
- zh
- en
---

# StickerQueries 🧷🗨️

**StickerQueries** is a multilingual dataset for sticker query generation and retrieval. It features human-annotated query-sticker pairs that capture the expressive, emotional, and cultural semantics embedded in stickers.
So far, the StickerQueries family has been downloaded over 200+ times!

## Dataset Structure

- `stickers_queries_zh_released.csv`: Chinese sticker annotations.
- `stickers_queries_en_released.csv`: English sticker annotations.
- `stickers/`: Sticker images in `.gif`, `.png`, or `.webm` formats.

Each row in the CSV files includes:
- `sticker_id`: The file path to the corresponding sticker image.
- `labeled_queries`: A comma-separated list of sticker queries representing the intended emotion, tone, or expression.

## Annotation Process

- Each annotation was reviewed by at least **two people**.
- In total, **42 English** and **18 Chinese** annotators contributed, with **over 60 hours** spent ensuring high-quality and diverse expressions.

## Looking for a sticker query generator?

- 🈶 **Chinese Model**: [Sticker Query Generator ZH](https://huggingface.co/metchee/sticker-query-generator-zh)  
- 🇬🇧 **English Model**: [Sticker Query Generator EN](https://huggingface.co/metchee/sticker-query-generator-en)

## Large-scale Sticker Dataset

Explore the broader dataset: [U-Sticker](https://huggingface.co/datasets/metchee/u-sticker)

---

## Citation

If you use StickerQueries in your work, please cite us as:

```bibtex
@misc{chee2025smallstickersbigmeanings,
      title={Small Stickers, Big Meanings: A Multilingual Sticker Semantic Understanding Dataset with a Gamified Approach}, 
      author={Heng Er Metilda Chee and Jiayin Wang and Zhiqiang Guo and Weizhi Ma and Min Zhang},
      year={2025},
      eprint={2506.01668},
      archivePrefix={arXiv},
      primaryClass={cs.MM},
      url={https://arxiv.org/abs/2506.01668}, 
}
```