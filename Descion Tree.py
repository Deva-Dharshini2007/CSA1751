import math
from collections import Counter, defaultdict

# ---------- Dataset (from your notebook) ----------
data = [
    ["sunny",     "hot",  "high",   "weak",   "no"],
    ["sunny",     "hot",  "high",   "strong", "no"],
    ["overcast",  "hot",  "high",   "weak",   "yes"],
    ["rain",      "mild", "high",   "weak",   "yes"],
    ["rain",      "cool", "normal", "weak",   "yes"],
    ["rain",      "cool", "normal", "strong", "no"],
    ["overcast",  "cool", "normal", "strong", "yes"],
    ["sunny",     "mild", "high",   "weak",   "no"],
    ["sunny",     "cool", "normal", "weak",   "yes"],
    ["rain",      "mild", "normal", "weak",   "yes"]
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"]


# ---------- Entropy Function ----------
def entropy(rows):
    label_counts = Counter(row[-1] for row in rows)
    total = len(rows)

    return sum(
        -(count/total) * math.log2(count/total)
        for count in label_counts.values()
    )


# ---------- Information Gain ----------
def info_gain(rows, attr_index):
    total_entropy = entropy(rows)

    subsets = defaultdict(list)
    for row in rows:
        subsets[row[attr_index]].append(row)

    weighted_entropy = sum(
        (len(subset)/len(rows)) * entropy(subset)
        for subset in subsets.values()
    )

    return total_entropy - weighted_entropy


# ---------- Compute IG for all attributes ----------
print("\nEntropy of Dataset =", round(entropy(data), 4))

for i in range(len(attributes)-1):
    gain = info_gain(data, i)
    print(f"Information Gain ({attributes[i]}) = {round(gain, 4)}")

import math
from collections import Counter, defaultdict

# -------- Dataset from your notebook --------
# a1 ,  a2 ,  a3 ,  Class

data = [
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["False", "Hot",  "High",   "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["True",  "Cool", "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "High",   "Yes"]
]

attributes = ["a1", "a2", "a3", "Class"]


# -------- Entropy --------
def entropy(rows):
    labels = Counter(row[-1] for row in rows)
    total = len(rows)

    return sum(
        -(c/total) * math.log2(c/total)
        for c in labels.values()
    )


# -------- Information Gain --------
def info_gain(rows, attr_index):
    total_entropy = entropy(rows)

    subsets = defaultdict(list)
    for row in rows:
        subsets[row[attr_index]].append(row)

    weighted_entropy = sum(
        (len(subset)/len(rows)) * entropy(subset)
        for subset in subsets.values()
    )

    return total_entropy - weighted_entropy


# -------- Run calculations --------
print("\nEntropy(S) =", round(entropy(data), 4))

for i in range(len(attributes)-1):
    gain = info_gain(data, i)
    print(f"Information Gain({attributes[i]}) =", round(gain, 4))

import math

# -------- Loan Approval Dataset --------
# Income , CreditScore , Collateral , LoanStatus

data = [
    ["High",   "Good",    "Yes", "Yes"],
    ["High",   "Good",    "No",  "Yes"],
    ["Medium", "Good",    "No",  "Yes"],
    ["Low",    "Good",    "Yes", "Yes"],
    ["Low",    "Average", "No",  "No"],
    ["Medium", "Average", "No",  "No"],
    ["High",   "Poor",    "Yes", "Yes"],
    ["Medium", "Poor",    "Yes", "No"],
    ["Low",    "Poor",    "No",  "No"],
    ["High",   "Average", "Yes", "Yes"]
]

attributes = ["Income", "CreditScore", "Collateral", "LoanStatus"]


# -------- Count Class Values --------
def class_count(rows):
    yes = sum(1 for r in rows if r[-1] == "Yes")
    no  = sum(1 for r in rows if r[-1] == "No")
    return yes, no


# -------- Entropy Function --------
def entropy(rows):
    yes, no = class_count(rows)
    total = yes + no
    if yes == 0 or no == 0:
        return 0

    p1 = yes / total
    p2 = no / total

    return -(p1 * math.log2(p1)) - (p2 * math.log2(p2))


# -------- Split Dataset --------
def split_on_attribute(rows, index):
    subsets = {}
    for row in rows:
        key = row[index]
        subsets.setdefault(key, []).append(row)
    return subsets


# -------- Information Gain --------
def info_gain(rows, index):
    total_entropy = entropy(rows)
    subsets = split_on_attribute(rows, index)

    weighted_entropy = 0

    print(f"\n--- Attribute: {attributes[index]} ---")

    for value, subset in subsets.items():
        e = entropy(subset)
        w = len(subset) / len(rows)
        weighted_entropy += w * e

        yes, no = class_count(subset)

        print(f"{value} -> {len(subset)} samples  "
              f"[Yes={yes}, No={no}]  "
              f"Entropy = {round(e,4)}")

    gain = round(total_entropy - weighted_entropy, 4)
    print("Information Gain =", gain)

    return gain


# -------- MAIN PROGRAM --------
print("\nTotal Dataset Entropy =", round(entropy(data), 4))

gains = []
for i in range(len(attributes)-1):
    gains.append(info_gain(data, i))

best_index = gains.index(max(gains))
print(f"\nAttribute selected as ROOT NODE = {attributes[best_index]}")
