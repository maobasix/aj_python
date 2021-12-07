def main():
    try:
        sd = float(input("输入上底"))
        xd = float(input("输入下底"))
        g = float(input("输入高"))
        print("面积为{:.2f}".format((sd + xd) * g / 2))
    except:
        main()
    else:
        pass


if __name__ == '__main__':
    main()
