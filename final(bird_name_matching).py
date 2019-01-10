from psychopy import visual, core,event,gui
from sys import exit
import csv, random


#print subj info
exp_name='鳥類名稱配對測驗'
info = {'編號':'','姓名':'', '年齡':'', '性別':('男','女'), '賞鳥年齡':'','專業度自評':(1,2,3,4,5,6,7,8,9,10)}
infoDlg = gui.DlgFromDict(dictionary = info, title = exp_name, order = ['編號','姓名','性別','年齡','賞鳥年齡','專業度自評'])
if infoDlg.OK == False:
    core.quit()
    
#open new files to record
dataFile = open("%s.csv"%(info['編號']+'_'+info['姓名']), 'a')
dataFile.write(info['姓名']+','+info['年齡']+','+info['編號']+'\n')

win = visual.Window(size = (1000,600), color = (1,1,1), fullscr = False )
#實驗準備
text_1 = visual.TextStim(win, text = u'',
                               height = 40,
                               pos = (0.0,0.0),
                               color = 'black',
                               bold = True,
                               italic = False)
text_1.text = '歡迎參加本實驗,按任意鍵繼續'

Yresp = visual.TextStim(win, text = "是",color='blue', height=65,pos = (-400,-200))
Nresp = visual.TextStim(win, text = "否",color='red', height=65,pos = (400,-200))
timer = core.Clock()

text_1.draw()
win.flip()
core.wait(0)
timer.reset()           
k_1 = event.waitKeys()
timeUse = timer.getTime()       
print (k_1, timeUse)

for phase in range(2,3):

 if phase == 1:
  trials=100
  testfiles= "test.csv"
  text_1.text = '請判斷圖片與名稱是否相符,是按左鍵,否按右鍵'
  text_1.draw()
  win.flip()
  event.waitKeys()
 elif phase == 2:
  trials=10
  testfiles= "test_10.csv"
  text_1.text = '請判斷圖片與名稱是否相符,是按左鍵,否按右鍵'
  text_1.draw()
  win.flip()
  event.waitKeys()


 reader = csv.DictReader(open(testfiles, "r"))  
 tt=list(reader)
 random.shuffle(tt)
 dataFile.write('bird_pic, bird_name, pic_lable, name_lable, pressedKeys, accuracy, RT\n')
 for i in range(0,trials):
      trials=i+1
      print('trial = %d'%trials)
      print('*******************')
      print('phase = %d'%phase)
      print('*******************')
      print(tt[i]['bird_pic'])
      print('*******************')
      print(tt[i]['bird_name'])
      print('*******************')
      print(tt[i]['pic_lable'])
      print('*******************')
      print(tt[i]['name_lable'])
      print('-----------------')
      
      
      pic = visual.ImageStim(win, image=tt[i]['bird_pic'], pos = (0,75), size = (650,400))
      
      name = visual.TextStim(win,text=tt[i]['bird_name'],color='black', height=75, pos = (0,-200))
      win.flip()
      core.wait(0.3)
      pic.draw()
      name.draw()
      Yresp.draw()
      Nresp.draw()
      win.flip()
      timer.reset()
      keys=event.waitKeys(8.0,["left","right"])
      
      RT = []
      RT = timer.getTime()
      print(RT)
      
      accuracy=[0]
      if keys != None:
       for key in keys: 
        if (key == "left") and (tt[i]['pic_lable'])==(tt[i]['name_lable']): 
         accuracy=[1]
        elif (key == "right") and (tt[i]['pic_lable'])!=(tt[i]['name_lable']): 
         accuracy=[1]
        
       
      print(accuracy)
      
       
     
      
      
      dataFile.write(tt[i]['bird_pic']+', '+tt[i]['bird_name']+','+tt[i]['pic_lable']+','+tt[i]['name_lable']+','+str(keys)+','+str(accuracy)+','+str(RT)+'\n')

text_1.text = '實驗結束,按任意鍵關閉視窗'
text_1.draw()
win.flip()
event.waitKeys()
win.close()
core.quit()