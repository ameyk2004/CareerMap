from pymongo import MongoClient
import pandas as pd

# MongoDB connection string
MONGODB_URI = "mongodb+srv://himanshugholse08:wBX31Hgv3SxhAg9E@interview-experience.s8jve.mongodb.net/"
client = MongoClient(MONGODB_URI)

# Access the database and collection
db = client["int-exp"]
collection = db["experience"]  # replace with actual collection name

# Fetch all documents
documents = list(collection.find())

# Convert documents to DataFrame with selected fields
data = []
for doc in documents:
    data.append({
        "uid": doc.get("uid", ""),
        "name": doc.get("name", ""),
        "email": doc.get("email", ""),
        "role": doc.get("role", ""),
        "company": doc.get("company", ""),
        "branch": doc.get("branch", ""),
        "batch": doc.get("batch", ""),
        "exp_text": doc.get("exp_text", ""),
        "profile_pic": doc.get("profile_pic", ""),
        "updated_at": doc.get("updated_at", "")
    })
    

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("interview_experiences.csv", index=False)
print("Data exported to interview_experiences.csv")

