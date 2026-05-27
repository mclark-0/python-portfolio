#maya
scores = [
88, 42, 95, 70, 63, 82, 55, 91, 74, 85,
38, 77, 90, 61, 89, 72, 59, 98, 45, 81,
67, 73, 88, 52, 94, 79, 100, 68, 83, 71
]
#challenge 2.1
print("the min score is ", min(scores), " and the max score is ", max(scores))
#challenge 2.2
print("the average test score is ", ((sum(scores))/len(scores)))
#challenge 2.3
scores.sort()
print("sorted list and lowest three scores:")
print(f"sorted list: {scores}")
# Accessing the first three elements of the sorted list
print(f"lowest three scores: {scores[:3]}")
#challenge 2.4
extra_credit_scores = []
for score in scores:
    extra_credit_scores.append(score + 5)
print("scores with extra credit:")
print(f"original (sorted) scores:    {scores}")
print(f"scores with 5 extra points: {extra_credit_scores}")
