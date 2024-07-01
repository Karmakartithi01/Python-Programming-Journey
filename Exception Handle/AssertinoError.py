x = "You are selected as a Junior Machine Learning Engineer in our company and you will get a competitive salary and perks"
y = "Reject"

your_score = 2000
min_score = 300

try:
    # This will raise an AssertionError if the condition is False
    assert your_score >= min_score
    print(x)
except AssertionError:
    print(y)
