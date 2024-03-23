
class ProductDTO:
  def __init__(self, name, description, unit_price, making_cost,factory_id) -> None:
    self.name = name
    self.description = description
    self.unit_price = unit_price
    self.making_cost = making_cost
    self.factory_id = factory_id