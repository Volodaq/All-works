from Address import Address
from Mailing import Mailing

from Address import Address
from Mailing import Mailing
to_address = Address("350011", "Краснодар", "Стасова", "132", "11")
from_address = Address("654321", "Екатеренбург", "Ленина", "76", "51")
mailing = Mailing(to_address, from_address, 150, "TRK123456")
print(mailing)
