from tkinter import *
from tkinter import messagebox

"""This is the opening screen for the program,
where the user will input their name and begin"""
window = Tk()
window.title("Delphi Sports Interest Form")
window.geometry("300x200+150+150")
window.configure(bg = "#E3CF9C")
window.rowconfigure(0, weight = 0)
window.rowconfigure(1, weight = 0)
window.rowconfigure(2, weight = 1)
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)

# This code is for the title of the first screen.
openingTitle = Label(window,
                     text = "Delphi Sports Interest Form",
                     font = ("Helvetica", 10),
                     bg = "#E3CF9C"
                     )
openingTitle.grid(row = 0, column = 0, columnspan = 2)
# This code is for the label for the name of the user
nameLabel = Label(window,
                  text = "Name:",
                  bg = "#E3CF9C")
nameLabel.grid(row = 1, column = 0)
# This code is for the entry field for the name of the user
nameInput = Entry(window)
nameInput.grid(row = 1, column = 1)

imgLogo = PhotoImage(file = "d_Logo_Resized.gif")
logoLabel = Label(image = imgLogo, text = "Delphi O")
logoLabel.grid(row = 2, column = 0)
logoLabel.image = imgLogo

imgMascot = PhotoImage(file = "Mascot_Oracle_Resized.gif")
mascotLabel = Label(image = imgMascot, text = "Oracle Mascot Picture")
mascotLabel.grid(row = 2, column = 1)
mascotLabel.image = imgLogo


