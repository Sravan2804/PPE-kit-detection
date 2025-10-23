# PPE Kit Detection

Detecting Personal Protective Equipment (PPE) on workers (helmets, vests, gloves, etc.) using YOLOv8.  
This project is built for safety compliance monitoring in workplaces, especially in industrial or construction settings.

---

## Project Overview

Many workplace accidents are preventable if safety protocols are followed. One critical measure is ensuring that personnel are wearing required **PPE**. This project develops a computer vision system that:

- **Detects** whether a person is wearing PPE items (helmet, vest, gloves, etc.)
- **Flags missing items** (e.g. no helmet, no gloves)
- Can be extended to **real-time inference** (camera / CCTV) or batch image/video processing
- Is built using the **Ultralytics YOLOv8** framework for object detection

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher  
- GPU with CUDA (recommended for training)  
- (~) 8 – 16 GB RAM or more  

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/PPE-kit-detection.git
   cd PPE-kit-detection
2. Set up a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

### Training & Inference

1. Prepare your dataset

- Place your images and labels (in YOLO format) into a dataset folder.
- Update configs/data.yaml to point to your training, validation, and (optional) test splits.
- List your PPE classes (e.g. helmet, vest, glove) in that config.

2. Training (in notebook or via script)

Open ppe_detection.ipynb (in Jupyter or Google Colab), or call your training function in Python, for example:
```
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # start from a YOLOv8-n (nano) pretrained model

model.train(
  data='configs/data.yaml',
  epochs=50,
  imgsz=640,
  batch=16,
  name='ppe_detection_exp'
)

```
This will train and save results (weights, graphs, logs) in runs/ or whichever project folder is specified.


### Results & Sample Detections

Tip: Include in this section some key metrics (e.g. mAP@0.5, precision, recall) and sample detection images or videos.

Metric	Value
mAP@0.5	0.87
Precision	0.90
Recall	0.85

Below is a sample detection result:
<img width="1607" height="938" alt="image" src="https://github.com/user-attachments/assets/08d67369-1135-4e8b-bf6a-44b998f92beb" />


### Future Improvements & Extensions

- Deploy in real-time on edge devices (Raspberry Pi, Jetson Nano)
- Trigger alerts when missing PPE is detected
- Add worker tracking (to monitor individuals over frames)
- Extend to video streams / live camera feeds
- Collect more data under diverse lighting / environments
- Evaluate and compare different backbone models (YOLOv7, YOLOv5, EfficientDet, etc.)

### Contributing

Contributions, suggestions, and bug reports are welcome! Please open an issue or submit a pull request. Some ways you could help:

- Add new PPE classes
- Improve inference speed or efficiency
- Integrate with a web dashboard / alerting system
- Add unit / integration tests
- Increase dataset diversity

### References & Related Projects

Here are some resources and related works for PPE / safety detection:

- PPE detection using YOLOv8 (common approach in industry)
- Dataset of Personal Protective Equipment (PPE) — a public dataset for PPE detection 
- Research on industrial safety and PPE datasets (e.g. SH17 dataset) 

### License & Acknowledgements

This project is licensed under the MIT License — see LICENSE file for details.

Acknowledgements:

- Ultralytics YOLOv8 for object detection tools

- Dataset providers

- Open source community
