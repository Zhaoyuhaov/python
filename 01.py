# 时间 2022/11/28 7:53
import  pyautogui  as pg
import  time
print('请把鼠标置于赞上')
time.sleep(3)
a=pg.position()
print('坐标:',a)
x=int(input('请输入x:'))
y=int(input('请输入y:'))
c=int(input('请输入点赞次数:'))
t=float(input('请输入点赞时间（秒）间隔:'))
pg.PAUSE=t
for i in range(0,c):
    pg.click(x,y)
    if pg.position()!=a:
        break




