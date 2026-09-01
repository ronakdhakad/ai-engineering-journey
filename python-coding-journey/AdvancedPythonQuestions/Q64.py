# 64. Implement Context Manager
# A Context Manager is used to manage resources (such as files) automatically. It is implemented using:
# __enter__()
# __exit__()

class Demo:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("End")

with Demo():
    print("Working...")