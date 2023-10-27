import mobile as mob

TestManufacturer = input("Enter the Manufacturer: ")
TestModelNumber = input("Enter the Model Number: ")
TestRetailPrice = input("Enter the Retail Price: ")

TestPhone = mob.Phone(TestManufacturer, TestModelNumber, TestRetailPrice)

print("")
print("Here are the Phone details")
print("Phone Manufacturer: "+str(TestPhone.get_Manufacturer()))
print("Phone Model Number: "+str(TestPhone.get_Model()))
print("Phone Retail Price: $"+str(TestPhone.get_RetailPrice()))
