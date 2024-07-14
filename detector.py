import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import requests
from io import BytesIO

class Detector:
    def __init__(self, model_name="TahaDouaji/detr-doc-table-detection"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name).to(self.device)

    def predict(self, image_path):
        try:
            image = Image.open(image_path)
        except Exception as e:
            raise ValueError(f"Could not open image: {e}")

        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        outputs = self.model(**inputs)

        target_sizes = torch.tensor([image.size[::-1]])
        results = self.processor.post_process_object_detection(outputs, target_sizes=target_sizes)[0]

        tables = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            if score > 0.5:  # confidence threshold
                box = [round(i, 2) for i in box.tolist()]
                tables.append({
                    "score": round(score.item(), 2),
                    "label": label.item(),
                    "box": box
                })

        if not tables:
            raise ValueError("No tables detected.")

        return tables
