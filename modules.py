# 3 çeşit
# python built-in modules -> math
# local modules (proje bazlı) -> inheritance.py
# 3. taraf kütüphaneler
#import math # bütün math modülünü al
from math import sqrt as karekok # math kütüphanesinden yalnızca sqrt'u al
# alias -> takma ad
from inheritance import Truck
import requests

print(karekok(25))

truck2 = Truck("Scania")
truck2.start()

response = requests.get("https://google.com")
print(response.status_code)
