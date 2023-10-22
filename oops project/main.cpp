#include<iostream.h>
#include<conio.h>
#include<stdio.h>

class Bank
{
    private:
        int acno;
        char name[50];
        int deposit;
        char type;
    public:
        void create_account(); //function to get data from user
        void show_account() const; //function to show data on screen
        void modify(); //function to add new data
        void dep(int); //function to accept amount and add to balance amount
        void draw(int); //function to accept amount and subtract from balance amount
        void report() const; //function to show data in tabular format
        int retacno() const; //function to return account number
        int retdeposit() const; //function to return balance amount
        char rettype() const; //function to return type of account
};

void Bank::create_account()
{
    cout<<"\nEnter the account number: ";
    cin>>acno;
    cout<<"\nEnter the name of the account holder: ";
    gets(name);
    cout<<"\nEnter the type of account (C/S): ";
    cin>>type;
    type=toupper(type);
    cout<<"\nEnter the initial deposit amount: ";
    cin>>deposit;
    cout<<"\nAccount created...";
}

void Bank::show_account() const
{
    cout<<"\nAccount number: "<<acno;
    cout<<"\nAccount holder name: ";
    puts(name);
    cout<<"\nType of account: "<<type;
    cout<<"\nBalance amount: "<<deposit;
}

void Bank::modify()
{
    cout<<"\nAccount number: "<<acno;
    cout<<"\nModify account holder name: ";
    gets(name);
    cout<<"\nModify type of account: ";
    cin>>type;
    type=toupper(type);
    cout<<"\nModify balance amount: ";
    cin>>deposit;
}

void Bank::dep(int x)
{
    deposit+=x;
}

void Bank::draw(int x)
{
    deposit-=x;
}

void Bank::report() const
{
    cout<<acno<<setw(10)<<" "<<name<<setw(10)<<" "<<type<<setw(6)<<deposit<<endl;
}

int Bank::retacno() const
{
    return acno;
}

int Bank::retdeposit() const
{
    return deposit;
}

char Bank::rettype() const
{
    return type;
}

void write_account(); //function to write record in binary file
void display_sp(int); //function to display account details given by user
void modify_account(int); //function to modify record of file
void delete_account(int); //function to delete record of file
void display_all(); //function to display all account details
void deposit_withdraw(int, int); //function to deposit/withdraw amount for given account

void write_account()
{
    Bank ac;
    ofstream outFile;
    outFile.open("account.dat",ios::binary|ios::app);
    ac.create_account();
    outFile.write(reinterpret_cast<char *> (&ac), sizeof(Bank));
    outFile.close();
}

void display_sp(int n)
{
    Bank ac;
    bool flag=false;
    ifstream inFile;
    inFile.open("account.dat",ios::binary);
    if(!inFile)
    {
        cout<<"File could not be opened !! Press any Key...";
        return;
    }
    cout<<"\nBALANCE DETAILS\n";

    while(inFile.read(reinterpret_cast<char *> (&ac), sizeof(Bank)))
    {
        if(ac.retacno()==n)
        {
            ac.show_account();
            flag=true;
        }
    }
    inFile.close();
    if(flag==false)
        cout<<"\n\nAccount number does not exist";
}

void modify_account(int n)
{
    bool found=false;
    Bank ac;
    fstream File;
    File.open("account.dat",ios::binary|ios::in|ios::out);
    if(!File)
    {
        cout<<"File could not be opened !! Press any Key...";
        return;
    }
    while(!File.eof() && found==false)
    {
        File.read(reinterpret_cast<char *> (&ac), sizeof(Bank));
        if(ac.retacno()==n)
        {
            ac.show_account();
            cout<<"\n\nEnter the new details of account"<<endl;
            ac.modify();
            int pos=(-1)*static_cast<int>(sizeof(Bank));
            File.seekp(pos,ios::cur);
            File.write(reinterpret_cast<char *> (&ac), sizeof(Bank));
            cout<<"\n\n\t Record Updated";
            found=true;
          }
    }
    File.close();
    if(found==false)
        cout<<"\n\n Record Not Found ";
}

