__author__ = 'rage'

from tkinter import Tk, Frame, BOTH, Menu, Message



class Example(Frame):

    global sortingAlgorithm

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.pack(fill=BOTH, expand=1)
        self.initUI()

    def initUI(self):

        self.parent.title("Sorting Algorithms")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        menubar.add_cascade(label="Choose Algo", menu=fileMenu)
        self.addAlgoNames(fileMenu)

        self.centerWindow()

    def centerWindow(self):

        w = 500
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def addAlgoNames(self, fileMenu):

        fileMenu.add_command(label="Selection Sort", command=self.onSelSort)
        fileMenu.add_command(label="Insertion Sort", command=self.onInsertSort)
        fileMenu.add_command(label="Bubble Sort", command=self.onBubbleSort)
        fileMenu.add_command(label="Quick Sort", command=self.onQuickSort)
        fileMenu.add_command(label="Merge Sort", command=self.onMergeSort)
        fileMenu.add_command(label="Counting Sort", command=self.onCountSort)
        fileMenu.add_command(label="Exit", command=self.onExit)

    def onSelSort(self):
        sortingAlgorithm = "Selection Sort"

    def onInsertSort(self):
        sortingAlgorithm = "Insertion Sort"

    def onBubbleSort(self):
        sortingAlgorithm = "Bubble Sort"

    def onQuickSort(self):
        sortingAlgorithm = "Quick Sort"

    def onMergeSort(self):
        sortingAlgorithm = "Merge Sort"

    def onCountSort(self):
        sortingAlgorithm = "Counting Sort"

    def onExit(self):
        self.quit()


def main():

    root = Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()