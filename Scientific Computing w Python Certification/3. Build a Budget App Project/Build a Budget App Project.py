class Category:
    def __init__(self, name):
        self.ledger = [] # Initialize as empty list to store transactions
        self.name = name 
        self.balance = 0.0
        self.spent = 0.0
    
    def __str__(self):
        # format output string
        title = self.name.center(30, '*')
        result = title+ '\n' # Title
        #running_balance = 0.0
        
        for entry in self.ledger:
            desc = entry.get('description', '')[:23] # Limit to 23 chars
            amount = f"{entry['amount']:.2f}" # 2 decimals
            #running_balance += entry['amount']
            #balance = f'{running_balance:.2f}'
            
            result += f"{desc:<23}{amount:>7}\n" #left align desc, right align amount    
        result += f'Total: {self.balance:.2f}' # remove trailing newline
        return result
        

    def check_funds(self, amount):
        return self.balance >= float(amount) #True if enough funds, False otherwise
        
    def get_balance(self): 
        return self.balance


    def transfer(self, amount, category):
        amount = float(amount)
        if self.check_funds(amount):    
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def deposit(self, amount, description = ''): 
        amount = float(amount)
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        self.balance += float(amount)
        return True # Indicate success
        

    def withdraw(self, amount, description = ''): 
        amount = float(amount)
        if self.check_funds(amount):    
            self.ledger.append({
                'amount': -amount,
                'description': description
                })
            self.balance -= amount
            self.spent += amount
            return True # Success
        else:
            return False # Failure due to insufficient funds
        
   

        
            
food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
#food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(45.29, 'shirt')
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(25, 'wipers')
print(food)
print(clothing)
print(auto)

def create_spend_chart(categories):
    total_spent = 0.0
    for category in categories:
        total_spent += category.spent
    percentages = []
    for category in categories:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = (category.spent / total_spent) * 100
        percentage = (percentage // 10) * 10
        percentages.append(percentage)
    
    result = 'Percentage spent by category\n'
    
    for level in range(100, -1, -10):
        level_str = f"{level:>3}|"
        bar = " "
        for percentage in percentages:
            if percentage >= level:
                bar += "o  "
            else:
                bar += "   "
        result += level_str + bar + "\n"

    num_categories = len(categories)
    line_length = (num_categories * 3) +1
    result += '    ' + ('-' * line_length) + '\n'
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "     "  # 5 spaces
        for j, category in enumerate(categories):
            char = category.name[i] if i < len(category.name) else " "
            line += char + "  "  # Always add two spaces after each character
        line = line[:14]  # Trim to 14 characters to match bar line length
        result += line + "\n"
    return result.rstrip('\n')
print(create_spend_chart([food, clothing, auto]))   

