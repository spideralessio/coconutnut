import json

d = json.load(open("data/coco/annotations/image_info_test2017.json"))
print(d.keys())
print(d["images"])
#print(d["categories"])
#wanted_cats = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train"]

#new_dataset = {"info":d["info"], "licenses":d["licenses"],"annotations":[],"categories":d["categories"]}

cats = {}
c = []
for cat in d["categories"]:
	cats[cat["id"]] = cat["name"]
	c.append(cat["name"])
#print(c)

#print(cats)
img_idx = {}
for im in d["images"]:
	img_idx[im["id"]] = im

'''
wanted_images = set()

for ann in d["annotations"]:
	i = ann["category_id"]
	name = cats[i]
	if name in wanted_cats:
		new_dataset["annotations"].append(ann)
		wanted_images.add(ann["image_id"])

new_dataset["images"] = [img_idx[i] for i in wanted_images]


print(len(new_dataset["images"]))'''