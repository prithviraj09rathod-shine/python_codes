import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="Species")
species_names = iris.target_names

# Define models with tuned hyperparameters
models = {
    "KNN (k=6)": KNeighborsClassifier(n_neighbors=6),
    "Decision Tree (depth=4, gini)": DecisionTreeClassifier(max_depth=4, criterion="gini", random_state=1234),
    "Random Forest (estimators=5, depth=6)": RandomForestClassifier(n_estimators=5, max_depth=6, random_state=1234),
    "Gradient Boosting (estimators=100, lr=0.2)": GradientBoostingClassifier(n_estimators=100, learning_rate=0.2, random_state=1234)
}

# Train all models
for name, model in models.items():
    model.fit(X, y)

# --- Accuracy Comparison Table ---
st.subheader("📊 Cross-Validated Accuracy Comparison")
acc_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    acc_results[name] = f"{scores.mean():.3f}"

acc_df = pd.DataFrame.from_dict(acc_results, orient="index", columns=["Accuracy"])
st.table(acc_df)

# --- Interactive Prediction ---
st.subheader("🔮 Interactive Prediction")
model_choice = st.selectbox("Choose a model:", list(models.keys()))
chosen_model = models[model_choice]

# Input sliders for features
sepal_length = st.slider("Sepal length (cm)", float(X["sepal length (cm)"].min()), float(X["sepal length (cm)"].max()), 5.0)
sepal_width  = st.slider("Sepal width (cm)",  float(X["sepal width (cm)"].min()),  float(X["sepal width (cm)"].max()), 3.0)
petal_length = st.slider("Petal length (cm)", float(X["petal length (cm)"].min()), float(X["petal length (cm)"].max()), 1.5)
petal_width  = st.slider("Petal width (cm)",  float(X["petal width (cm)"].min()),  float(X["petal width (cm)"].max()), 0.2)

# Prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = chosen_model.predict(input_data)[0]
pred_species = species_names[prediction]

st.write(f"Using **{model_choice}**, the predicted species is: **{pred_species.capitalize()}**")

# Show probabilities if supported
if hasattr(chosen_model, "predict_proba"):
    probs = chosen_model.predict_proba(input_data)[0]
    prob_df = pd.DataFrame(probs, index=species_names, columns=["Probability"])
    st.bar_chart(prob_df)