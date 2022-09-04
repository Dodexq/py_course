def main():
    total = 0
    while True:
        try:
            num = input('Enter a number (q to quit): ')
            if num.lower() == 'q':
                print('Goodbye!')
                break
            num = int(num)
        except ValueError:
            print("Integer please")
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        else:
            total += num
            print(total)

main()