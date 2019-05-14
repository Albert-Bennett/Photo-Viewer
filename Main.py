try:
    import Tkinter
except:
    import tkinter as Tkinter
    
import ImageHandle
import Settings

from RepeatingTimer import RepeatingTimer

class PictureWindow(Tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        Tkinter.Canvas.__init__(self, *args, **kwargs)
        self.CurrentIndex = 0
        self.imagelist = Settings.CurrentTheme["ImageFilepaths"]
        self.imagelist_p=[]
        
        self.t = RepeatingTimer(Settings.CurrentTheme["ChangeTime"], self.next_image)
        self.t.start()
        
        self.next_image()
        
        self.all_function_trigger()
        
    def show_image(self, path):
        img = ImageHandle.tk_image(path, self.winfo_screenwidth(), self.winfo_screenheight())
        self.delete(self.find_withtag("bacl"))
        self.allready = self.create_image(self.winfo_screenwidth()/2, self.winfo_screenheight()/2, image=img, anchor='center', tag="bacl")
        
        self.image = img
        self.master.title("Photo Viewer ({})".format(self.CurrentIndex))
        return

    def next_image(self):
        try:
            currentImg = self.imagelist[self.CurrentIndex]
            
            self.show_image(currentImg)      
            self.CurrentIndex +=1
            
            if self.CurrentIndex >= len(self.imagelist):
                self.CurrentIndex = 0
        except EOFError as e:
            pass
        return
    
    def all_function_trigger(self):
        self.window_settings()
        return
    
    def window_settings(self):
        self['width'] = self.winfo_screenwidth()
        self['height'] = self.winfo_screenheight()
        return
    

def main():
    root = Tkinter.Tk(className=" Photo Viewer")
    PictureWindow(root).pack(expand="yes", fill="both")
    root.resizable(width=0, height=0)
    root.mainloop()
    return

if __name__ == '__main__':
    main()