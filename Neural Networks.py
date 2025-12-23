import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample data
X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 1, 1, 0]   # XOR output

# Build Neural Network
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

# Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X, y, epochs=500, verbose=0)

# Test
print(model.predict([[1, 0]]))
