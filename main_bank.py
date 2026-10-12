from bank_account import SavingsAccount, CurrentAccount

def print_histroy(account) -> None:
    """Prints Transaction histroy for an account"""

    print(f"Transaction histroy for {account.holder_name}")
    print("-" * 40)

    for transaction in account.transaction_histroy:
        print(transaction)



def main() -> None:
    """Demonstrate the banking System."""

    savings1 = SavingsAccount(
        "S001",
        "Prasad",
        10000,
        5
    )

    savings2 = SavingsAccount(
        "S002",
        "Rahul",
        15000,
        4
    )
    current1 = CurrentAccount(
        "C001",
        "Anil",
        5000,
        3000
    )


    ## Savings account transactions
    savings1.deposit(2000)
    savings1.withdraw(1000)
    savings1.apply_interest()

    savings2.deposit(3000)
    savings2.withdraw(2000)
    savings2.apply_interest()

    #Current account transactions
    current1.deposit(1000)
    current1.withdraw(7000)


    print("Final Balances")
    print("-" * 30)
    print(f"{savings1.holder_name}: {savings1.get_balance()}")
    print(f"{savings2.holder_name}: {savings2.get_balance()}")
    print(f"{current1.holder_name}: {current1.get_balance()}")

    print_histroy(savings1)
    print_histroy(savings2)
    print_histroy(current1)


    # Demonstrating ValueError
    try:
        savings1.withdraw(100000)
    except ValueError as error:
        print(f"Error: {error}")




if __name__ == "__main__":
    main()