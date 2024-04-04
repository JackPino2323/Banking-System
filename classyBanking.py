class Account:
    # The initializing function
    def __init__(self, sOwner, iID, fBalance):
        self.sOwner = sOwner
        self.iID = iID
        self.fBalance = fBalance
    
    # Returns sOwner
    def getOwner(self):
        return self.sOwner
    
    # Returns iID 
    def getID(self):
        return self.iID
    
    # Returns fBalance 
    def getBalance(self):
        return self.fBalance
    
    # Sets sOwner to the value included in the parameters
    def setOwner(self, sOwner):
        self.sOwner = sOwner
        
    # Sets iID to the value included in the parameters
    def setID(self, iID):
        self.iID = iID
        
    # Sets fBalance to the value included in the parameters
    def setBalance(self, fBalance):
        self.fBalance = fBalance
    
    # Adds the amount to the fBalance value
    def deposit(self, amount):
        self.fBalance += amount
    
    # Subtracts the amount from the fBalance value
    def withdraw(self, amount):
        self.fBalance -= amount
        if self.fBalance < 0:
            print('Warning: Your account balance has fallen below 0. A $5 penalty has been deducted from your account.')
            self.fBalance -= 5
            
    # Prints out all of the values included in the Account object
    def printAccountInfo(self):
        print('Owner: ' + self.sOwner)
        print('ID: ' + str(self.iID))
        print('Balance: ' + str(self.fBalance))

                
    
class CheckingAccount(Account):
    # The initializing method
    def __init__(self, sOwner, iID, fBalance, iTF):
        super().__init__(sOwner, iID, fBalance)
        self.iTF = iTF
        self.iTC = 0

    # Returns iTC 
    def getTransactionCount(self):
        return self.iTC
    
    # Returns iTF 
    def getTransactionFee(self):
        return self.iTF
    
    # Sets iTC to the value included in the parameters
    def setTransactionCount(self, iTC):
        self.iTC = iTC
    
    # Sets iTF to the value included in the parameters
    def setTransactionFee(self, iTF):
        self.iTF = iTF
    
    # Adds the amount to fBalance and adds 1 to iTC, then calls the deductFees function
    def deposit(self, amount):
        self.fBalance += amount
        self.iTC += 1
        self.deductFees()
    
    # Subtracts the amount from fBalance and adds 1 to iTC
    # Prints a warning message and subtracts a $5 penalty from fBalance if fBalance is below 0
    # Then calls the deductFees function
    def withdraw(self, amount):
        self.fBalance -= amount
        self.iTC += 1
        if self.fBalance < 0:
            print('Warning: Your account balance has fallen below 0. A $5 penalty has been deducted from your account.')
            self.fBalance -= 5
        self.deductFees()
    
    # subtracts iTF from fBalance if iTC equals 5
    def deductFees(self):
        if self.iTC == 5:
            self.fBalance -= self.iTF
            self.setTransactionCount(0)
    
    
    
class SavingsAccount(Account):
    # The initializing function
    def __init__(self, sOwner, iID, fBalance, fIR):
        super().__init__(sOwner, iID, fBalance)
        self.fIR = fIR
        
    # Returns fIR
    def getInterestRate(self):
        return self.fIR
    
    # Sets fIR to the value included in the parameters
    def setInterestRate(self, fIR):
        self.fIR = fIR
        
    # Subtracts the amount from fBalance
    # Prints a warning message and subtracts a $5 penalty from fBalance if fBalance is below 0
    def withdraw(self, amount):
        self.fBalance -= amount
        if self.fBalance < 0:
            print('Warning: Your account balance has fallen below 0. A $5 penalty has been deducted from your account.')
            self.fBalance -= 5
            self.fIR = 0

    # Adds the product of fBalance and fIR to fBalance
    def applyInterest(self):
        self.fBalance = self.fBalance * (self.fIR + 1)
            
            
def main():
# Tests for the Account class
    testGetOwner()
    testGetID()
    testGetBalance()
    testSetOwner()
    testSetID()
    testSetBalance()
    testDeposit()
    testWithdraw()
