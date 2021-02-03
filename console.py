import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

product_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer1 = Manufacturer("Honeywell", "Producer of health and safety, protective equipment")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer ("Mandor Fabric Shop", "Fabric shop and producer of fashion masks, bandanas and clothing")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer ("Soap Works" , "Hygiene products and general cosmetic soaps")
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer ("Disposable Supplies" , "Suppliers of toiletries and disposable materials and miscellaneous items")
manufacturer_repository.save(manufacturer4)

product1 = Product("Plain nets", manufacturer1, "hairnets", 50, 2.00, 4.00)
product_repository.save(product1)

product2 = Product("Xtra protective gloves", manufacturer1, "surgical gloves", 40, 1.00, 3.00)
product_repository.save(product2)

product3 = Product("Xtra protective masks", manufacturer1, "surgical masks", 100, 1.00, 2.50)
product_repository.save(product3)

product4 = Product("Fabulous fabric masks", manufacturer2, "fashion masks", 35, 2.00, 5.00)
product_repository.save(product4)

product5 = Product("Brilliant bandanas", manufacturer2, "bandanas", 20, 3.00, 6.00 )
product_repository.save(product5)

product6 = Product("Handy sanitiser", manufacturer3, "hand sanitiser", 50, 2.00, 5.00)
product_repository.save(product6)

product7 = Product("Handy liquid soap", manufacturer3, "liquid hand soap", 40, 2.00, 5.00)
product_repository.save(product7)

product8 = Product("Behind the scenes", manufacturer4, "toilet paper", 20, 3.00, 6.00)
product_repository.save(product8)

product9 = Product("Hand me dat wipe", manufacturer4, "hand wipes", 90, 2.00, 6.00)
product_repository.save(product9) 


pdb.set_trace()