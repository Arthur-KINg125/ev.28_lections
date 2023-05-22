from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
import json


class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
        return "Saved!"
    

    class Comment(CreateMixin, ReadMixin, DeleteMixin):
        pass


smartphones = Product()
print(smartphones.post(title='Redmi Note 10', desc_='The best', qty=10, price=250))
print(smartphones.post(title='Redmi Note 20', desc_='The best', qty=5, price=500))
print(smartphones.post(title='Iphone 14 pro max', desc_='The best', qty=5, price=1000))
print(smartphones.post(title='Samsung S22 Ultra', desc_='The best', qty=3, price=750))
print(smartphones.post(title='Iphone 13 Pro max', desc_='The best', qty=15, price=666))
print()
print()
print(smartphones.list())
print()
print(smartphones.detail(4))
print(smartphones.detail(15))
print()
print(smartphones.patch(1, title='Redmi Note 9'))
print()
print(smartphones.list())
print()
print(smartphones.delete(-1))
print(smartphones.delete(1))
print(smartphones.save())