import vlc as abc
'''def os():
    from OS import cmd 
    print(cmd)'''
def code(a):
    import inspect
    lines = inspect.getsource(abc)
    print(lines)
code("vlc")