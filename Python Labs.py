def  is_isogram(word):
	if type(word) != str :
		raise 'Argument should be string'
	else:
		word =  word.lower()
		for i in word:
			if  word.count(i)> 1 or word == ' ':
				return (word, False)
		return (word, True)




def remove_duplicate(string):
	new_string = ""
	count =0
	for i in string.lower():
		if i not in new_string:
			new_string +=i
		else:
			count +=1
		result =(''.join(sorted(new_string)), count)
	return result


def power(x,y):
	if y == 0:
		return 1
	else:
		return x*power(x, y-1)


def my_sort(n):
	even=[]
	odd =[]
	if type(n)!= list:
		return'Invalid input'
	else:
		for num in n:
			if num%2 != 0:
				odd.append(num)
			else:
				even.append(num)
				even.sort()
			result = odd + even
		return result

def my_sort(list):
	odd = [x for x in list if x%2 != 0]
	even = [y for y in list if y%2 == 0]
	even.sort()
	result = odd + even
	return result



class ShoppingCart():
	def  __init__(self):
		self.total = 0
		self.items ={}
	def add_item(self,item_name,quantity,price):
		if  not item_name in self.items:
			self.items[item_name] = quantity
			self.total += (price * quantity)
		else:
			self.total += (price * quantity)
		
	def remove_item(self,item_name,quantity,price):
		if item_name in self.items:
			if quantity > item_name[quantity]:
				del self.items[item_name]
				self.total -= (price * quantity)
				return self.items
			else:
				del self.items[item_name]
				self.total -= (price * quantity)
				return self.items


	def checkout(self,cash_paid):
		if cash_paid < self.total:
			return 'Cash paid not enough'
		elif cash_paid == self.total:
			return 'Cost fully paid'

		else:
			balance = self.total - cash_paid
			return balance

class Shop(ShoppingCart):
	def __init__(self):
		self.quantity = 100

	def remove_item(self):
		self.quantity -= 1





class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if not item_name in self.items:
           self.total += (quantity * price)
           self.items[item_name] = quantity
        
    def remove_item(self, item_name, quantity, price):
        if quantity > self.items[item_name]:
            self.items[item_name] = 0
            self.total-= (quantity * price)
        else:
            self.items[item_name]-= quantity
            self.total-=  (quantity * price) 
        
    def checkout(self, cash_paid):
        if self.total > cash_paid:
            return 'Cash paid not enough'
        else:
            return (cash_paid - self.total)
            
class Shop(ShoppingCart):
  
    def __init__(self):
        self.quantity = 100
    
    def remove_item(self):
		self.quantity -= 1