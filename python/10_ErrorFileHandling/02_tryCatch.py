arsenal = {"gun": 12,"grenade": 30}
try:
    arsenal["rifel"]
except KeyError:
    print("The key that you are trying to access doesnot exists")
print("\nThis will operate after try except")
