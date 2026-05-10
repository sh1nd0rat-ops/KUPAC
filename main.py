#pythonの基礎の基礎
print(100*5+40*8)
print(10*20)
print(5%3)
print(10%2)
print(-100)
print(100+-99)
print(10**3)
print(0.1)
print(1.00)
print(10+20)
print(1.2+1.3)
print(3/2)
print(3/3) #割り切れても小数点数以下が0のfloat型になる．
print(10+20.0) #片方がfloat型のとき，その和もfloat型になる．
print(0.1+0.2)
print((100*5)+(40*8)+(80*5)+(60*10)+(90*20)+(110*10))
video = 100*5
label = 40*8
print(video + label) #変数は計算式の中で値の代わりに使える．
abs(-123)
print(abs(-123)) #-123がこの関数の引数である．この関数は引数の絶対値を返す．
#123が戻り値である．
print(abs(100-200)/2)
minus_value = 100*-1
abs(minus_value)
print(abs(minus_value))
abs_value=abs(-10)
print(abs_value)

#関数の例
abs(-10) #引数が-10のとき，この関数は10を返す．
round(1.12,1) #この関数は有効数字を指定された桁数に丸める．この場合は小数点以下1桁に丸める．
min(10,20) #この関数は引数の中で最小の値を返す．この場合は10を返す．
max(10,20) #この関数は引数の中で最大の値を返す．この場合は20を返す．
int(10.5)#この関数は引数を整数に変換する(切り捨て)．この場合は10を返す．
float(10) #この関数は引数を浮動小数点数に変換する．この場合は10.0を返す．
import math #mathモジュールをインポートする．
math.sqrt(2.0) #この関数は引数の平方根を返す．
print(round(math.sqrt(2.0),5))
#abs()など，関数の中にはモジュールをインポートせずに使えるものもある(組み込み関数).
import calendar
print(calendar.prmonth(1970,5))

#文字列と入出力
print(123)
print("123") #文字列はダブルクォーテーションで囲む．
123+345
"123+234"
"ABC"+"DEF" #文字列の連結．
123*456
int("123") #この関数は引数を整数に変換する．この場合は123を返す．
text = "123.4"
float(text) #この関数は引数を浮動小数点数に変換する．この場合は123.4を返す．
str(123)
num = 123.456
str(num)
height = 172
print("わたしの身長は"+str(height)+"cmです．")
input("好きな文字を入力してください：") #この関数はユーザーからの入力を待ち，入力された文字列を返す．
name = input("あなたの名前を入力してください：")
print("こんにちは，"+name+"さん！")
text = "lower letters"
upper_text = text.upper() #この関数は引数の文字列をすべて大文字に変換する．
print(upper_text) #データに結び付いた関数をメソッドと呼ぶ．この場合はupper()がtextというデータに結び付いている．
text = "The shells she sells are sea-shells, I'm sure."
text.find("sea")#関数とメソッドの違いは引数の数にある．関数は引数を複数とることができるが，メソッドは引数を1つしかとらない．この場合は"sea"という文字列を引数としてとる．
data = 0.25
data.as_integer_ratio()
text = input("好きな文章を入力してください：")
print(text+"を小文字に変換すると"+text.lower()+"になります") 

#条件式と分岐
100>50
12>100
100<=100
100==10
100!=100
"A"<"Z"<"z" #文字列の比較は辞書順で行われる．この場合は"A"が最も小さく，次に"Z"，最後に"z"が最も大きい．
"123"<"234"
"python-1"<"python-a"
a = 100
if a==100:
    print("100点満点！")#インデントはスペース4つ分が一般的．インデントはコードのブロックを表す．この場合はif文のブロックを表す．
a = 99
if a==100:
    print("100点満点！")
else:
    print("残念ながら満点ではありません．")
print("123は数字ですか？", "123".isdecimal())#この関数は引数の文字列が数字で構成されているかどうかを判定する．
string = input("文字列を入力してください：")
if string.isdecimal():
    print(string+"は数字です")
else:
    print(string+"は数字ではありません")
string = input("文字列を入力してください：")
if string.isalpha():
    print(string+"はアルファベットで構成されています")
elif string.isdecimal():
    print(string+"は数字で構成されています")
else:
    print(string+"はアルファベットでも数字でも構成されていません")

