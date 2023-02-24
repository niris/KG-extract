import json 

with open("merged_file.json",'r') as f:
    data = json.load(f)
    for i in data:
        labels = list(map(lambda x: x["label"], data[i]['graph']['nodes']))
        ner_tags = list(map(lambda x: x["ner_tag"], data[i]['graph']['nodes']))
        new_obj = {"tokens":labels,"ner_tags":ner_tags}
        with open("ner_dataset.jsonl", "a") as ner_file:
            json.dump(new_obj, ner_file, indent=4)
