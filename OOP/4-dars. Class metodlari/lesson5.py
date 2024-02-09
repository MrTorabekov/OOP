class ResourceHandler:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.open_resource()

    def open_resource(self):
        print(f"Resursni ochish : {self.resource_name}")

    def close_resource(self):
        print(f"Resursni yoping : {self.resource_name}")

    def __del__(self):
        self.close_resource()
        print(f"Resurs ishlovi uchun {self.resource_name} yo'q qilinmoqda")


resource = ResourceHandler("example_resource")

del resource
