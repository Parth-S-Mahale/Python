"""
# python one.py
"""

"""
python directly assigns the string "__main__" 
to the __name__ variable in background given 
below:
 
__name__ = "__main__"
"""

def func():
    print("FUNC() IN one.py")

print("TOP LEVEL IN one.py")

if __name__ == "__main__":
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')