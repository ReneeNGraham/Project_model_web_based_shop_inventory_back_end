import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

# manufacturer_repository.delete_all()
# product_repository.delete(all)


manufacturer1 = Manufacturer("Honeywell", "Producer of health and safety, protective equipment")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer ("Mandor's Fabric Shop", "Fabric shop and producer of fashion masks, bandanas and clothing")
manufacturer_repository.save(manufacturer2)

product1 = Product("Plain nets", manufacturer1, "hairnets", 50, 2.00, 4.00)
product_repository.save(product1)

product2 = Product("Exrtra protective gloves", manufacturer2, "surgical gloves", 40, 1.00, 3.00)
product_repository.save(product2)

pdb.set_trace()

