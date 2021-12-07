def main():

    try:
        a = int(input("输入"))
        print(a[::-1])
    except:
        print("输入错误请重新输入")
        main()
    else:
        pass


if __name__ == '__main__':
    main()
