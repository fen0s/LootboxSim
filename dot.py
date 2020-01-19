from tkinter import *
from PIL import ImageTk, Image
import os
from pathlib import Path
from google_images_search import GoogleImagesSearch
import time
import random
from winsound import *
from gistfile1 import nouns
from prefstuff import *
balance = 100
spent = 0
balancestr = 'Balance: $%s' % balance
basepath = os.getcwd()
print(basepath)
root = Tk()
earned = 0
lboxcount = 0
itemsprice = 0
lbtext = 'Lootboxes opened: %s\n Money spent: $%s\nMoney earned: %s' % (lboxcount, spent, earned)
playeritems = {}
def lbplus(event):
    global btn2
    global lboxcount
    global lbtext
    global lbwindow
    global balance
    global balancestr
    global spent
    if btn2['state'] == NORMAL:
       btn2['state'] = DISABLED
       lboxcount += 1
       spent += 10
       lbtext = 'Lootboxes opened: %s\n Money spent: $%s\nMoney earned: $%s' % (lboxcount, spent, earned)
       balance -= 10
       balancestr = 'Balance: $%s' % balance
       lbl.configure(text=lbtext)
       balancelabel.configure(text=balancestr)
       root.update()
       lbwindow = Toplevel()
       lbwindow.geometry('200x100')
       lbwindtext = Label(lbwindow,
                       text = 'Opening lootbox... \nPlease wait...',
                       width=17, height=2,
                       font='arial 10')
       lbwindtext.place(relx=0.5, rely=0.5, anchor=CENTER)
       lbwindow.after(1300, lb_open)
    else:
        pass
def sell(event):
    global itemsprice
    global balance
    global balancestr
    global playeritems
    global earned
    balance += itemsprice
    earned += itemsprice
    lbtext = 'Lootboxes opened: %s\n Money spent: $%s\nMoney earned: $%s' % (lboxcount, spent, earned)
    lbl.configure(text=lbtext)
    itemsprice = 0
    playeritems = {}
    balancestr = 'Balance: $%s' % balance
    balancelabel.configure(text=balancestr)
    sold = Toplevel()
    sold.geometry('50x50')
    soldlabel = Label(sold,
                      text = 'Items sold!',
                      width = 10, height = 1,
                      font = 'arial 10')
    soldlabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)
def lb_open():
    global lbwindow
    btn2['state'] = NORMAL
    lootstr = ''
    lootwindow = Toplevel()
    lbwindow.destroy()
    lootwindow.geometry('600x400')
    lootlb = Label(lootwindow,
                   text='Congratulations! You got...',
                   width=20, height=3,
                   font='arial 14')
    lootlb.pack(side='top')
    tier = random.choice(qualities)
    for x in range(prefix_number.get(tier)):
        pref = random.choice(prefdict.get(tier))
        if pref in lootstr:
            pref1 = random.choice(prefdict.get(tier))
            lootstr += pref1 + ' '
        else:
           lootstr += pref + ' '
    lootstr += random.choice(nouns).title()
    loot = Label(lootwindow,
                 text=lootstr,
                 width=35, height=2,
                 fg = quality_colors.get(tier),
                 font='arial 19')
    qual = Label(lootwindow,
                 text=tier.upper() + ' Quality!',
                 fg=quality_colors.get(tier),
                 width=20, height=2,
                 font='arial 22')
    loot.place(rely=0.9, relx=0.5, anchor=CENTER)
    qual.place(rely=0.5, relx=0.5, anchor=CENTER)
    playeritems.update({str(tier).title() + ' ' + lootstr : str(random.randint(1, prices.get(tier)))})
    PlaySound('l.wav', SND_FILENAME)
def openinv(event):
    global itemsprice
    inv_window = Toplevel()
    inv_window.geometry('1000x500')
    invlabel = Label(inv_window,
                     text='YOUR ITEMS:',
                     width = 30, height = 2,
                     font='arial 22')
    invlabel.pack(side='top')
    itemlist = ''
    for y in playeritems.items():
        itemlist += 'Item: {0}, price: {1}$'.format(y[0], y[1]) + '\n'
    itemlistlabel = Label(inv_window,
                          text = itemlist,
                          width = 100, height = 40,
                          font = 'arial 14')
    itemlistlabel.pack(side='top')
    for z in playeritems.values():
        itemsprice += int(z)
    sellbutton = Button(inv_window,
                        text = 'Sell items for price of %s$?' % itemsprice,
                        width = 40, height = 1,
                        font='arial 15')
    sellbutton.place(relx = 0.5, rely = 0.95, anchor = CENTER)
    sellbutton.bind('<Button-1>', sell)


#Path for images
imgpath = Path(basepath + '/imgs/instagram-hex-colors-gradient-background.png')
imgif = Path(basepath + '/imgs/lbox.png')
img = ImageTk.PhotoImage(Image.open(imgpath))
lbgif = ImageTk.PhotoImage(Image.open(imgif).resize(size=(170, 150)))
panel = Label(root, image = img)
panel.place(relx=0.5, rely=0.5, anchor=CENTER)
root.geometry('600x400')
lbl = Label(root,
            text = lbtext,
            width=17, height=3,
            bg='#e07ef9',
            font='arial 10')
gif = Label(root, image = lbgif)
gif.place(relx=0.5, rely = 0.5, anchor = CENTER)
lbl.place(relx=0.89, rely = 0.07, anchor=CENTER)
btn2 = Button(root,
              text = 'Buy lootbox for $10',
              width=16, height=2,
              bg = "#bd7ad8", fg='#6900b6', font='arial 13')
btn2.place(relx=0.5, rely=0.9, anchor=S)
btn2.bind('<Button-1>', lbplus)
invbutton = Button(root,
                   text = 'Open inventory',
                   width=20, height = 1,
                   bg = "#e07ef9", fg='purple', font='arial 10')
invbutton.bind('<Button-1>', openinv)
invbutton.place(relx = 0.1, rely = 0.02, anchor = CENTER)
balancelabel = Label(root,
                     text = balancestr,
                     width = 20, height = 1,
                     bg = '#bd7ad8', fg='#59d327', font = 'arial 10')
balancelabel.place(relx = 0.1, rely = 0.97, anchor = CENTER)
root.mainloop()
