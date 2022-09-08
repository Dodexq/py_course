import datetime

def is_summer(date_today):
    
    summer_start = datetime.date(2022, 6, 20)
    fall_start = datetime.date(2022, 9, 22)
    
    return (summer_start < date_today < fall_start)

def main():
    while True:
        try: 
            input_date = input("What day is it today? example (07 09 2022) ").split()
            date_dict = {"year":int(input_date[2]), "month":int(input_date[1]), \
                "day":int(input_date[0])}
            date_today = datetime.date(**date_dict)
        except Exception:
            print("Something is wrong, please enter the date from the example")
            continue

        else:
            print("wear You should wear white pants") if is_summer(date_today) \
            else print("You should wear black pants")

main()