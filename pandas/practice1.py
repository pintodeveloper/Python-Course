import pandas as pd

df = pd.DataFrame({
    "A": 10,
    "B": pd.Timestamp("20260218"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": pd.Categorical(["test","tarin","test","train"]),
    "E": "foo"
})

print(df)