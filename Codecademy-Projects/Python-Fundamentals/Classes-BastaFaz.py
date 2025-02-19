from datetime import time

### Menu
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = time(hour=start_time)
    self.end_time = time(hour=end_time)
  def __repr__(self):
    return f'{self.name} is served from {self.start_time.strftime("%H")} till {self.end_time.strftime("%H")} hrs'
  def calculate_bill(self, purchased_items):
    tot_price = 0
    for i in purchased_items: tot_price += self.items[i]
    return tot_price


brunch = Menu('Brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu('Early bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu('Dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu('Kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

print(brunch)

# Calculate bill
breakfast_order_sum = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
print(breakfast_order_sum)
early_order_sum = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli'])
print(early_order_sum)

### Franchise
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, hr):
    t = time(hour=hr)
    return [m for m in self.menus if m.start_time <= t <= m.end_time]
    

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])
print(flagship_store)

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))

### Businesess
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return self.name


basta_faz = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(basta_faz.franchises)

arepas_menu = Menu('Take a’ Arepa', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

take_arepa = Business("Take a' Arepa", [arepas_place])
print(take_arepa.franchises)
