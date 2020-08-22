import pandas as pd
from sklearn.base import TransformerMixin

class DateEncoder(TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return pd.concat([X.dt.month, X.dt.weekday, X.dt.hour], axis=1)
