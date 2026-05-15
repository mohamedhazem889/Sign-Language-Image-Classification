# Sign Language Recognition – Kaggle Competition

This repository contains code and resources for participating in the [Sign Language Kaggle Competition](https://www.kaggle.com/competitions/sign-language-kaggle-comp). The goal is to develop models that can accurately recognize sign language gestures from the provided dataset.

> **Achievement:**  
> I am currently ranked **second** on the competition leaderboard for this challenge.

## Competition Overview

The challenge is to create a machine learning solution that can classify images of sign language gestures. This task is critical for improving accessibility tools for the deaf and hard-of-hearing communities.

**Competition link:** [Sign Language Kaggle Competition](https://www.kaggle.com/competitions/sign-language-kaggle-comp)

## Dataset

The dataset for this competition can be found on the [competition page's Data section](https://www.kaggle.com/competitions/sign-language-kaggle-comp/data). It includes labeled images of various sign language gestures which should be used to train and evaluate your models.

**Key Details:**
- Images represent different alphabetic or symbolic hand gestures.
- Training and test sets are provided.
- Labels correspond to the specific sign represented in each image.

*Note:* You may need to accept the competition rules and login on Kaggle to access the dataset files.

## Notebook Summary

The main notebook in this repository outlines the entire solution pipeline for the competition. The process includes:

- **Exploratory Data Analysis (EDA):** Insightful plots and statistics to better understand feature distributions and class balance.
- **Data Preprocessing & Augmentation:** Image normalization, resizing, and data augmentation strategies to improve model generalization.
- **Model Building:** Design and implementation of deep learning architectures tailored for image classification, with experimentation on different models and hyperparameters.
- **Training & Evaluation:** Training the model on the competition dataset, monitoring metrics such as accuracy and loss, and evaluating the model's performance on validation data.
- **Submission Preparation:** Generating and formatting predictions as required for Kaggle competition submission.

The methodology in this notebook enabled me to achieve the second-place ranking on the competition leaderboard.

## Deploying the Model with FastAPI and ngrok

The trained model can be deployed as an API using [FastAPI](https://fastapi.tiangolo.com/) to serve predictions in real time. To make the API accessible from outside your local environment (such as for testing or demonstration purposes), [ngrok](https://ngrok.com/) can be used to tunnel your local FastAPI server to a public URL.

### Deployment Steps

1. **Export the trained model:**  
   After training, save your best-performing model (e.g., `model.pth` for PyTorch or `model.h5` for Keras).

2. **FastAPI Application:**  
   Use FastAPI to create an API endpoint (e.g., `/predict`) that loads the trained model and accepts image input for prediction.

3. **Run the FastAPI server locally:**  
   ```bash
   uvicorn api:app --reload
   ```
   (Assuming `api.py` contains your FastAPI app.)

4. **Expose the API with ngrok:**  
   Start ngrok to tunnel traffic to your local FastAPI server, which typically runs on port 8000:
   ```bash
   ngrok http 8000
   ```
   ngrok will provide a public URL which can be shared for prediction requests.

## Repository Structure

- `notebooks/` – Jupyter notebooks for data exploration, training, and evaluation.
- `src/` – Source code for data processing, model building, and utilities.
- `models/` – Saved model files and checkpoints.
- `api.py` – FastAPI application for model inference.
- `README.md` – This file.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```

2. **Download the dataset:**
   - Visit the [Kaggle competition Data page](https://www.kaggle.com/competitions/sign-language-kaggle-comp/data).
   - Download the files and place them in a suitable directory within this repo (e.g., `data/`).

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run notebooks or scripts:**
    - Explore or train your models using the provided notebooks and scripts.

5. **Deploy the API:**
    - Follow the deployment steps above to serve your model.

## Contributing

Contributions are welcome! Please submit pull requests or open issues if you have suggestions or find bugs.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

**Good luck in the competition!**
