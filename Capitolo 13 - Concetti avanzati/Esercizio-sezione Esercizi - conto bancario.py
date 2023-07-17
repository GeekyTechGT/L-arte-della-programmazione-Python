import multiprocessing
import time

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = multiprocessing.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Saldo insufficiente.")

    def get_balance(self):
        return self.balance

def process_task(account, process_id):
    for _ in range(5):
        time.sleep(1)
        account.deposit(100)
        account.withdraw(50)
        balance = account.get_balance()
        print(f"Processo {process_id}: saldo attuale: {balance}")

def main():
    # Creazione di un'istanza di BankAccount
    account = BankAccount(initial_balance=1000)

    # Esecuzione di processi
    process1 = multiprocessing.Process(target=process_task, args=(account, 1))
    process2 = multiprocessing.Process(target=process_task, args=(account, 2))
    process1.start()
    process2.start()

    process1.join()
    process2.join()

    # Stampa il saldo finale
    final_balance = account.get_balance()
    print(f"Saldo finale: {final_balance}")

if __name__ == "__main__":
    main()
