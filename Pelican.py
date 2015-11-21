#!/usr/bin/env python
#-*- coding: utf-8 -*-

'a test module'

__author__ = "李金标"

from html.parser import HTMLParser
parser = HTMLParser()

from tkinter import *
print("tk.TkVersion",TkVersion)
#import tkMessageBox

root = Tk()
root.configure(background='#EFEFEF',pady=15)

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(background='#EFEFEF')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        htmlFame = LabelFrame(self, text="HTML中的Unicode编码", bg = "#EFEFEF")
        htmlFame.pack(fill="both", expand="yes")
        self.htmlText = Text(htmlFame,highlightcolor='#4D90FE',highlightthickness=1,width=60,height=5,padx=5,pady=5,highlightbackground='#EEEEEE')
        self.htmlText.bind("<KeyRelease>", self.OnKeyPressHtml)
        self.htmlText.grid(row=0, column=0, padx=5, pady=5)

        cssFame = LabelFrame(self, text="CSS中的Unicode编码", bg = "#EFEFEF")
        cssFame.pack(fill="both", expand="yes")
        self.cssText = Text(cssFame,highlightcolor='#4D90FE',highlightthickness=1,width=60,height=5,padx=5,pady=5,highlightbackground='#EEEEEE')
        self.cssText.bind("<KeyRelease>", self.OnKeyPressCss)
        self.cssText.grid(row=0, column=0, padx=5, pady=5)

        javaScriptFame = LabelFrame(self, text="JavaScript中的Unicode编码", bg = "#EFEFEF")
        javaScriptFame.pack(fill="both", expand="yes")
        self.javaScriptText = Text(javaScriptFame,highlightcolor='#4D90FE',highlightthickness=1,width=60,height=5,padx=5,pady=5,highlightbackground='#EEEEEE')
        self.javaScriptText.bind("<KeyRelease>", self.OnKeyPressJavaScript)
        self.javaScriptText.grid(row=0, column=0, padx=5, pady=5)

        
        sourceFame = LabelFrame(self, text="原始文本", bg = "#EFEFEF")
        sourceFame.pack(fill="both", expand="yes")
        self.sourceText = Text(sourceFame,highlightcolor='#4D90FE',highlightthickness=1,width=60,height=5,padx=5,pady=5,highlightbackground='#EEEEEE')
        self.sourceText.bind("<KeyRelease>", self.OnKeyPressSource)
        self.sourceText.grid(row=0, column=0, padx=5, pady=5)
        
        # self.alertButton = Button(self, text='Hello', command=self.hello)
        # self.alertButton.pack()
    def OnKeyPressHtml(self,event):

        originalValue = self.htmlText.get('0.0',END)
        value = list(parser.unescape(originalValue))
        print(value)
        #javaScript
        self.javaScriptText.delete('0.0', END)
        def dealJavaScriptText(x):
            return '\\u'+('000'+hex(ord(x))[2:])[-4:] 
        mapJavaScriptValue = map(dealJavaScriptText,value)
        resultJavaScriptValue = "".join(list(mapJavaScriptValue)[:-1])
        self.javaScriptText.insert('0.0', resultJavaScriptValue)

        #Source
        self.sourceText.delete('0.0', END)
        self.sourceText.insert('0.0', parser.unescape(originalValue))

        #css
        self.cssText.delete('0.0', END)
        def dealCssText(x):
            return '\\'+('000'+hex(ord(x))[2:])[-4:]
        mapCssValue = map(dealCssText,value)
        resultCssValue = "".join(list(mapCssValue)[:-1])
        self.cssText.insert('0.0', resultCssValue)
    def OnKeyPressCss(self,event):

        originalValue = (self.cssText.get('0.0',END))[1:-1]

        self.javaScriptText.delete('0.0', END)
        self.htmlText.delete('0.0', END)
        self.sourceText.delete('0.0', END)
        if (len(originalValue)>0): 
            print(originalValue)
            #print(originalValue.split('\\'))
            value = originalValue.split('\\')
            #print(value)

            #javaScript
            
            def dealJavaScriptText(x):
                if len(x) < 4:
                    return
                return '\\u'+x 
            mapJavaScriptValue = map(dealJavaScriptText,value)
            resultJavaScriptValue = "".join(list(mapJavaScriptValue))
            self.javaScriptText.insert('0.0', resultJavaScriptValue)

            #html
            
            def dealHtmlText(x):
                if len(x) < 4:
                    return
                return '&#'+str(int(x,16))+';'
            mapHtmlValue = map(dealHtmlText,value)
            resultHtmlValue = "".join(list(mapHtmlValue))
            self.htmlText.insert('0.0', resultHtmlValue)

            #Source
            
            def dealSourceText(x):
                if len(x) < 4:
                    return
                return chr(int(x,16))
            mapSourceValue = map(dealSourceText,value)
            resultSourceValue = "".join(list(mapSourceValue))
            self.sourceText.insert('0.0', resultSourceValue)
    def OnKeyPressJavaScript(self,event):

        originalValue = self.javaScriptText.get('0.0',END)[2:-1]
        self.htmlText.delete('0.0', END)
        self.cssText.delete('0.0', END)
        self.sourceText.delete('0.0', END)
        if len(originalValue)>0:

            value = originalValue.split('\\u')
            #css 
            def dealCssText(x):
                if len(x) < 4:
                    return
                return '\\'+x 
            mapCssValue = map(dealCssText,value)
            resultCssValue = "".join(list(mapCssValue))
            self.cssText.insert('0.0', resultCssValue)

            #html 
            def dealHtmlText(x):
                if len(x) < 4:
                    return
                return '&#'+str(int(x,16))+';'
            mapHtmlValue = map(dealHtmlText,value)
            resultHtmlValue = "".join(list(mapHtmlValue))
            self.htmlText.insert('0.0', resultHtmlValue)

            #Source
            def dealSourceText(x):
                if len(x) < 4:
                    return
                return chr(int(x,16))
            mapSourceValue = map(dealSourceText,value)
            resultSourceValue = "".join(list(mapSourceValue))
            self.sourceText.insert('0.0', resultSourceValue)
    def OnKeyPressSource(self,event):

        value = self.sourceText.get('0.0',END)
        value = list(value)

        #javaScript
        self.javaScriptText.delete('0.0', END)
        def dealJavaScriptText(x):
            return '\\u'+('000'+hex(ord(x))[2:])[-4:] 
        mapJavaScriptValue = map(dealJavaScriptText,value)
        resultJavaScriptValue = "".join(list(mapJavaScriptValue)[:-1])
        self.javaScriptText.insert('0.0', resultJavaScriptValue)

        #html
        self.htmlText.delete('0.0', END)
        def dealHtmlText(x):
            return '&#'+str(ord(x))+';'
        mapHtmlValue = map(dealHtmlText,value)
        resultHtmlValue = "".join(list(mapHtmlValue)[:-1])
        self.htmlText.insert('0.0', resultHtmlValue)

        #css
        self.cssText.delete('0.0', END)
        def dealCssText(x):
            return '\\'+('000'+hex(ord(x))[2:])[-4:]
        mapCssValue = map(dealCssText,value)
        resultCssValue = "".join(list(mapCssValue)[:-1])
        self.cssText.insert('0.0', resultCssValue)


    # def hello(self):
    #     html = self.htmlText.get('0.0', END) or 'world'
    #     tkMessageBox.showinfo('Message', 'Hello, %s' % html)

app = Application()
# 设置窗口标题:
app.master.title('Unicode编码转换器')
app.master.geometry('480x500')
# 主消息循环:
app.mainloop()