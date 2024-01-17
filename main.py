from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Load your dataset and preprocess it
df = pd.read_csv('dataset9000.csv')

for column in df.columns:
    if df[column].dtype == 'object':
        label_encoder = LabelEncoder()
        df[column + '_encoded'] = label_encoder.fit_transform(df[column])

df.drop(['Database Fundamentals', 'Computer Architecture',
         'Distributed Computing Systems', 'Cyber Security', 'Networking',
         'Software Development', 'Programming Skills', 'Project Management',
         'Computer Forensics Fundamentals', 'Technical Communication', 'AI ML',
         'Software Engineering', 'Business Analysis', 'Communication skills',
         'Data Science', 'Troubleshooting skills', 'Graphics Designing',
         'Role_encoded'], axis=1, inplace=True)

X = df.drop('Role', axis=1)
y = df['Role']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_scaled, y)

# ... Your existing routes ...

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/ml", methods=["GET", "POST"])
def ml():
    if request.method == "POST":
        # Retrieve form data
        user_input = {
    "Database Fundamentals": int(request.form.get("fName")),
    "Computer Architecture": int(request.form.get("lName")),
    "Distributed Computing Systems": int(request.form.get("computingSystems")),
    "Cyber Security": int(request.form.get("cyberSecurity")),
    "Network Encoding": int(request.form.get("networkEncoding")),
    "Software Development": int(request.form.get("softwareDevelopment")),
    "Programming Skillz": int(request.form.get("progammingSkills")),
    "Project Management": int(request.form.get("projectManagement")),
    "Computer Forensics": int(request.form.get("computerForensics")),
    "Fundamentals": int(request.form.get("fundamentals")),
    "Technical Communication": int(request.form.get("technicalCommunication")),
    "AI ML": int(request.form.get("aiml")),
    "Software Engineering": int(request.form.get("softwareEngineering")),
    "Buisness Analyisis": int(request.form.get("buisnessanalysis")),
    "Communication Skills": int(request.form.get("communicationskills")),
    "Data Science": int(request.form.get("dataScience")),
    "Troubleshooting skills": int(request.form.get("Troubleshooting")),
    "Graphics Designing": int(request.form.get("graphicsdesign"))
}


        # Transform user input
        user_df = pd.DataFrame([user_input])
        user_input_scaled = scaler.transform(user_df)

        # Make predictions
        user_predictions_proba = knn_model.predict_proba(user_input_scaled)
        top_3_classes = user_predictions_proba.argsort()[0, -3:][::-1]

        # Decode the predicted classes
        predicted_roles = label_encoder.inverse_transform(top_3_classes)

        return render_template("ml.html", predicted_roles=predicted_roles)

    return render_template("ml.html")

if __name__ == "__main__":
    app.run(debug=True)