#プール型と論理演算子
1+2
1<2 #プール型は真と偽の2つの値をとるデータ型．
true_value = True
false_value = False
print(true_value)
print(false_value)
height = input("身長を入力してください：")
120 <= int(height)
age = 11
height = 110
if (10<=age)and(120<=height):
    print("OK!")
else:
    print("NG!")
A = True
B = False
C = A and B
print(C)
age = int(input("年齢を入力してください："))
if not((int(age) >= 10) or (int(age) <= 80)):
    print("ご遠慮ください")
else:
    print("お乗りいただけます")

#while文によるループ
text = ""
while text != "finish":
    text = input("finishと入力すんなよ？")
    print(text+"と入力されました")
print("終了しました")
counter = 1 
while counter <= 5:
    text = input("数字を入力してください：")
    if text == "999":
        break
    if text.isdigit():
        number = int(text)
        print(str(counter)+"回目，"+str(number*number))
        counter = counter + 1
    else:
        print("数字を入力してください")

print("終了しました")
i = 0
while i < 10:
    i = i + 1
    if(i % 2) == 1:
        continue
    print(str(i)+"is even")
counter = 1
while counter <= 10:
    text = input("数字を入力してください：")
    if not text.isdigit():
        print("入力し直してください")
        continue
    if text == "999":
        print("中断します")
        break
    
    number = int(text)
    print(str(counter)+"回目，"+str(number*number))
    counter += 1

#関数の定義
momo = input("個数を入力してください：")
mikan = input("個数を入力してください：")
kakaku_momo = 100
kakaku_mikan = 40
total = (kakaku_momo*int(momo))+(kakaku_mikan*int(mikan))
print("合計金額は"+str(total)+"円です")
def calculate_total_price(momo,milan):#関数の定義．この関数は引数としてmomoとmilanをとる．
    kakaku_momo = 100
    kakaku_mikan = 40
    total = (kakaku_momo*int(momo))+(kakaku_mikan*int(milan))
    return total#returnとはこの関数の戻り値を指定するキーワード．
total = calculate_total_price(2,12325)
print(total)
#ローカル変数とグローバル変数の違いは変数の有効範囲にある．ローカル変数は関数の中で定義された変数であり，その関数の中でしか使えない．グローバル変数は関数の外で定義された変数であり，どこでも使える．
global_value = 200
def test_global(arg):
    return arg * global_value
print(test_global(10))#global_valueは関数の外で定義されたグローバル変数であるため，関数の中でも使える．
def func1(name):
    print( f"Hello {name}, this is func1")

def func2():
    func1(" func2")

func2()#func2はfunc1を呼び出している．このように関数の中で別の関数を呼び出すことができる．
import time
def print_time():
    now = time.asctime()
    print(f"It is {now} now.")
print_time()#この関数は引数を必要としない．
def func(arg1, arg2, arg3):
    print(f"arg1 is {arg1}, arg2 is {arg2}, arg3 is {arg3}")
func(1,2,3)
func(arg3=3,arg2=123,arg1=0)#引数の順番を入れ替えても，キーワード引数を使うことで正しく値を渡すことができる．
def func1(arg=999):
    print(arg)
func1(12345)
func1()#引数を省略した場合は，デフォルト引数が使われる．この場合は999が使われる．
def calculate_total_price(momo,milan,name="上"):
    kakaku_momo = 100
    kakaku_mikan = 40
    total = (kakaku_momo*int(momo))+(kakaku_mikan*int(milan))
    print(f"{name} 様：合計金額は{total}円です")
calculate_total_price(2,3,"でゅんこ")

#Pythonの型とオブジェクト
def foo():#関数もオブジェクトである．
    print("hi!")
import math #モジュールもオブジェクトである．
station = ["東京","品川","新横浜","小田原","熱海"]
cases = [100,25,110,135,93,95,93]
print(cases)
empty_list = []
print(empty_list)
print(station[3])
total_cases  = sum(cases)
print(total_cases)
values = ["A","B","C"]
print(values)
values.insert(0,999)
print(f"修正後{values}")
values[2] = "123435"
print(f"修正後{values}")
del values[0]
print(f"修正後{values}")
cases = [100,25,110,135,93,95,93]
print(cases)
index = 0
total = 0
while index < len(cases):
    total = total + cases[index]
    index += 1
