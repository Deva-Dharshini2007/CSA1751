import math
from collections import Counter
import pprint

# Sample dataset
dataset = [
    ['Sunny', 'Hot', 'High', 'False', 'No'],
    ['Sunny', 'Hot', 'High', 'True', 'No'],
    ['Overcast', 'Hot', 'High', 'False', 'Yes'],
    ['Rain', 'Mild', 'High', 'False', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'False', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'True', 'No'],
    ['Overcast', 'Cool', 'Normal', 'True', 'Yes'],
    ['Sunny', 'Mild', 'High', 'False', 'No'],
    ['Sunny', 'Cool', 'Normal', 'False', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'False', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'True', 'Yes'],
    ['Overcast', 'Mild', 'High', 'True', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'False', 'Yes'],
    ['Rain', 'Mild', 'High', 'True', 'No']
]

features = ['Outlook', 'Temperature', 'Humidity', 'Windy']

# Entropy function
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

# Split dataset by feature value
def split_data(data, feature_index, value):
    return [row for row in data if row[feature_index] == value]

# Choose best feature to split
def best_feature_to_split(data):
    base_entropy = entropy(data)
    best_gain = 0
    best_feature = -1
    num_features = len(data[0]) - 1

    for i in range(num_features):
        feature_values = set([row[i] for row in data])
        new_entropy = 0
        for value in feature_values:
            subset = split_data(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_gain:
            best_gain = info_gain
            best_feature = i
    return best_feature

# Majority vote
def majority_vote(labels):
    return Counter(labels).most_common(1)[0][0]

# Build tree recursively
def build_tree(data, features):
    labels = [row[-1] for row in data]

    # If all labels are same, return label
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # If no features left, return majority
    if len(features) == 0:
        return majority_vote(labels)

    # Choose best feature
    best_feat = best_feature_to_split(data)
    best_feat_name = features[best_feat]
    tree = {best_feat_name: {}}

    feature_values = set([row[best_feat] for row in data])
    for value in feature_values:
        subset = split_data(data, best_feat, value)
        if not subset:
            tree[best_feat_name][value] = majority_vote(labels)
        else:
            # Remove the used feature from features
            new_features = features[:best_feat] + features[best_feat+1:]
            # Remove the used feature column from subset
            new_subset = [row[:best_feat] + row[best_feat+1:] for row in subset]
            tree[best_feat_name][value] = build_tree(new_subset, new_features)
    return tree

# Build and display the tree
decision_tree = build_tree(dataset, features)
pprint.pprint(decision_tree)
