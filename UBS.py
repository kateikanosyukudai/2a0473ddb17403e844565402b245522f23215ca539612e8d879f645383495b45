# **********************
# m23270_task013.py
#　内容：
#　入力：縦と横の数
#　出力：
# **********************

print('Please input only Odd number')
yoko=int(input('Input横(3-9) | '))
tate=int(input('Input縦(3-9) | '))
wa=yoko+tate

if not(wa%2==0 and wa>=6):
    print('Bad input only Odd number')
else:
    for j in range(tate):
        for i in range(yoko):
            if (i==(yoko-1)/2 and j==(tate-1)/2):
                print('0',end=' ')
            else:
                print('*',end=' ')
        print()