print(total)
values = [1,2,3,4,5]
for value in values:
    print(f"valueは{value},value*valueは{value*value}") #while文よりもfor文の方が簡潔に書ける．
total = 0
cases = [100,125,110,135,93,95,93]
for case in cases:
    total += case
print(f"合計人数は{total}")

#辞書オブジェクト
#辞書はキーと値のペアを格納するデータ構造．キーはユニークでなければならない．値は重複してもよい．辞書は波括弧{}で囲む．
english_word = {"apple": "りんご","orange": "みかん","peach": "もも"}
print(english_word["apple"])
empty_dict = {}
print(empty_dict)
english_word["grape"] = "ぶどう"
print(english_word)
english_word["grape"] = "紫"
print(english_word)
del english_word["grape"]
print(english_word)
print(len(english_word))
print("apple" in english_word)
print("grape" in english_word)
text = input("文字列を入力してね：")
if text in english_word:
    print(f"{text}は{english_word[text]}です")
else:
    print(f"{text} は登録されてねえよ")

#タプルとコレクション
ningyocho = 35.686321, 139.783757 #タプルは丸括弧()で囲む．タプルはリストと似ているが，リストは変更可能であるのに対して，タプルは変更不可能である．
print(ningyocho)
kotoshi = "平成", 2
print(kotoshi)
ningyocho = (35.686321, 139.783757)
ido = ningyocho[0]
keido = ningyocho[1]
print(f"人形町の緯度は{ido}，経度は{keido}です")
value1 = (1,2,3)
value2 = (1,2,3)
value3 = (2,3,4)
print(value1 == value2)
print(value1 == value3)
print(value1 < value3)#タプルの比較は要素ごとに行われる．この場合は，最初の要素が同じであるため，次の要素を比較する．次の要素も同じであるため，最後の要素を比較する．
value4 = (1,2)
print(value1 < value4) #このように要素の数は異なるときは，要素数が少ない方が小さいとされる．
dict1 = {"dog": "犬", "cat": "猫"}
dict2 = {"dog": "犬", "cat": "猫"}
print(f"dict1とdict2は等しいか？{dict1 == dict2}")
list_obf =  ["pen", "bool", "notebook"]
if "book" in list_obf:
    print("list_obfにbookが登録されています")
print("pencil" in list_obf)
str_obj = "Hello, world!"
print("w" in str_obj)
print("x" in str_obj)
str_obj = "abracadabra"
print("cad" in str_obj)
list_obj = ["apple", "orange", "banana"]
for item in list_obj:
    upper_name = item.upper()
    print(upper_name)
tuple_obj = ("apple", "orange", "banana")
for fruit_name in tuple_obj:
    lower_name = fruit_name.lower()
    print(fruit_name)
values = [10, 20, 30, 40, 55]
print(values[0]+values[2])
values = (10, 20, 30, 40, 55)
print(values[0]+values[2])
values = "HELLO"
print(values[0]+values[2])
#シーケンスとはリスト，タプル，文字列などのように，複数の値を順序付けて格納するデータ構造の総称．シーケンスはインデックスを使って要素にアクセスできる．シーケンスはfor文で繰り返し処理ができる．
list_obj = [1,2,3]
var1, var2, var3 = list_obj #これをunpackingと呼ぶ．
print(var1, var2, var3)
var1 , var2, var3 = (1,2,3)
print(var1, var2, var3)
var1, var2, var3= "abc"
print(var1, var2)#このように変数の数と要素の数が一致しないときは，エラーになる．
ningyocho = 35.686321, 139.783757
ido, keido = ningyocho # このようにタプルをアンパックすることもできる．
print(f"人形町の緯度は{ido}，経度は{keido}です")
case = [100,125,110,135,93,95,93]
total = 0
for cases in case:
    total += cases
average = total / len(case)
print(f"合計感染者は{total}人、平均感染者は{average:.1f}人です")
def total_and_average(case_list):
    total = 0
    for cases in case_list:
        total += cases
    num = len(case_list)
    average = total/num
    return(total, f"{average:.1f}", num)
total_and_average([100,125,110,135,93,95,93])
total, average, num = total_and_average([100,125,110,135,93,95,93])
print(f"合計は{total}人,平均は{average}人,人数は{num}人です．")
