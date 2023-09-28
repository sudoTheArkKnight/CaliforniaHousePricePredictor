# California Housing Prices Prediction

## Project Overview
This project focuses on predicting housing prices in California districts using machine learning. The goal is to build a regression model that can estimate the median house value based on various features. The dataset used for this project is the [California Housing Prices dataset](https://www.kaggle.com/camnugent/california-housing-prices) from Kaggle.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Exploration](#data-exploration)
6. [Data Preprocessing](#data-preprocessing)
7. [Model Building](#model-building)
8. [Model Evaluation](#model-evaluation)
9. [Results](#results)
10. [Contributing](#contributing)
11. [License](#license)

## Dataset
- **Dataset Source:** [California Housing Prices](https://www.kaggle.com/camnugent/california-housing-prices) on Kaggle
- **Description:** This dataset contains housing-related information for various districts in California. It includes features like population, median income, housing median age, and the target variable, median house value.
### Understating the dataset
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/0c3c127b-e057-467a-ad0d-71270a20ce4d)
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/3145441b-73c1-4fee-9ccb-4d5985d7df3b)
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/01bd003d-f004-46a9-bf71-d6db87c5672c)
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/ceffa6eb-e218-49fb-aa58-6e6d04ccd333)


## Installation
1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory.
3. Install the required Python packages using `pip install -r requirements.txt`.

## Usage
1. Launch Jupyter Notebook: Run `jupyter notebook` in the project directory.
2. Open and run the `Predictor.ipynb` notebook to explore the project.

## Data Exploration
- Explore the dataset using Python and Jupyter Notebook.
- Generate histograms, scatter plots, and correlation matrices to gain insights into the data.
### Here are some graphs to help you gain a better understanding
\n*This is a heat map, showing the corelation each columns has with each other*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/1e797a0b-dd07-430c-b8a9-770f3b0806ed)
\n*This is the histogram (similar to the one shown earlier) showing the data distribution*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/b693279e-753e-4435-b057-81a39fc3c455)
\n*This is a scatter plot, makes it simple to spot outliers in the dataset*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/7c58eb93-7764-42cd-98ba-97649d1c594f)


## Data Preprocessing
- Handle missing data using imputation.
- Perform feature engineering to create new informative features.
- Scale the data to prepare it for modeling.

## Model Building
- Build a Linear Regression model using scikit-learn.
- Train the model on the training dataset.
- Evaluate the model's performance using various metrics.

## Model Evaluation
- Calculate evaluation metrics, including Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
- Visualize model predictions and compare them to actual values.
### here are a few graphs that will help you understand the performance of the model.
\n*Scatter plot*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/05080eff-cbab-4524-a8e7-c233560187fc)
\n*Residual plot*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/838f8a2f-6f5e-4911-8091-3d65bc77a6aa)
\n*Feature importance plot*
![image](https://github.com/The-Ark-Knight/CaliforniaHousePricePredictor/assets/90926369/5f0d2f85-c9f7-49cc-9f9a-3c36d3f6365a)


## Results
- Summarize key findings and insights from the project.
- Discuss the model's performance and any improvements achieved through model refinement.
- The resultant was calculated based on the following parameters
Mean Absolute Error: 0.4367338817223555
Mean Squared Error: 0.3603952607354783
Root Mean Squared Error: 0.6003292935843446
- this values are very average for a model of this type, to achive more suposticated results i will be refining and rewriting parts of the code to ensure maxixmum accuracy

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
