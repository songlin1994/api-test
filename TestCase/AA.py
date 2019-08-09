from Common import Assert, read_excel, Request

request = Request.Request()
assertions = Assert.Assertions()

if __name__ == '__main__':
    num =0
    for i in range(1,100):
        if i%2==1:
            num = num+1/i
    print(num)