class Catalogue:

    def __init__ (self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        products_starts_with_letter = []
        for product in self.products:
            if product[0] == first_letter:
                products_starts_with_letter.append(product)
        return products_starts_with_letter

    def __repr__ (self):
        product = sorted(self.products)
        return f"Items in the {self.name} catalogue:\n" + "\n".join(product)

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)