"""This code is for the button to advance the screen
This function sets up the fall sports screen,
and includes the button to advance to winter and spring sport screens"""
def advanceToFall():
    if nameInput.get() == "":
        messagebox.showerror("Invalid Name", "Please enter a name")
    else:
        # This code sets up the second window, the one for fall sports
        fallSports = Tk()
        fallSports.title("Fall Sports Interest")
        fallSports.geometry("300x200+150+150")
        fallSports.configure(bg = "#E3CF9C")
        #This code is for the fallSports screen title
        fallTitle = Label(fallSports,
                          text = "Mark the fall sports you have interest in",
                          font = ("Helvetica", 10),
                          bg = "#E3CF9C")
        fallTitle.grid(row = 0, column = 0, columnspan = 2)

        """The following code is for each of the fall sport buttons"""
        # Football Button
        footballButton = Checkbutton(fallSports,
                                     text = "Football  ",
                                     height = 2,
                                     width = 10,
                                     bg = "#E3CF9C")
        footballButton.grid(row = 1, column = 0, sticky = "NWS")
        # Volleyball button
        volleyballButton = Checkbutton(fallSports,
                                       text = "Volleyball",
                                       height = 2,
                                       width = 13,
                                       bg = "#E3CF9C")
        volleyballButton.grid(row = 1, column = 1, sticky = "NWS")
        # Soccer Button
        soccerButton = Checkbutton(fallSports,
                                   text = "Soccer    ",
                                   height = 2,
                                   width = 10,
                                   bg = "#E3CF9C")
        soccerButton.grid(row = 2, column = 0, sticky = "NWS")
        # Boys Tennis Button
        boysTennisButton = Checkbutton(fallSports,
                                       text = "Boys Tennis",
                                       height = 2,
                                       width = 13,
                                       bg = "#E3CF9C")
        boysTennisButton.grid(row = 2, column = 1, sticky = "NEWS")
        # Girls Golf Button
        girlsGolfButton = Checkbutton(fallSports,
                                      text = "Girls Golf",
                                      height = 2,
                                      width = 10,
                                      bg = "#E3CF9C")
        girlsGolfButton.grid(row = 3, column = 0, sticky = "NWS")
        # Cross Country Button
        xcountryButton = Checkbutton(fallSports,
                                     text = "Cross Country",
                                     height = 2,
                                     width = 13,
                                     bg = "#E3CF9C")
        xcountryButton.grid(row = 3, column = 1, sticky = "NES")
        
        """ This code is for when the "None" button is clicked
        This function clears all other fall sport selections"""
        def fallNoneClicked():
            footballButton.deselect()
            volleyballButton.deselect()
            soccerButton.deselect()
            boysTennisButton.deselect()
            girlsGolfButton.deselect()
            xcountryButton.deselect()
        # Sets up None button
        fallNoneButton = Checkbutton(fallSports,
                                     text = "None     ",
                                     height = 2,
                                     width = 10,
                                     bg = "#E3CF9C",
                                     command = fallNoneClicked)
        fallNoneButton.grid(row = 4, column = 0, sticky = "NWS")

        """This function sets up the winter sports screen
        and includes the button for advancing to the spring sports screen"""
        def advanceToWinter():
            winterSports = Tk()
            winterSports.title("Winter Sports Interest")
            winterSports.geometry("300x200+150+150")
            winterSports.configure(bg = "#E3CF9C")
            # Below is code for setting up the winter sports title label
            winterTitle = Label(winterSports,
                                text = "Mark the winter sports you have interest in",
                                font = ("Helvetica", 10),
                                bg = "#E3CF9C")
            winterTitle.grid(row = 0, column = 0, columnspan = 2)

            """The following code is for each of the winter sport buttons"""
            # Boys Basketball Button
            boysBasketballButton = Checkbutton(winterSports,
                                               text = "Boys Basketball",
                                               height = 2,
                                               width = 10,
                                               bg = "#E3CF9C")
            boysBasketballButton.grid(row = 1, column = 0, sticky = "NEWS")
            # Girls Basketball Button
            girlsBasketballButton = Checkbutton(winterSports,
                                                text = "Girls Basketball",
                                                height = 2,
                                                width = 10,
                                                bg = "#E3CF9C")
            girlsBasketballButton.grid(row = 1, column = 1,sticky = "NES")
            # Swim Button
            swimButton = Checkbutton(winterSports,
                                     text = "Swim       ",
                                     height = 2,
                                     width = 10,
                                     bg = "#E3CF9C")
            swimButton.grid(row = 2, column = 0, sticky = "NWS")
            # Wrestling Button
            wrestlingButton = Checkbutton(winterSports,
                                          text = "Wrestling        ",
                                          height = 2,
                                          width = 10,
                                          bg = "#E3CF9C")
            wrestlingButton.grid(row = 2, column = 1, sticky = "NES")
            """ This code is for when the "None" button is clicked
            This function clears all other winter sport selections"""
            def winterNoneClicked():
                boysBasketballButton.deselect()
                girlsBasketballButton.deselect()
                swimButton.deselect()
                wrestlingButton.deselect()
            # Sets up None button
            winterNoneButton = Checkbutton(winterSports,
                                           text = "None       ",
                                           height = 2,
                                           width = 10,
                                           bg = "#E3CF9C",
                                           command = winterNoneClicked)
            winterNoneButton.grid(row = 3, column = 0, sticky = "NWS")
            
            """This function sets up the spring sports screen
            It includes the function for closing the program once users are done"""
            def advanceToSpring():
                springSports = Tk()
                springSports.title("Spring Sports Interest")
                springSports.geometry("300x200+150+150")
                springSports.configure(bg = "#E3CF9C")
                # Below is code for setting up the spring sports title label
                springTitle = Label(springSports,
                                    text = "Mark the spring sports you have interest in",
                                    font = ("Helvetica", 10),
                                    bg = "#E3CF9C")
                springTitle.grid(row = 0, column = 0, columnspan = 2)

                """The following code is for each of the fall sport buttons"""
                # Track and Field Button
                trackButton = Checkbutton(springSports,
                                          text = "Track and Field",
                                          height = 2,
                                          width = 10,
                                          bg = "#E3CF9C")
                trackButton.grid(row = 1, column = 0, sticky = "NEWS")
                # Boys Golf Button
                boysGolfButton = Checkbutton(springSports,
                                             text = "Boys Golf",
                                             height = 2,
                                             width = 10,
                                             bg = "#E3CF9C")
                boysGolfButton.grid(row = 1, column = 1, sticky = "NEWS")
                # Girls Tennis Button
                girlsTennisButton = Checkbutton(springSports,
                                                text = "Girls Tennis     ",
                                                height = 2,
                                                width = 10,
                                                bg = "#E3CF9C")
                girlsTennisButton.grid(row = 2, column = 0, sticky = "NEWS")
                # Baseball Button
                baseballButton = Checkbutton(springSports,
                                             text = "Baseball",
                                             height = 2,
                                             width = 13,
                                               bg = "#E3CF9C")
                baseballButton.grid(row = 2, column = 1, sticky = "NWS")
                # Softball Button
                softballButton = Checkbutton(springSports,
                                             text = "Softball         ",
                                             height = 2,
                                             width = 13,
                                               bg = "#E3CF9C")
                softballButton.grid(row = 3, column = 0, sticky = "NWS")
                
                """ This code is for when the "None" button is clicked
                This function clears all other spring sport selections"""
                def springNoneClicked():
                    trackButton.deselect()
                    boysGolfButton.deselect()
                    girlsTennisButton.deselect()
                    baseballButton.deselect()
                    softballButton.deselect()
                # Sets up the None button
                springNoneButton = Checkbutton(springSports,
                                               text = "None     ",
                                               height = 2,
                                               width = 10,
                                               bg = "#E3CF9C",
                                               command = springNoneClicked)
                springNoneButton.grid(row = 3, column = 1, sticky = "NEWS")
                # This function closes the program when the "Finish" button is clicked
                def endProgram():
                    springSports.destroy()
                # Sets up the finish button
                finishButton = Button(springSports,
                                      text = "Finish",
                                      command = endProgram,
                                      bg = "#FAE4AC")
                finishButton.grid(row = 4, column = 0, columnspan = 2)
                # Closes winter sports screen once the next screen has been opened
                winterSports.destroy()
            # Sets up the button to advance to spring
            nextButton3 = Button(winterSports,
                                 text = "Next",
                                 command = advanceToSpring,
                                 bg = "#FAE4AC")
            nextButton3.grid(row = 3, column = 1)
            # Closes fall sports screen once the next screen has been opened
            fallSports.destroy()
        # Sets up the button to advance to winter
        nextButton2 = Button(fallSports,
                             text = "Next",
                             command = advanceToWinter,
                             bg = "#FAE4AC")
        nextButton2.grid(row = 4, column = 1)
        # Closes name input screen once the next screen has been opened
        window.destroy()
# Sets up the button to advance to fall
nextButton = Button(window, text = "Next",
                    command = advanceToFall,
                    bg = "#FAE4AC")
nextButton.grid(row = 2, column = 0, columnspan = 2)



def main():
    """Sets up window and its features"""
    window.mainloop()

if __name__ == "__main__":
    main()
