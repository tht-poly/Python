a=5
while a==5:


    print("POLY HESAP MAKİNESİ")

    print("Toplama yapmak için + tuşuna daha sonra ENTER tuşuna basınız.")
    print("Çıkartma yapmak için - tuşuna daha sonra ENTER tuşuna basınız.")
    print("Çarpma yapmak için x tuşuna daha sonra ENTER tuşuna basınız.")
    print("Bölme yapmak için / tuşuna daha sonra ENTER tuşuna basınız.")
    s=input("Hangi işlemi yapmak istersiniz ?:")

    if s == '+':
        ilksayi=int(input("Toplamak istediğiniz ilk sayıyı giriniz.:"))
        ikincisayi=int(input("Toplamak istediğiniz ikinci sayıyı giriniz.:"))
        sonuc=ilksayi+ikincisayi
        print(ilksayi,"+",ikincisayi,"=",sonuc)
    elif s == '-':
        ilksayi=int(input("Çıkarmak istediğiniz ilk sayıyı giriniz.:"))
        ikincisayi=int(input("Çıkarmak istediğiniz ikinci sayıyı giriniz.:"))
        sonuc=ilksayi-ikincisayi
        print(ilksayi,"-",ikincisayi,"=",sonuc)
    elif s == 'x':
        ilksayi=int(input("Çarpmak istediğiniz ilk sayıyı giriniz.:"))
        ikincisayi=int(input("Çarpmak istediğiniz ikinci sayıyı giriniz.:"))
        sonuc=ilksayi*ikincisayi
        print(ilksayi,"*",ikincisayi,"=",sonuc)
    elif s == '/':
        ilksayi=int(input("Bölmek istediğiniz ilk sayıyı giriniz.:"))
        ikincisayi=int(input("Bölmek istediğiniz ikinci sayıyı giriniz.:"))
        sonuc=ilksayi/ikincisayi
        print(ilksayi,"/",ikincisayi,"=",sonuc)
    else :
        print("Hatalı işlem yaptınız.")
