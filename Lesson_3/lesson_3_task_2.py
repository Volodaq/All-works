from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 12 Pro", "+66924749130"))

for phone in catalog:
    print(phone.get_info())
