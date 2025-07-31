from datasets import load_dataset_builder, GeneratorBasedBuilder, DatasetInfo, SplitGenerator, Split, Value

class StickerQueries(GeneratorBasedBuilder):
    def _info(self):
        return DatasetInfo(
            description="Small Stickers, Big Meanings: A Multilingual Sticker Semantic Understanding Dataset with a Gamified Approach,
            features={
                "sticker_id": Value("string"),
                "labeled_queries": Value("string")
            },
            supervised_keys=None,
            homepage="https://huggingface.co/datasets/metchee/sticker-queries",
        )

    def _split_generators(self, dl_manager):
        data_files = dl_manager.download_and_extract({
            "train": "stickers_queries_en_released.csv"
        })
        return [SplitGenerator(name=Split.TRAIN, gen_kwargs={"filepath": data_files["train"]})]

    def _generate_examples(self, filepath):
        import csv
        with open(filepath, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for idx, row in enumerate(reader):
                yield idx, {
                    "sticker_id": row["sticker_id"],
                    "labeled_queries": row["labeled_queries"]
                }
