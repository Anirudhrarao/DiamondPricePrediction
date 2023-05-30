
# Diamond Price Prediction
There are 10 independent variables (including `id`):
**The dataset** The goal is to predict `price` of given diamond (Regression Analysis).
* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

Dataset Source Link :
[https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)


# Simple linear Regression
Simple Linear Regression is a type of Regression algorithms that models the relationship between a dependent variable and a single independent variable. The relationship shown by a Simple Linear Regression model is linear or a sloped straight line, hence it is called Simple Linear Regression.

The key point in Simple Linear Regression is that the dependent variable must be a continuous/real value. However, the independent variable can be measured on continuous or categorical values.
### Task Performed:
1. Data Cleaning
2. Exploratory Data Analysis
3. Data Preprocessing and feature engineering
4. Model training
5. Pickelizing model
6. Creating flask app for model


## Tech Stack

**Client:** Flask

**Server:** Python, Machine Learning, Statistics, Oops


## Support

For support, email raorudhra16@gmail.com or contact.


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rao-anirudhra-aa013b240/)


## Run Locally

Clone the project

```bash
  gh repo clone Anirudhrarao/DiamondPricePrediction
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Training model 

```bash
  python src\pipelines\traning_pipeline.py
```

Start the server

```bash
  python app.py
```


## Screenshots of project

![App Screenshot](https://raw.githubusercontent.com/Anirudhrarao/DiamondPricePrediction/main/screenshot/ssc.png)


## Authors

- [@Anirudhrarao](https://github.com/Anirudhrarao)

