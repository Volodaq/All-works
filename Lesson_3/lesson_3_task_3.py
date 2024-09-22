from Address import Address
from Mailing import Mailing

to_address = Address("350011", "Краснодар", "Стасова", "132", "11")
from_address = Address("620000", "Екатеринбург", "Ленина", "72", "26")

mailing = Mailing(to_address, from_address, 150, "отправление 1")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
