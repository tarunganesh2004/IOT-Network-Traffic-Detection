import numpy as np
import pandas as pd
import networkx as nx
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Load dataset
df = pd.read_csv("your_dataset.csv")  # Replace with your actual dataset path

# Extract features and labels
features = df.iloc[:, :-1].values  # First 34 columns
labels = df.iloc[:, -1].values  # Label column

# Encode labels
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)

# Normalize features
scaler = StandardScaler()
features = scaler.fit_transform(features)

# Split into train-test sets
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)


# Create adjacency matrix using cosine similarity
def create_adjacency_matrix(X, threshold=0.7):
    similarity_matrix = cosine_similarity(X)
    adj_matrix = (similarity_matrix > threshold).astype(
        int
    )  # Threshold-based adjacency
    return adj_matrix


# Construct graph using NetworkX
def construct_graph(X):
    adj_matrix = create_adjacency_matrix(X)
    G = nx.from_numpy_matrix(adj_matrix)  # Convert to NetworkX graph
    return G, adj_matrix


# Create graph for training data
G_train, adj_matrix_train = construct_graph(X_train)


# Convert adjacency matrix into a graph-based feature representation
def extract_graph_features(X, adj_matrix):
    """
    Transform features using graph neighborhood averaging.
    Each node's new feature is the mean of its neighbors' features.
    """
    new_features = np.zeros_like(X)
    for i in range(len(X)):
        neighbors = np.where(adj_matrix[i] == 1)[0]  # Get indices of connected nodes
        if len(neighbors) > 0:
            new_features[i] = np.mean(
                X[neighbors], axis=0
            )  # Mean of neighbors' features
        else:
            new_features[i] = X[i]  # If no neighbors, keep original features
    return new_features


# Apply graph transformation
X_train_graph = extract_graph_features(X_train, adj_matrix_train)
X_test_graph = extract_graph_features(X_test, create_adjacency_matrix(X_test))

# Reshape data for LSTM (samples, timesteps, features)
X_train_lstm = X_train_graph.reshape(X_train_graph.shape[0], 1, X_train_graph.shape[1])
X_test_lstm = X_test_graph.reshape(X_test_graph.shape[0], 1, X_test_graph.shape[1])

# Define LSTM model
model = Sequential(
    [
        LSTM(64, return_sequences=True, input_shape=(1, X_train_lstm.shape[2])),
        Dropout(0.3),
        LSTM(32, return_sequences=False),
        Dropout(0.3),
        Dense(16, activation="relu"),
        Dense(
            len(np.unique(y_train)), activation="softmax"
        ),  # Multi-class classification
    ]
)

# Compile model
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Train model
model.fit(
    X_train_lstm,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test_lstm, y_test),
)

# Evaluate model
test_loss, test_acc = model.evaluate(X_test_lstm, y_test)
print(f"Test Accuracy: {test_acc:.4f}")
