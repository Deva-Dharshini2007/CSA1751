import math

# ---------- Helper functions ----------
def sigmoid(net):
    return 1 / (1 + math.exp(-net))

def d_sigmoid(out):
    return out * (1 - out)

# ---------- Inputs ----------
x1, x2, x3 = 1, 0, 1

# ---------- Weights from inputs → hidden layer ----------
w14 = 0.2   # x1 -> H4
w24 = 0.4   # x2 -> H4
w34 = -0.6  # x3 -> H4

w15 = -0.3  # x1 -> H5
w25 = 0.1   # x2 -> H5
w35 = 0.2   # x3 -> H5

# ---------- Biases for hidden layer ----------
theta4 = -0.4
theta5 = 0.2

# ---------- Weights hidden → output ----------
w46 = -0.3
w56 = -0.2

# ---------- Bias output ----------
theta6 = 0.1

eta = 0.9          # learning rate
target = 1.0       # given actual output


def forward_pass():
    # Hidden neuron H4
    net4 = x1*w14 + x2*w24 + x3*w34 + theta4
    o4 = sigmoid(net4)

    # Hidden neuron H5
    net5 = x1*w15 + x2*w25 + x3*w35 + theta5
    o5 = sigmoid(net5)

    # Output neuron O6
    net6 = o4*w46 + o5*w56 + theta6
    o6 = sigmoid(net6)

    return (o4, o5, o6)


# ---------- FIRST FORWARD PASS ----------
o4, o5, o6 = forward_pass()
print("Output before training =", round(o6, 4))

# ---------- BACK-PROPAGATION ----------
# Output layer error term
delta6 = (target - o6) * d_sigmoid(o6)

# Hidden layer deltas
delta4 = d_sigmoid(o4) * (delta6 * w46)
delta5 = d_sigmoid(o5) * (delta6 * w56)

# ---- Update weights hidden → output ----
w46 += eta * delta6 * o4
w56 += eta * delta6 * o5
theta6 += eta * delta6   # bias update

# ---- Update weights input → hidden ----
w14 += eta * delta4 * x1
w24 += eta * delta4 * x2
w34 += eta * delta4 * x3
theta4 += eta * delta4

w15 += eta * delta5 * x1
w25 += eta * delta5 * x2
w35 += eta * delta5 * x3
theta5 += eta * delta5

# ---------- SECOND FORWARD PASS ----------
o4, o5, o6 = forward_pass()
print("Output after training =", round(o6, 4))

# ---------- Show updated weights ----------
print("\nUpdated Weights:")
print("w14, w24, w34 =", round(w14,4), round(w24,4), round(w34,4))
print("w15, w25, w35 =", round(w15,4), round(w25,4), round(w35,4))
print("w46, w56     =", round(w46,4), round(w56,4))

import math

# ---------- helper functions ----------
def sigmoid(net):
    return 1 / (1 + math.exp(-net))

def d_sigmoid(out):
    # derivative: sigmoid(x) * (1 - sigmoid(x))
    return out * (1 - out)

# ---------- inputs ----------
# Replace these if your sheet has different values.
x1 = 0.3   # example value seen in the scribble
x2 = 0.8   # example value seen in the scribble

# ---------- weights input -> hidden ----------
# Example values inferred from the drawing; adjust if your sheet differs.
# Hidden node H3 (upper hidden node)
w13 = 0.1   # weight from x1 to H3
w23 = 0.8   # weight from x2 to H3

# Hidden node H4 (lower hidden node)
w14 = 0.4   # weight from x1 to H4
w24 = 0.6   # weight from x2 to H4

# ---------- biases for hidden layer ----------
# The scribble doesn’t clearly show numeric bias values; use what your homework gives.
# If none given, you can set them to 0 or whatever the problem specifies.
theta3 = 0.0  # bias for H3
theta4 = 0.0  # bias for H4

# ---------- weights hidden -> output ----------
# Example values seen: one looks like 0.3, another 0.9. Adjust if needed.
w35 = 0.3   # weight from H3 to output Y
w45 = 0.9   # weight from H4 to output Y

# ---------- bias output ----------
theta5 = 0.0  # replace if your sheet shows a specific bias

# learning rate and target
eta = 1.0      # example from your note; change if different
target = 0.5   # example target seen in the note; change if different

# ---------- forward pass ----------
def forward_pass():
    # hidden node H3
    net3 = x1*w13 + x2*w23 + theta3
    o3 = sigmoid(net3)

    # hidden node H4
    net4 = x1*w14 + x2*w24 + theta4
    o4 = sigmoid(net4)

    # output node Y
    net5 = o3*w35 + o4*w45 + theta5
    y = sigmoid(net5)

    return o3, o4, y

# -------- first forward pass --------
o3, o4, y = forward_pass()
print("Output before training =", round(y, 4))

# -------- backpropagation --------
# Output layer error term
delta5 = (target - y) * d_sigmoid(y)

# Hidden layer deltas
delta3 = d_sigmoid(o3) * (delta5 * w35)
delta4 = d_sigmoid(o4) * (delta5 * w45)

# --- update weights hidden -> output ---
w35 += eta * delta5 * o3
w45 += eta * delta5 * o4
theta5 += eta * delta5

# --- update weights input -> hidden ---
w13 += eta * delta3 * x1
w23 += eta * delta3 * x2
theta3 += eta * delta3

w14 += eta * delta4 * x1
w24 += eta * delta4 * x2
theta4 += eta * delta4

# -------- second forward pass --------
o3, o4, y = forward_pass()
print("Output after training =", round(y, 4))

# -------- updated weights summary --------
print("\nUpdated weights and biases:")
print(f"w13, w23 = {w13:.4f}, {w23:.4f}")
print(f"w14, w24 = {w14:.4f}, {w24:.4f}")
print(f"w35, w45 = {w35:.4f}, {w45:.4f}")
print(f"theta3, theta4, theta5 = {theta3:.4f}, {theta4:.4f}, {theta5:.4f}")
