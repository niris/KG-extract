import os
import json


def merge_all_json_files(json_dir_path):
    """
    Merge all JSON files in the input directory into a single JSON file in the output directory
    """
    merged_data = {}
    for file_name in os.listdir(os.path.join("input", json_dir_path)):
        with open(os.path.join("input", json_dir_path, file_name), "r") as f:
            data = json.load(f)
            merged_data.update(data)
    with open(os.path.join("output", json_dir_path + ".json"), "w") as f:
        json.dump(merged_data, f, indent=4)


def convert_to_ner_dataset(input_file_path, output_file_name):
    """
    converts graph data in the input file to a dataset for NER training
    """
    with open(input_file_path, "r") as f:
        data = json.load(f)
        for i in data:
            labels = list(map(lambda x: x["label"], data[i]["graph"]["nodes"]))
            ner_tags = list(map(lambda x: x["ner_tag"], data[i]["graph"]["nodes"]))
            new_obj = {"tokens": labels, "ner_tags": ner_tags}
            with open(f"{output_file_name}.jsonl", "a") as ner_file:
                json.dump(new_obj, ner_file, indent=4)
