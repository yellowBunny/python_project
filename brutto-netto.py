def brutto(n,tax):
    try:
        t=float(n)/(1+(int(tax)*.01))        
        return '\n{} netto w tym VAT {}'.format(round(t,2),round(float(n)-t,2))
    except ValueError as err:
        return 'błąd wartości --> {}'.format(err)  
kwota = input('\nWpisz kowtę Brutto: ')
tax = input('Wpisz VAT: ')
print(brutto(kwota,tax))
input()

