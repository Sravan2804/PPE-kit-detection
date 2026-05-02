# PPE Kit Detection

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sravan2804/PPE-kit-detection/blob/main/ppe-det.ipynb)

This project focuses on **detecting Personal Protective Equipment (PPE)** such as helmets, masks, and safety vests using **YOLOv8l**, a state-of-the-art object detection model by Ultralytics.  
It helps ensure workplace safety compliance by automatically identifying whether individuals are properly equipped in industrial environments.

---


## 🚀 Features
- Real-time detection of PPE compliance
- Multi-class object detection (10 PPE-related categories)
- Trained and fine-tuned on custom dataset
- Optimized for inference on both images and video
- Supports Google Colab and local GPU environments

---

## Project Overview

Many workplace accidents are preventable if safety protocols are followed. One critical measure is ensuring that personnel are wearing required **PPE**. This project develops a computer vision system that:

- **Detects** whether a person is wearing PPE items (helmet, vest, gloves, etc.)
- **Flags missing items** (e.g. no helmet, no gloves)
- Can be extended to **real-time inference** (camera / CCTV) or batch image/video processing
- Is built using the **Ultralytics YOLOv8** framework for object detection


---

## Detected Classes
| Label | Description |
|:--|:--|
| Hardhat | Worker wearing a helmet |
| Mask | Worker wearing a face mask |
| NO-Hardhat | Worker without a helmet |
| NO-Mask | Worker without a face mask |
| NO-Safety Vest | Worker without a safety vest |
| Person | Generic human detection |
| Safety Cone | Road/industrial safety cone |
| Safety Vest | Worker wearing a safety vest |
| machinery | Construction or industrial machinery |
| vehicle | Cars, trucks, or site vehicles |

---

## 🗂️ Repository Structure
```
PPE-kit-detection/
│
├── YOLO-weights/           # Trained YOLOv8l model weights
├── results/                # Output images or videos after detection
├── ppe-det.ipynb           # Colab notebook for training and evaluation
├── inference.py            # Script for running detections locally
├── requirements.txt        # Dependencies and library versions
└── README.md               # Project documentation
```

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
```
2. Set up a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
---

### Explore the Training Notebook

You can open the full Colab notebook that includes dataset setup, training, and inference steps here:

<p align="center">
  <a href="https://colab.research.google.com/github/Sravan2804/PPE-kit-detection/blob/main/ppe_det.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
  </a>
</p>

---

### Training & Inference

1. Prepare your dataset

- Place your images and labels (in YOLO format) into a dataset folder.
- Update configs/data.yaml to point to your training, validation, and (optional) test splits.
- List your PPE classes (e.g. helmet, vest, glove) in that config.

2. Training (in notebook or via script)

Open ppe_det.ipynb (in Jupyter or Google Colab), or call your training function in Python, for example:
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

---

### Results & Sample Detections

Tip: Include in this section some key metrics (e.g. mAP@0.5, precision, recall) and sample detection images or videos.

- Metric	    Value
- mAP@0.5	 0.87
- Precision	 0.90
- Recall	    0.85

This is one of the frame from the video ppe2.mp4 before:
<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/1e1a51b1-6827-4a62-b795-55d60ea03b6f" />

Below is a sample detection result:
<img width="1607" height="938" alt="image" src="https://github.com/user-attachments/assets/08d67369-1135-4e8b-bf6a-44b998f92beb" />

---

### Future Improvements & Extensions

- Deploy in real-time on edge devices (Raspberry Pi, Jetson Nano)
- Trigger alerts when missing PPE is detected
- Add worker tracking (to monitor individuals over frames)
- Extend to video streams / live camera feeds
- Collect more data under diverse lighting / environments
- Evaluate and compare different backbone models (YOLOv7, YOLOv5, EfficientDet, etc.)

---

### Contributing

Contributions, suggestions, and bug reports are welcome! Please open an issue or submit a pull request. Some ways you could help:

- Add new PPE classes
- Improve inference speed or efficiency
- Integrate with a web dashboard / alerting system
- Add unit / integration tests
- Increase dataset diversity

---

### References & Related Projects

Here are some resources and related works for PPE / safety detection:

- PPE detection using YOLOv8 (common approach in industry)
- Dataset of Personal Protective Equipment (PPE) — a public dataset for PPE detection 
- Research on industrial safety and PPE datasets (e.g. SH17 dataset) 

---

### License & Acknowledgements

This project is licensed under the MIT License — see LICENSE file for details.

Acknowledgements:

- Ultralytics YOLOv8 for object detection tools

- Dataset providers

- Open source community

### Author
**Rama Sravan Gunda**  
📍 University of Limerick | MEngg in Computer Vision & AI  
📧 ramasravan007@gmail.com  
🌐 [GitHub Profile](https://github.com/Sravan2804)

---

<p align="center">
   “Safety doesn’t happen by accident — it’s detected by design.”
</p> 
