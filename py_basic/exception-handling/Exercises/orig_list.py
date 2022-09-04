import math

def main():
    
    orig_list=[1,2,4,"1234","abc",0,10,20]
    inv_list=[]

    for el in orig_list:
        try:
            inv_el=1/float(el)
        except ZeroDivisionError as e: 
            print(el,'-',e)
            inv_el=math.inf
        except ValueError as e:
            print(el,'-',e)
            inv_el=math.nan
        except Exception as e: 
            print("другая ошибка")
        else:
            print(el,"-", "без ошибок")
        finally:
            inv_list.append(inv_el)

    print("список обратных величин:",inv_list)        

main()