try:
    a = int(input())
    c= a // 2
except ZeroDivisionError:
    print("division error")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Hello")