import time
import os

factory = ["car"]
distribution = []
shop = []

def factory_to_dtb():
    distribution.extend(factory)
    factory.clear()

def dtb_to_shop():
    shop.extend(distribution)
    distribution.clear()

def print_list():
    print("Factory = ",str(factory))
    print("Distribution = ",str(distribution))
    print("shop = ",str(shop))

def next_print():
    time.sleep(2)
    os.system('cls')

print_list()
factory_to_dtb()
next_print()
print_list()
dtb_to_shop()
next_print()
print_list()
