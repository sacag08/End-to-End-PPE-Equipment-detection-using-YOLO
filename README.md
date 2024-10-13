# Real-time Worker Safety Compliance Detection using YOLOv5

## Project Overview
This project aims to enhance worker safety in industrial environments by implementing a **real-time safety compliance detection system** using the **YOLOv5s** model. The model is trained to detect whether workers are wearing proper safety gear, such as helmets, vests, gloves, and shoes, using image and video data. The project involves building a modular pipeline for data ingestion, model training, and deployment in a scalable cloud environment.

### Key Features
- **Object Detection Model:** Uses YOLOv5s to detect 8 classes of safety gear: `helmet`, `no_helmet`, `vest`, `no_vest`, `gloves`, `no_gloves`, `shoes`, and `no_shoes`.
- **Large Dataset:** The model is trained on a pre-labeled dataset from **Roboflow** containing over 4000 images.
- **Training:** The YOLOv5s model was trained for 150 epochs to optimize performance for safety compliance detection.
- **Real-time Detection:** Provides real-time predictions and alerts for safety compliance breaches by processing images and video feeds.
- **Deployment:** The model is deployed on **AWS EC2** in a Docker container for scalability and efficiency.

---

## Workflow and Pipeline

The overall workflow of the project is modular and consists of the following components:

1. **Data Preparation:**
   - Used a pre-labeled dataset from Roboflow, categorized into 8 safety gear classes.
   - Data augmentation techniques were applied to improve model generalization.

2. **Model Training:**
   - YOLOv5s model was trained on the dataset for 150 epochs.
   - Optimized hyperparameters for detecting small objects in real-time scenarios.

3. **Pipeline Setup:**
   - The pipeline is organized into the following key files:
     - **constants:** Defines key constants such as paths, model configurations, and class labels.
     - **entity:** Defines key entities like datasets, model configurations, and inputs/outputs.
     - **components** Contains modular components for data ingestion, preprocessing, and model evaluation.
     - **pipelines:** Combines all the components into a seamless workflow for real-time image processing.
     - **app.py:** The entry point for running the detection model on new data or video streams.

4. **Deployment:**
   - The trained YOLOv5 model is deployed on an **AWS EC2 instance**.
   - **Docker** was used to containerize the application, ensuring a consistent and scalable environment for deployment.

---
## How to Use

Once deployed, the app can:
- **Predict on Images:** Upload an image via the web interface or API, and the model will return predictions regarding the safety compliance of the workers.
- **Real-time Video Detection:** Feed real-time video streams for ongoing safety compliance detection.

---

## Model Performance
- The YOLOv5s model achieved **X% mAP (mean Average Precision)** on the test dataset.
- The model is optimized for real-time detection with a minimal delay between frame capture and prediction.

---

## Future Enhancements
- Integrating **additional safety gear classes** such as face shields and harnesses.
- **Edge deployment** using IoT devices for on-premise safety monitoring.
- Improving model accuracy using **transfer learning** and additional data augmentation techniques.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or contributions, please contact sachitagarwal98@gmail.com.

