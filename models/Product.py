class Product:
    def __init__(self,product_name:str,description:str,fabrication_date:str,seller_id:int,genre:str,location:str,new_product:bool,product_id:int,quantity:int,preco:int):
        self.product_name=product_name
        self.description=description
        self.fabrication_date=fabrication_date
        self.seller_id=seller_id
        self.genre=genre
        self.location=location
        self.new_product=new_product
        self.product_id=product_id
        self.quantity=quantity
        self.preco=preco
        self.comments={}