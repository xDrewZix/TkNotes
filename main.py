from tkinter import *
from tkinter import ttk



class Notebook():
	
	def __init__(self, name):
		
		self.notes = {}
		self.name=name
		
	
	def addNote(self, note, id):
		
		
		self.notes[id] = note		
	
	def getnotes(self):
		
		return self.notes
		
		
	
class Library():

	def __init__(self):

		self.__library = []

	def addToLibrary(self, notebook):

		self.__library.append(notebook)
	
	def getLibraryID(self):

		return len(self.__library)
	
	def retrieveNoteBook(self, id):

		return self.__library[id]






def noteBookDetails():

	instruction = Label(root, text="please to enter a notebook name")
	instruction.grid(row=2, column=3)
	e = Entry(root)
	e.grid(row=3, column=3)
	addButton = Button(root, text="press to add", command=lambda: self.createNoteBook(e.get()))
	addButton.grid(row=5, column=5)
	
	
def createNoteBook(name):
	if name == '':
		createlibraryframe.grid_forget()
	else:	
		oNotebook = Notebook(name)
		library.addToLibrary(oNotebook)
		e.delete(0, 'end')
		createlibraryframe.grid_forget()
		id=library.getLibraryID()
		value = oNotebook.notes
		value =len(value)
		my_List.insert(parent='', index='end', iid=id, text=f"{oNotebook.name}", values=(value))


	

def addnotes(notebook, entry, selection):
	if selection in notebook.notes.keys():
		notebook.notes[selection] = entry
	else:
		subid = str(len(notebook.notes))
		id = selection+'.'+subid
		notebook.addNote(entry, id)
		my_List.insert(parent=selection, index='end', iid=id, text=f"{entry[:10]}", values=(0))
	
	
	
def getnotes(name):
	notes = name.getnotes
	for i in name.notes.values():
		print(i)
		
def getselection(entry):
	selection = my_List.selection()[0]
	parent_id = my_List.parent(selection)

	if parent_id == '':
		id = int(selection) - 1
		notebook = library.retrieveNoteBook(id)
		addnotes(notebook, entry, selection)
	else:
		parent_id = int(parent_id) - 1
		notebook = library.retrieveNoteBook(parent_id)
		addnotes(notebook, entry, selection)
		
	
def insertText():
	selecteditem = my_List.selection()[0]
	parent_id = my_List.parent(selecteditem)
	if parent_id == '':
		pass
	else:
		parent_id = int(parent_id)
		id = parent_id - 1
		notebook = library.retrieveNoteBook(id)
		text = notebook.notes[selecteditem]
		notewindow.delete('1.0', 'end')
		notewindow.insert('end', text)
	
	



	
	



	
	
	



	
	
root = Tk()

#add tree to sidebar.

library = Library()

my_List = ttk.Treeview(root)
my_List['column'] = ("entries")

my_List.column("#0", width=150, minwidth=25)
my_List.column("entries" , anchor=W, width=150)

my_List.heading("#0", text="Notebook", anchor=W)
my_List.heading("entries", text="Number of entries", anchor=W)

my_List.grid(row=1, column=0)

# add note window

notewindow = Text(root)
saveNotesButton = Button(text='save', command = lambda: getselection(notewindow.get('1.0', 'end')))
saveNotesButton.grid(row=0, column=2) 

notewindow.grid(row=1, column = 2)
my_List.bind('<<TreeviewSelect>>', lambda event: insertText())






#add functions to sidebar


sideframe = Frame(root)
sideframe.grid(row=0, column=0)

createNoteBookButton = Button(sideframe, text="click me to create a new notebook", command=lambda:  createlibraryframe.grid(row=0, column=1), anchor=E, height=2, width=4)

createNoteBookButton.grid(row=2, column=0)




#  creates a new frame for entering notebook details and creating it.

createlibraryframe = Frame(root)


e = Entry(createlibraryframe)
instruction = Label(createlibraryframe, text="please enter a notebook name")
addButton = Button(createlibraryframe, text="press to add", command=lambda: createNoteBook(e.get()))


e.grid(row=1, column=2)
addButton.grid(row=2, column=2)
instruction.grid(row=0, column=2)









root.mainloop()
