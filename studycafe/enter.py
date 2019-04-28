from decorators import debug

@debug
def greeter(name :str)->str:
    """greeter function to New Comer"""
    return 'Hello,%s' %(name) 
