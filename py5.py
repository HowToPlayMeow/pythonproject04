def inputWitdhlong( ) :
    wi = float( input('กว้าง : ') )
    lo = float( input('ยาว : ') )
    return wi, lo

def inputBaseHigh( ) :
    ba = float( input('ฐาน : ') )
    hi = float( input('สูง : ') )
    return ba, hi

def calAndShowAreaSquare( ba, hi ) :
    area = ba * hi / 2
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')

wi, lo = inputWitdhlong( )
calAndShowAreaSquare(wi, lo)
print('--------------------------')
ba, hi = inputBaseHigh( )
calAndShowAreaSquare(ba, hi)