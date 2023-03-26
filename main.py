import tkinter as tk
from tkinter import messagebox
import os
import random

def randomizer():
    randomp = random.randint(1,5)

    if randomp == 1:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(200, 200, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(430, 200, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(650, 200, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(900, 200, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(1100, 200, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(650, 400, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: [planetclick()])
        photocanvas.tag_bind(plan1, "<Enter>", lambda event: messagebox.showinfo("lore", story1))
        photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore", story2))
        photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore", story3))
        photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore", story4))
        photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore", story5))
    elif randomp == 2:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(1100, 200, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(900, 200, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(650, 200, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(430, 200, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(200, 200, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(650, 400, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: [planetclick()])
        photocanvas.tag_bind(plan1, "<Enter>", lambda event: messagebox.showinfo("lore", story1))
        photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore", story2))
        photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore", story3))
        photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore", story4))
        photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore", story5))
    elif randomp == 3:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(430, 200, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(650, 200, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(200, 200, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(1100, 200, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(900, 200, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(650, 400, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: [planetclick()])
        photocanvas.tag_bind(plan1, "<Enter>", lambda event: messagebox.showinfo("lore", story1))
        photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore", story2))
        photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore", story3))
        photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore", story4))
        photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore", story5))
    elif randomp == 4:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(1100, 200, image=p1re, anchor="center")
        plan2 = photocanvas.create_image(900, 200, image=p2re, anchor="center")
        plan3 = photocanvas.create_image(650, 200, image=p3re, anchor="center")
        plan4 = photocanvas.create_image(430, 200, image=p4re, anchor="center")
        plan5 = photocanvas.create_image(200, 200, image=p5re, anchor="center")
        newbutton = photocanvas.create_image(650, 400, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: [planetclick()])
        photocanvas.tag_bind(plan1, "<Enter>", lambda event: messagebox.showinfo("lore", story1))
        photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore", story2))
        photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore", story3))
        photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore", story4))
        photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore", story5))

    elif randomp == 5:
        photocanvas.create_image(0, 0, image=background, anchor="nw")
        plan1 = photocanvas.create_image(200, 200, image=p1re)
        plan2 = photocanvas.create_image(650, 200, image=p2re)
        plan3 = photocanvas.create_image(900, 200, image=p3re)
        plan4 = photocanvas.create_image(1100, 200, image=p4re)
        plan5 = photocanvas.create_image(430, 200, image=p5re)
        newbutton = photocanvas.create_image(650, 400, image=b1)
        photocanvas.tag_bind(newbutton, '<Button-1>', lambda event: [planetclick()])
        photocanvas.tag_bind(plan1, "<Enter>", lambda event: messagebox.showinfo("lore", story1))
        photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore", story2))
        photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore", story3))
        photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore", story4))
        photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore", story5))


story1 = ('''In a galaxy far, far away lies the planet Zorgon, a world unlike any other. 
                                 Zorgon is inhabited by a race of sentient cheese creatures called Cheesoids who evolved from a particularly delicious batch of gouda. 
                               The Cheesoids are a peaceful species, but they are also fiercely competitive when it comes to cheese-related matters. In their culture, cheese is everything.
                               Cheesoids are constantly inventing new types of cheese and holding cheese-tasting competitions to determine the best flavors."
                              "Despite their love of cheese, the Cheesoids are also known for their impressive technological advancements. 
                              They have developed cheese-powered spaceships and have even built entire cities made entirely out of different types of cheese."
                              'However, the Cheesoids' greatest invention was their "Cheeseball of Peace", a giant cheese ball that they launched into space as a symbol of their peaceful intentions. 
                              The Cheeseball of Peace is now a famous landmark in the galaxy, and many alien races visit Zorgon to marvel at the Cheesoids' love of cheese and their incredible inventions.''')
story2 = ('''In a distant galaxy, there exists a desolate planet named Nefaris, 
            once home to a thriving alien race. But Nefaris fell victim to a catastrophic event, 
            a massive asteroid impact that plunged the planet into darkness and triggered a chain reaction of destruction. 
            The asteroid impact caused the planet's delicate ecosystem to collapse, wiping out all forms of life. 
            The once vibrant forests were reduced to ash, the rivers ran dry, and the skies turned red with toxic fumes. 
            Now, the planet is nothing but a barren wasteland, a graveyard of a lost civilization. 
            The few remaining ruins offer glimpses of what once was, but they serve only as a reminder of the tragedy that befell Nefaris. 
            so, the planet remains silent, a tragic reminder of the fragility of life and the devastating consequences of a single cosmic event.''')
story3 = ('''Deep in the heart of the galaxy lies a planet unlike any other. 
            Known simply as Xandria, this celestial body is home to towering mountains, glittering oceans, and vast, 
            rolling plains that stretch as far as the eye can see. 
            But it is not just the planet's natural beauty that captivates those who gaze upon it. 
            Xandria is also home to a thriving civilization of beings unlike any seen before. 
            They possess advanced technology, a deep understanding of the universe, and a peaceful way of life that belies their formidable power. 
            Visitors to Xandria often speak of feeling a sense of peace and wonder that is hard to describe, as if the very air is infused with magic. 
            And indeed, there are whispers that Xandria holds secrets beyond the imagination of any mortal mind, secrets that could change the very course of the galaxy itself.''')
story4 = ('''In a faraway galaxy lies a planet called Zephyrion, where the sky is a vibrant shade of purple and the winds howl with such ferocity that it's said they can knock a grown man off his feet. 
            The planet is home to a species of sentient beings known as Zephyrites, who have evolved to withstand the extreme 
            weather conditions and harness the power of the winds for their own use. 
            They live in towering cities that hover in the sky, held aloft by advanced anti-gravity technology. 
            Zephyrites are a peaceful species, but they fiercely defend their planet from outside threats, 
            and their warriors are feared for their skill with the sword and mastery of the winds. 
            Despite their isolation, the Zephyrites are a thriving civilization, with a rich culture of music, art, and literature that celebrates the beauty and power of the winds that shape their world.''')
story5 = ('''Deep in the reaches of space, there is a planet known only as Xalaxia. 
            It is a place of dread and horror, shrouded in an eternal night where the stars themselves seem to flee from the darkness. 
            Few who have ventured there have returned, and those that have come back are forever changed, haunted by the terrors they witnessed. 
            It is said that the planet is cursed by an ancient evil, a malevolent force that lurks in the shadows and feeds on the fears of those foolish enough to visit. 
            The skies are filled with strange, writhing shapes that seem to pulse with a sinister energy, while the ground itself is littered with the bones of creatures long dead. 
            In the heart of Xalaxia, there is a great temple, said to be the source of the planet's curse. Those who have dared to enter never return, and it is whispered that the temple holds the key to unspeakable power, a power that could drive a person mad with its sheer horror. 
            Beware, traveler, for Xalaxia is a planet of nightmares, and those who dare to set foot there do so at their own peril.''')



def planetclick():
    randomizer()
    photocanvas.tag_bind(plan1,"<Enter>",lambda event: messagebox.showinfo("lore",story1))
    photocanvas.tag_bind(plan2, "<Enter>", lambda event: messagebox.showinfo("lore",story2))
    photocanvas.tag_bind(plan3, "<Enter>", lambda event: messagebox.showinfo("lore",story3))
    photocanvas.tag_bind(plan4, "<Enter>", lambda event: messagebox.showinfo("lore",story4))
    photocanvas.tag_bind(plan5, "<Enter>", lambda event: messagebox.showinfo("lore",story5))

root = tk.Tk()

root.geometry("1400x1400")
root.title("My Little Solar System")
root.configure(bg="black")

label = tk.Label(root,text="Welcome to the Solar System!", font=('Tw Cen MT', 18),fg="Purple",bg="Black")
label.pack(padx=5,pady=5)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

photocanvas = tk.Canvas(root,width=1400,height =1000)
photocanvas.pack(expand='YES',fill='both')

bgdirectory = os.path.dirname(__file__)
#File paths for each planet png
bgpath = "SolarSystemResources\solarsystemgif.gif"
planet1 = "SolarSystemResources\Planet_1.png"
planet2 = "SolarSystemResources\Planet_2.png"
planet3 = "SolarSystemResources\Planet_3.png"
planet4 = "SolarSystemResources\Planet_4.png"
planet5 = "SolarSystemResources\Planet_5.png"
button = "SolarSystemResources\Button.png"
button_clicked = "SolarSystemResources\Button2.png"

bg_file_path = os.path.join(bgdirectory,bgpath)
p1fp = os.path.join(bgdirectory,planet1)
p2fp = os.path.join(bgdirectory,planet2)
p3fp = os.path.join(bgdirectory,planet3)
p4fp = os.path.join(bgdirectory,planet4)
p5fp = os.path.join(bgdirectory,planet5)
button1 = os.path.join(bgdirectory,button)
button2= os.path.join(bgdirectory,button_clicked)

background = tk.PhotoImage(file = bg_file_path)
p1 = tk.PhotoImage(file=p1fp)
p2 = tk.PhotoImage(file=p2fp)
p3 = tk.PhotoImage(file=p3fp)
p4 = tk.PhotoImage(file=p4fp)
p5 = tk.PhotoImage(file=p5fp)
b1 = tk.PhotoImage(file=button1)
b2 = tk.PhotoImage(file=button2)

background = background.zoom(5)
p1re = p1.zoom(5)
p2re = p2.zoom(5)
p3re = p3.zoom(5)
p4re = p4.zoom(5)
p5re = p5.zoom(5)
b1 = b1.zoom(1)
b2 = b2.zoom(1)

photocanvas.create_image(0, 0, image=background, anchor="nw")
newbutton = photocanvas.create_image(650,400,image=b1)
photocanvas.tag_bind(newbutton,'<Button-1>',lambda event: planetclick())

plan1 = photocanvas.create_image(650, 200, image=p1re)
plan2 = photocanvas.create_image(200, 200, image=p2re)
plan3 = photocanvas.create_image(430, 200, image=p3re)
plan4 = photocanvas.create_image(900, 200, image=p4re)
plan5 = photocanvas.create_image(1100, 200, image=p5re)

photocanvas.tag_bind(plan1, '<Enter>', lambda event: planetclick())
photocanvas.tag_bind(plan2, '<Enter>', lambda event: planetclick())
photocanvas.tag_bind(plan3, '<Enter>', lambda event: planetclick())
photocanvas.tag_bind(plan4, '<Enter>', lambda event: planetclick())
photocanvas.tag_bind(plan5, '<Enter>', lambda event: planetclick())




root.mainloop()