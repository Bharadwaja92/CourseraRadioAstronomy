from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.datasets import load_boston
from sklearn.utils import Bunch

dtr = DecisionTreeRegressor()
dtc = DecisionTreeClassifier()

boston = load_boston()
ks = list(boston.keys())

print(boston[ks[1]][:10])

data = boston.data