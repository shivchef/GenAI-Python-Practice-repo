
chaitype = "chaiking"
def update_order():
    
    def kitchen():
         
        chaitype = "Kesar"
        def hello():
            nonlocal chaitype 
            chaitype = 'british' 
        hello()
    kitchen()
    print("After kitchen update", chaitype)

update_order()
print("After kitchen update", chaitype)


