import pickle
import pandas as pd
from sklearn_pandas import DataFrameMapper
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from utils import DateEncoder

df = pd.read_csv('data/weather_power.csv', parse_dates=[0])

target = 'energy_demand'
y = df[target]
X = df[['date', 'temperature']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=False)

mapper = DataFrameMapper([
    ('date', DateEncoder(), {'input_df': True}),
    (['temperature'], [SimpleImputer(), PolynomialFeatures(degree=2, include_bias=False)])
], df_out=True)

model = GradientBoostingRegressor()
pipe = make_pipeline(mapper, model)
pipe.fit(X_train, y_train)

with open('static/pipe.pkl', 'wb') as f:
    pickle.dump(pipe, f)