# Tests for the Checking class
    testGetTransactionCount()
    testGetTransactionFee()
    testSetTransactionCount()
    testSetTransactionFee()
    testCheckingDeposit()
    testCheckingWithdraw()
    testDeductFees()
# Tests for the Savings class
    testGetInterestRate()
    testSetInterestRate()
    testSavingsWithdraw()
    testApplyInterest()

###############################
# Tests for the Account class #
###############################
newAccount = Account('Jack', 1, -19.16)
newAccount2 = Account('Natalia', 2, 553.91)

# Tests if the getOwner function works properly
def testGetOwner():
    assert newAccount.getOwner() == 'Jack', 'The getOwner function did not return the correct value'
    assert newAccount2.getOwner() == 'Natalia', 'The getOwner function did not return the correct value'

# Tests if the getID function works properly
def testGetID():
    assert newAccount.getID() == 1, 'The getID function did not return the correct value'
    assert newAccount2.getID() == 2, 'The getID function did not return the correct value'

# Tests if the getBalance function works properly
def testGetBalance():
    assert newAccount.getBalance() == -19.16, 'The getBalance function did not return the correct value'
    assert newAccount2.getBalance() == 553.91, 'The getBalance function did not return the correct value'

# Tests if the setOwner function works properly
def testSetOwner():
    newAccount.setOwner('Jack Pino')
    assert newAccount.getOwner() == 'Jack Pino', 'The setOwner function should have set sOwner to "Jack Pino"'
    newAccount2.setOwner('Natalia Ivanov')
    assert newAccount2.getOwner() == 'Natalia Ivanov', 'The setOwner function should have set sOwner to "Natalia Ivanov"'
    
# Tests if the setID function works properly
def testSetID():
    newAccount.setID(23)
    assert newAccount.getID() == 23, 'The setID function should have set iID to 23'
    newAccount2.setID(6)
    assert newAccount2.getID() == 6, 'The setID function should have set iID to 6'

# Tests if the setBalance function works properly
def testSetBalance():
    newAccount.setBalance(100.01)
    assert newAccount.getBalance() == 100.01, 'The setBalance function should have set fBalance to 100.01'
    newAccount2.setBalance(200)
    assert newAccount2.getBalance() == 200, 'The setBalance function should have set fBalance to 200.02'
    
# Tests if the deposit function works properly when dealing with positive and negative values
def testDeposit():
    newAccount.deposit(10)
    assert newAccount.getBalance() == 110.01, 'The deposit function did not work as intended'
    newAccount2.deposit(-10)
    assert newAccount2.getBalance() == 190, 'The deposit function did not work as intended'

# Tests if the withdraw function works properly when dealing with positive and negative values
# Also checks that fBalance is decreased by 5 if it is less than 0
def testWithdraw():
    newAccount.withdraw(-10)
    assert newAccount.getBalance() == 120.01, 'The withdraw function did not work as intended'
    newAccount2.withdraw(200)
    assert newAccount2.getBalance() == -15, 'The withdraw function did not work as intended'
    
#######################################
# Tests for the CheckingAccount class #
#######################################
newChecking = CheckingAccount('Gabe', 3, 101.01, 2)
newChecking2 = CheckingAccount('Evan', 4, 202.02, 3)

# Makes sure that the getTransactionCount function works properly
def testGetTransactionCount():
    assert newChecking.getTransactionCount() == 0, 'There have not been any transactions yet, so iTC should still be 0'
    newChecking.deposit(10.1)
    assert newChecking.getTransactionCount() == 1, 'After the previous transaction, iTC should be at 1'
    
# Makes sure that the getTransactionFee function works properly
def testGetTransactionFee():
    assert newChecking.getTransactionFee() == 2, 'The getTransactionFee function did not return the correct value'
    assert newChecking2.getTransactionFee() == 3, 'The getTransactionFee function did not return the correct value'
    
# Makes sure that the getTransactionCount function works properly
def testSetTransactionCount():
    newChecking.setTransactionCount(1)
    assert newChecking.getTransactionCount() == 1, 'The setTransactionCount function should have set iTC to 1'
    newChecking2.setTransactionCount(2)
    assert newChecking2.getTransactionCount() == 2, 'The setTransactionCount function should have set iTC to 2'
    
