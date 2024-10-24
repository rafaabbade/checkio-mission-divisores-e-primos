"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
    {
        "input": [7],
        "answer": [[1, 7], "Primo"]
    },
    {
        "input": [10],
        "answer": [[1, 2, 5, 10], "Não é Primo"]
    },
    {
        "input": [1],
        "answer": [[1], "Não é Primo"]
    },
    {
        "input": [13],
        "answer": [[1, 13], "Primo"]
    },
    {
        "input": [15],
        "answer": [[1, 3, 5, 15], "Não é Primo"]
    }
]
}
