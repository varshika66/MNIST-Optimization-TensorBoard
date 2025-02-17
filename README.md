# MNIST Optimization with TensorBoard

📌 Project Overview
This project implements and compares different optimization techniques (Adam vs. SGD) for training an MNIST digit classification model. The training progress is logged and visualized using TensorBoard to analyze performance trends.

🚀 How to Run the Code
Follow these steps to run the project:

1️⃣ Clone the Repository
git clone https://github.com/varshika66/MNIST-Optimization-TensorBoard.git
cd MNIST-Optimization-TensorBoard
2️⃣ Install Required Dependencies
Ensure you have Python installed, then install the required packages:
pip install -r requirements.txt
3️⃣ Run the Main Script
Start training the MNIST model using different optimizers:
python mnist_train.py
4️⃣ View Training Logs in TensorBoard
Run the following command to open TensorBoard and visualize training progress:
tensorboard --logdir=logs/
Then, open http://localhost:6006/ in your browser.

## 📂 Project Structure

| File Name         | Description |
|-------------------|-------------|
| `mnist_train.py`  | Main script for training the MNIST model |
| `lossfunction_py.py` | Implements and compares different loss functions (MSE, Cross-Entropy) |
| `tensor_py.py`   | Demonstrates tensor manipulations and broadcasting |
| `neural_py.py`   | Implements a neural network for MNIST classification |
| `requirements.txt` | List of required Python packages |
| `README.md`      | Project documentation (this file) |


📊 Results & Analysis
Comparison of Adam vs. SGD Optimization
Loss and Accuracy trends visualized using TensorBoard
Final Test Accuracy:
Adam Optimizer: ~98.5%
SGD Optimizer: ~95.2%
📝 Student Information
Name: [Indukuri Varshika]
University: [University of Central Missouri]
Course: [Neural Network Deep Learning]
Assignment Title: MNIST Optimization with TensorBoard
Submission Date: [2/16/25]
📜 License
This project is created for educational purposes.
