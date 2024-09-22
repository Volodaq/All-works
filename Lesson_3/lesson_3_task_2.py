from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 12 Pro", "+66924749130"))
catalog.append(Smartphone("Apple", "iPhone 14", "+79189457471"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79189457472"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79189457473"))
catalog.append(Smartphone("Google", "Pixel 7", "+79189457474"))
catalog.append(Smartphone("Sony", "Xperia 5", "+79189457475"))

for phone in catalog:
    print(phone)
