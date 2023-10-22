#include <iostream>
#include <vector>

using namespace std;

// Account class to store account details
class Account {
private:
    long accountNumber;
    float balance;
public:
    Account(int accountNumber, float balance) {
        this->accountNumber = accountNumber;
        this->balance = balance;
    }
    int getAccountNumber() {
        return accountNumber;
    }
    float getBalance() {
        return balance;
    }
    void deposit(float amount) {
        balance += amount;
    }
    void withdraw(float amount) {
        balance -= amount;
    }
};

// Customer class to store customer details
class Customer {
private:
    string name;
    vector<Account> accounts;
public:
    Customer(string name) {
        this->name = name;
    }
    string getName() {
        return name;
    }
    vector<Account>& getAccounts() {
        return accounts;
    }
    void addAccount(Account account) {
        accounts.push_back(account);
    }
};

// Transaction class to perform banking transactions
class Transaction {
public:
    static void createAccount(Customer& customer, int accountNumber, float balance) {
        Account account(accountNumber, balance);
        customer.addAccount(account);
        cout << "Account created successfully." << endl;
    }
    static void deposit(Customer& customer, int accountNumber, float amount) {
        vector<Account>& accounts = customer.getAccounts();
        for (int i = 0; i < accounts.size(); i++) {
            if (accounts[i].getAccountNumber() == accountNumber) {
                accounts[i].deposit(amount);
                cout << "Amount deposited successfully." << endl;
                return;
            }
        }
        cout << "Account not found." << endl;
    }
    static void withdraw(Customer& customer, int accountNumber, float amount) {
        vector<Account>& accounts = customer.getAccounts();
        for (int i = 0; i < accounts.size(); i++) {
            if (accounts[i].getAccountNumber() == accountNumber) {
                if (accounts[i].getBalance() >= amount) {
                    accounts[i].withdraw(amount);
                    cout << "Amount withdrawn successfully." << endl;
                } else {
                    cout << "Insufficient balance." << endl;
                }
                return;
            }
        }
        cout << "Account not found." << endl;
    }
    static void balanceEnquiry(Customer& customer, int accountNumber) {
        vector<Account>& accounts = customer.getAccounts();
        for (int i = 0; i < accounts.size(); i++) {
            if (accounts[i].getAccountNumber() == accountNumber) {
                cout << "Balance: " << accounts[i].getBalance() << endl;
                return;
            }
        }
        cout << "Account not found." << endl;
    }
};

// Main function to test the banking system
int main() {
	string acc_name;
	int choice;
	long accno;
	float bal;
	cout<<"enter account name :-";
	cin>>acc_name;
    Customer customer(acc_name);
while (true){

    cout<<"option menu\n1.create account\n2.deposit\n3.withdraw\n4.balance enquiry\n0.exit\nenter your choice:- ";
    cin>>choice;
	if (choice == 1) {
    // Code to create account
    	cout<<"enter acc no. :-";
    	cin>>accno;
    	cout<<"enter the starting balance:-";
    	cin>>bal;
    	Transaction::createAccount(customer, accno, bal);
} 	else if (choice == 2) {
    // Code to deposit amount
    	cout<<"enter acc no. :-";
    	cin>>accno;
    	cout<<"enter the balance to be deposited:-";
    	cin>>bal;
    	Transaction::deposit(customer, accno, bal);
} 	else if (choice == 3) {
    // Code to withdraw amount
    	cout<<"enter acc no. :-";
    	cin>>accno;
    	cout<<"enter the balance to be withdrawed:-";
    	cin>>bal;
    	Transaction::withdraw(customer, accno, bal);
} 	else if (choice == 4) {
    // Code to check balance
    	cout<<"enter acc no. :-";
    	cin>>accno;
    	Transaction::balanceEnquiry(customer, accno);}
    else if (choice==0){
    	return false;
	}
	else {
    cout << "Invalid choice. Please choose 1, 2, 3, or 4." << endl;
}}
    return 0;
}

