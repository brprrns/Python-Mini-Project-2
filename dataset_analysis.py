import numpy as np
import pandas as pd


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Load and clean the Titanic dataset"""

    df = pd.read_csv(file_path)

    ## Drop unnecessary columns
    df = df.drop(columns = ["PassengerId", "Name", "Ticket", "Cabin"],
                  errors = "ignore")


    ## Fill missing values

    # Numerical columns
    df["Age"].fillna(df["Age"].median())

    # Categorical columns
    df["Embarked"].fillna(df["Embarked"].mode()[0])

    return df



def pandas_analysis(df: pd.DataFrame) -> None:
    """Perform pandas analysis on the Titanic dataset"""

    print("\n---GROUPBY SUMMERY---")

    group_summary = df.groupby("Sex").agg(
        passengers = ("Sex", "count"),
        average_age = ("Age", "mean"),
        average_fare = ("Fare", "mean"),
        survival_rate = ("Survived", "mean")
    )

    print(group_summary)


    print("\n ---TOP 10 FARES---")

    top_10 = df.nlargest(10, "Fare")[["Sex", "Age", "Fare", "Survived"]]

    print(top_10)

    print("\n ---FILTERED SUBSET---")

    filtered = df[
        (df["Age"] > 30)
        & (df["Fare"] > 50)
        & (df["Survived"] == 1)
    ]

    print(filtered.head(10))

    print("\n ---MERGE----")

    passenger_summary = df.groupby("Pclass").agg(
        passenger_count = ("Pclass", "count"),
        average_fare = ("Fare", "mean")
    ).reset_index()

    class_names = pd.DataFrame({
        "Pclass": [1, 2, 3],
        "ClassName" : ["First Class", "Second Class", "Third Class"]
    })

    merged = pd.merge(passenger_summary, class_names, on = "Pclass", how = "left")

    print(merged)




def numpy_analysis(df: pd.DataFrame) -> None:
    """Perform Numpy analysis on the Titanic dataset"""

    ages = df["Age"].to_numpy()
    fares = df["Fare"].to_numpy()

    print("\n ---NUMPY ANALYSIS---")

    print(f"Mean Age: {np.mean(ages):.2f}")
    print(f"Standard Deviation of Age: {np.std(ages):.2f}")
    print(f"25th Percentile of Age: {np.percentile(ages, 25):.2f}")
    print(f"75th Percentile of Age: {np.percentile(ages, 75):.2f}")

    correlation = np.corrcoef(ages, fares)[0, 1]
    print(f"Correlation between Age and Fare: {correlation:.2f}")



def main() -> None:
    """Run dataset Analysis"""

    file_path = "titanic.csv"
    df = load_and_clean_data(file_path)

    print("Dataset Shape:", df.shape)
    print("\n Missing Values:\n", df.isnull().sum())


    pandas_analysis(df)
    numpy_analysis(df)


if __name__ == "__main__":
    main()