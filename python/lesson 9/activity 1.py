class employee :

    def __init__(self):
        print("Empployee created")

    def __del__(self):
        print("Destructor called , employee deleated")

obj = employee()
del obj            