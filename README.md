# Yoga Pose Classification

A machine learning project for classifying **16 different yoga poses** using **MediaPipe Pose landmarks** and a neural network.

## Overview

The project follows:

**Yoga Images → MediaPipe Landmarks → Geometric Features → Neural Network → Pose Classification**

MediaPipe extracts body landmarks from images, while joint angles and distances are used as features for classification.

## Dataset

The dataset contains 16 selected yoga poses, including Boat, Camel, Chair, Child, Cobra, Crow, Downward Dog, Eagle, Fish, Half Moon, and others.

`download_script.py` downloads images from URL lists, organizes them by pose, and uses MD5 hashing to prevent duplicate images.

`move_script.py` filters the dataset by keeping the selected pose classes and moving the remaining folders to `Main_Dataset_extra`.

## Feature Extraction

For every image:

* Detect pose landmarks using MediaPipe.
* Extract relevant body-joint coordinates.
* Calculate joint angles and Euclidean distances.
* Use these geometric features as model input.

## Model

The main model is a fully connected neural network using:

* Dense layers with ReLU activation
* Batch Normalization
* Dropout
* Adam/AdamW optimization
* Softmax output for pose classification

The project includes two model implementations in:

```text
main_model.ipynb
mini_model.ipynb
```

## Evaluation

Models are evaluated using:

* Accuracy
* Validation loss
* Confusion matrix
* Class-wise predictions

## Project Structure

```text
Yoga-Pose-Classification/
├── Main_Dataset/
├── Main_Dataset_extra/
├── download_script.py
├── move_script.py
├── main_model.ipynb
└── mini_model.ipynb
```

## Installation

```bash
pip install numpy opencv-python tensorflow scikit-learn mediapipe matplotlib seaborn requests tqdm
```

## Usage

Download the images:

```bash
python download_script.py
```

Filter the dataset:

```bash
python move_script.py
```

Then open `main_model.ipynb` or `mini_model.ipynb` to extract features, train, and evaluate the model.

## Future Improvements

* Real-time webcam-based pose classification
* Automated pose correction
* Improved feature engineering
* Independent test-set evaluation
