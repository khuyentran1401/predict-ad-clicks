import bentoml
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)
iris = load_iris()
X = iris.data[:, :4]
Y = iris.target
model.fit(X, Y)
print(type(model))

# `save` a given classifier and retrieve coresponding tag:
tag = bentoml.sklearn.save_model("kneighbors", model)

# retrieve metadata with `bentoml.models.get`:
# metadata = bentoml.models.get(tag)

# load the model back:
# loaded = bentoml.sklearn.load_model("kneighbors:latest")

# Run a given model under `Runner` abstraction with `to_runner`
# runner = bentoml.sklearn.get(tag).to_runner()
# runner.init_local()
# runner.run([[1,2,3,4,5]])
