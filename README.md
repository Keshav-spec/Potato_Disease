# Potato Disease Detection Project

This project involves building a machine learning model to detect potato plant diseases based on leaf images. The project includes both a frontend and backend, with the goal of providing an easy-to-use interface for farmers and agricultural experts.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Image Upload**: Upload potato leaf images for disease detection.
- **Real-time Prediction**: Get instant results for disease classification.
- **User-friendly Interface**: A responsive web application built with React.
- **Scalable Backend**: API built to handle multiple requests efficiently.

## Technologies Used
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow/Keras for model training and inference
- **Database**: SQLite (optional for user data storage)
- **Deployment**: Docker, GitHub

## Installation
### Prerequisites
- Node.js (version 16.x recommended)
- Python 3.x
- Git

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install dependencies for the frontend:
    ```bash
    cd frontend
    npm install
    ```

3. Install dependencies for the backend:
    ```bash
    cd ../backend
    pip install -r requirements.txt
    ```

4. Start the backend server:
    ```bash
    python app.py
    ```

5. Start the frontend:
    ```bash
    cd ../frontend
    npm start
    ```

6. Open your browser and navigate to:
    ```
    http://localhost:3000
    ```

## Usage
1. Upload an image of a potato leaf using the "Upload" button on the homepage.
2. View the prediction results displayed below the uploaded image.
3. Follow the recommendations provided for disease treatment.

## Model Details
- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: Image of potato leaves
- **Output**: Class label (e.g., healthy, early blight, late blight)
- **Training Dataset**: Publicly available dataset of potato leaf images
- **File Path**: The trained model is located at `../models/1.keras`.

## File Structure
```
root
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── App.js
├── backend
│   ├── static
│   ├── templates
│   └── app.py
├── models
│   └── 1.keras
└── README.md
```