void delete_account(int n)
{
    Bank ac;
    ifstream inFile;
    ofstream outFile;
    inFile.open("account.dat",ios::binary);
    if(!inFile)
    {
        cout<<"File could not be opened !! Press any Key...";
        return;
    }
    outFile.open("temp.dat",ios::binary);
    inFile.seekg(0,ios::beg);
    while(inFile.read(reinterpret_cast<char *> (&ac), sizeof(Bank)))
    {
        if(ac.retacno()!=n)
        {
            outFile.write(reinterpret_cast<char *> (&ac), sizeof(Bank));
        }
    }
    inFile.close();
    outFile.close();
    remove("account.dat");
    rename("temp.dat","account.dat");
    cout<<"\n\n\tRecord Deleted ..";
}

void display_all()
{
    Bank ac;
    ifstream inFile;
    inFile.open("account.dat",ios::binary);
    if(!inFile)
    {
        cout<<"File could not be opened !! Press any Key...";
        return;
    }
    cout<<"\n\n\t\tACCOUNT HOLDER LIST\n\n";
    cout<<"====================================================\n";
    cout<<"A/c no.      NAME           Type  Balance\n";
    cout<<"====================================================\n";
    while(inFile.read(reinterpret_cast<char *> (&ac), sizeof(Bank)))
    {
        ac.report();
    }
    inFile.close();
}

void deposit_withdraw(int n, int option)
{
    int amt;
    bool found=false;
    Bank ac;
    fstream File;
    File.open("account.dat", ios::binary|ios::in|ios::out);
    if(!File)
    {
        cout<<"File could not be opened !! Press any Key...";
        return;
    }
    while(!File.eof() && found==false)
    {
        File.read(reinterpret_cast<char *> (&ac), sizeof(Bank));
        if(ac.retacno()==n)
        {
            ac.show_account();
            if(option==1)
            {
                cout<<"\n\n\tTO DEPOSIT AMOUNT ";
                cout<<"\n\nEnter the amount to be deposited: ";
                cin>>amt;
                ac.dep(amt);
            }
            if(option==2)
            {
                cout<<"\n\n\tTO WITHDRAW AMOUNT ";
                cout<<"\n\nEnter the amount to be withdraw: ";
                cin>>amt;
                int bal=ac.retdeposit()-amt;
                if((bal<500 && ac.rettype()=='S') || (bal<1000 && ac.rettype()=='C'))
                    cout<<"Insufficient balance";
                else
                    ac.draw(amt);
            }
            int pos=(-1)*static_cast<int>(sizeof(ac));
            File.seekp(pos,ios::cur);
            File.write(reinterpret_cast<char *> (&ac), sizeof(Bank));
            cout<<"\n\n\t Record Updated";
            found=true;
        }
    }
    File.close();
    if(found==false)
        cout<<"\n\n Record Not Found ";
}

int main()
{
    char ch;
    int num;
    do
    {
        clrscr();
        cout<<"\n\n\n\tMAIN MENU";
        cout<<"\n\n\t01. NEW ACCOUNT";
        cout<<"\n\n\t02. DEPOSIT AMOUNT";
        cout<<"\n\n\t03. WITHDRAW AMOUNT";
        cout<<"\n\n\t04. BALANCE ENQUIRY";
        cout<<"\n\n\t05. ALL ACCOUNT HOLDER LIST";
        cout<<"\n\n\t06. CLOSE AN ACCOUNT";
        cout<<"\n\n\t07. MODIFY AN ACCOUNT";
        cout<<"\n\n\t08. EXIT";
        cout<<"\n\n\tSelect Your Option (1-8) ";
        cin>>ch;
        clrscr();
        switch(ch)
        {
        case '1':
            write_account();
            break;
        case '2':
            cout<<"\n\n\tEnter The account No. : "; cin>>num;
            deposit_withdraw(num, 1);
            break;
        case '3':
            cout<<"\n\n\tEnter The account No. : "; cin>>num;
            deposit_withdraw(num, 2);
            break;
        case '4':
            cout<<"\n\n\tEnter The account No. : "; cin>>num;
            display_sp(num);
            break;
        case '5':
            display_all();
            break;
        case '6':
            cout<<"\n\n\tEnter The account No. : "; cin>>num;
            delete_account(num);
            break;
         case '7':
            cout<<"\n\n\tEnter The account No. : "; cin>>num;
            modify_account(num);
            break;
         case '8':
            cout<<"\n\n\tThanks for using bank management system";
            break;
         default :cout<<"\a";
        }
        getch();
    }while(ch!='8');
    return 0;
}