# Makes sure that the setTransactionFee function works properly
def testSetTransactionFee():
    newChecking.setTransactionFee(5)
    assert newChecking.getTransactionFee() == 5, 'The setTransactionFee function should have set iTF to 5'
    newChecking2.setTransactionFee(6)
    assert newChecking2.getTransactionFee() == 6, 'The setTransactionFee function should have set iTF to 6'
    
# Makes sure that the deposit function for the Checking class works properly when dealing with positive and negative values
# Also checks that the iTC value gets increased by 1
def testCheckingDeposit():
    newChecking.deposit(-10)
    assert newChecking.getBalance() == 101.11 and newChecking.getTransactionCount() == 2, 'fBalance should have been decreased by -10 and iTC increased by 1'
    newChecking2.deposit(10)
    assert newChecking2.getBalance() == 212.02 and newChecking2.getTransactionCount() == 3, 'fBalance and iTC should have been increased by 10 and 1 respectivly'
    
# Makes sure that the withdraw function for the Checking class works properly when dealing with positive and negative values
# Also checks that the iTC value gets increased by 1, and that fBalance is decreased by 5 if it is less than 0
def testCheckingWithdraw():
    newChecking.withdraw(-10)
    assert newChecking.getBalance() == 111.11 and newChecking.getTransactionCount() == 3, 'fBalance and iTC should have been increased by 10 and 1 respectivly'
    newChecking2.withdraw(217.02)
    assert newChecking2.getBalance() == -10 and newChecking2.getTransactionCount() == 4, 'fBalance should have been decreased by -222.02 after the withdrawel plus fees and iTC increased by 1'
    
# Makes sure that the deductFees function subtracts 5 from fBalance after iTC reaches 5
# Also makes sure that deductFees does nothing if iTC is below 5
def testDeductFees():
    newChecking.deposit(5)
    assert newChecking.getBalance() == 116.11, 'Because iTC only increased from 3 to 4, fBalance gets adjusted normally after calling the deposit function'
    newChecking.deposit(5)
    assert newChecking.getBalance() == 116.11, 'iTC should have been increased to 5, and subsequently deducted 5 from fBalance, causing no change in fBalance'
######################################
# Tests for the SavingsAccount class #
######################################
newSavings = SavingsAccount('Matthew', 10, 1000, .02)
newSavings2 = SavingsAccount('Charlie', 11, 2000, .04)

# Makes sure that the getInterestRate function works properly
def testGetInterestRate():
    assert newSavings.getInterestRate() == .02, 'The getInterestRate function did not return the correct value'
    assert newSavings2.getInterestRate() == .04, 'The getInterestRate function did not return the correct value'
    
# Makes sure that the setInterestRate function works properly
def testSetInterestRate():
    newSavings.setInterestRate(.05)
    assert newSavings.getInterestRate() == .05, 'fIR should have been set to .05'
    newSavings2.setInterestRate(.07)
    assert newSavings2.getInterestRate() == .07, 'fIR should have been set to .07'
    
# Makes sure that the withdraw function for the Savings class works properly when dealing with positive and negative values
# Also checks that fIR is set to 0 and that fBalance is decreased by 5 if it is less than 0
def testSavingsWithdraw():
    newSavings.withdraw(1005)
    assert newSavings.getBalance() == -10 and newSavings.getInterestRate() == 0, 'fBalance should have been decreased by 1010 after the withdrawel plus fees'
    newSavings2.withdraw(-10)
    assert newSavings2.getBalance() == 2010, 'fBalance should have been increased by 10 after the withdrawel'
    
# Makes sure that the correct amount of interest is applied to fBalance
def testApplyInterest():
    newSavings.setBalance(100)
    newSavings.setInterestRate(.05)
    newSavings.applyInterest()
    assert newSavings.getBalance() == 105, 'fBalance should have been increased by 5 after applying the 5% interest rate'
    newSavings2.setBalance(200)
    newSavings2.applyInterest()
    assert newSavings2.getBalance() == 214, 'fBalance should have increased by 14 after applying the 7% interest rate'

if __name__ == "__main__":    
    main()
