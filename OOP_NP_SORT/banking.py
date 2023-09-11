class Bank:
    def __init__(self, bank_name, bank_code):
        self.name =bank_name
        self.code = bank_code
        self.branch_list = []
        # if branch_list is None:
        #     self.branch_list = []
        # else:
        #     self.branch_list = branch_list

    def addBranch(self, branch):
        if branch not in self.branch_list:
            self.branch_list.append(branch)

    def removeBranch(self, branch_code):
        for branch in self.branch_list:
            if branch.branch_code == branch_code:
                self.branch_list.remove(branch)

    def getBranch(self, branch_code):
        for branch in self.branch_list:
            if branch.branch_code == branch_code:
                return branch
        return None

    def getAllBranches(self):
        print()
        for branch in self.branch_list:
            print("branch code:",branch.branch_code,"   branch city:",branch.city)

    def updateinfo(self,newname,newcode):
        self.name = newname
        self.code = newcode

    def print_bank(self):
        print("bank name: ",self.name,"bank_code: ",self.code)
        for branch in self.branch_list:
            print("branch=>>>",branch.city)


class Branch:
    def __init__(self,branch_code,city,bank):
        self.branch_code = branch_code
        self.city = city
        self.bank = bank
        self.account_list = []
        # if account_list is None:
        #     self.branch_list = []
        # else:
        #     self.account_list = account_list

    def print_branch(self):
        print("bank name:",self.bank.name,"bank code:",b1.code,"branch city:",self.city,"branch code:",self.branch_code)

    def addAccount(self,account_obj):
        if account_obj not in self.account_list:
            self.account_list.append(account_obj)

    def removeAccount(self,account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                self.account_list.remove(account)

    def getAccount(self,account_number):
        for account in self.account_list:
            if account.account_number == account_number:
                return account
        return None
    def updateInfo(self,branch_code,city):
        self.branch_code = branch_code
        self.city = city

class Account:
    def __init__(self, acc_no, branch_obj):
        self.balance = 0.0
        self.account_number = acc_no
        self.branch = branch_obj
    
    def debitAmount(self, amt):
        if self.balance >= amt :
            self.balance = self.balance - amt
    
    def creditAmount(self,amt):
        self.balance = self.balance + amt
        
    def getBalance(self):
        return self.balance
    
class Saving_Account(Account):
    def __init__(self,acc_no,branch,min_balance):
        self.min_balance = min_balance
        self.customer = None
        super().__init__(acc_no,branch)

    def setCustomer(self,customer_obj):
        self.customer = customer_obj

    def removeCustomer(self):
        self.customer = None

    def debitAmount(self, amt):
        if self.balance-amt >= self.min_balance:
            self.balance = self.balance - amt

class Current_Account(Account):
    def __init__(self,acc_no,branch,interest_rate):
        self.customer = None
        self.interest_rate =  interest_rate
        super().__init__(acc_no,branch)

    def setCustomer(self,customer_obj):
        self.customer = customer_obj

    def removeCustomer(self):
        self.customer = None

    def debitAmount(self,amt):
        if self.balance >= amt :
            self.balance = self.balance - amt

class Customer:
    next_id = 1
    def __init__(self,name,address,phone):
        self.saving_acc = None
        self.current_acc = None
        self.id = Customer.next_id
        self.name = name
        self.address = address
        self.phone = phone
        Customer.next_id = Customer.next_id+1
    def setSavingAcc(self,saving_acc):
        self.saving_acc = saving_acc

    def getSavingAcc(self):
        return self.saving_acc

    def setCurrentAcc(self,current_acc):
        self.current_acc = current_acc

    def getCurrentAcc(self):
        return self.current_acc
    
    
        


print("---------------- Task (i) ---------------")
b1 = Bank("DBBL", 1256)
b2 = Bank("EBL", 1257)

print("---------------- Task (ii) ---------------")
br1 = Branch(1,"Dhanmondi", b1)
br2 = Branch(2,"mothijheel", b1)
br3 = Branch(3,"Mirpur", b2)
br4 = Branch(4,"Gulshan", b2)

b1.addBranch(br1)
b1.addBranch(br2)
b2.addBranch(br3)
b2.addBranch(br4)

# print(br1.print_branch())

print("---------------- Task (iii) ---------------")
print(b1.getAllBranches())
print(b2.getAllBranches())

print("---------------- Task (iv) ---------------")
s1 = Saving_Account(1234,br1,500)
br1.addAccount(s1)

s2 = Saving_Account(1235,br4,1000)
br4.addAccount(s2)

c1 = Current_Account(5432,br1,0.10)
br1.addAccount(c1)

c2 = Current_Account(5431,br3,0.12)
br3.addAccount(c2)

print("---------------- Task (v) ---------------")
cs1 = Customer("Afif","Dhaka","01911111111")
cs2 = Customer("Sohan","Dhaka","01511111111")

#account s1 and c1 for customer cs1
cs1.setSavingAcc(s1)
cs1.setCurrentAcc(c1)
#account s2 and c2 for customer cs2
cs2.setSavingAcc(s2)
cs2.setCurrentAcc(c2)

s1.setCustomer(cs1)
c1.setCustomer(cs1)

s2.setCustomer(cs2)
c2.setCustomer(cs2)

print("---------------- Task (vi) ---------------")
customer2 = cs2.current_acc            #getting current account
# print(customer2)
print("cs2 customer current account number:", customer2.account_number)
print("current balance:", customer2.balance)
print("interest rate:",customer2.interest_rate)
brnch = customer2.branch
bnk =brnch.bank
print("branch code:",brnch.branch_code, "bank name:",bnk.name)

