import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import phonemetadata

number=input("enter no.:")
phone_number = phonenumbers.parse(number)

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number(phone_number,'en'))
print(phonemetadata.NumberFormat(phone_number,'en'))
