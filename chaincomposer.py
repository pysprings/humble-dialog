import Tkinter as tk


class ReverbFilter:
    def __repr__(self):
        raise Exception

    def __str__(self):
        raise Exception


class ChainComposer:
    def __init__(self, view):
        self.view = view
        self.filters = (ReverbFilter,)
        self.chain = ()

    def initialize(self):
        self.view.set_selection(self.filters)

    def add(self, index):
        self.chain = self.chain + (self.filters[index],)
        self.view.set_chain(self.chain)


class ChainComposerDialog:
    def __init__(self, master):
        root = tk.Frame(master)
        root.pack()

        self.chaincomposer = ChainComposer(self)

        filter_frame = tk.Frame(master)
        filter_frame.pack(side=tk.LEFT)

        filter_label = tk.Label(filter_frame, text="Available Filters:")
        filter_label.pack(side=tk.TOP)

        self.filters = tk.Listbox(filter_frame)
        self.filters.pack(side=tk.TOP, pady=15)

        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.LEFT)

        self.add_button = tk.Button(button_frame, text="add", command=self.add)
        self.add_button.pack(side=tk.TOP)


        chain_frame = tk.Frame(master)
        chain_frame.pack(side=tk.LEFT)

        chain_label = tk.Label(chain_frame, text="Chain:")
        chain_label.pack(side=tk.TOP)

        self.chain = tk.Listbox(chain_frame)
        self.chain.pack(side=tk.TOP, pady=15)

        self.chaincomposer.initialize()

    def set_chain(self, chain):
        self.chain.delete(0, tk.END)
        for c in chain:
            self.chain.insert(tk.END, c)

    def set_selection(self, selection):
        self.filters.delete(0, tk.END)
        for s in selection:
            self.filters.insert(tk.END, s)

    def add(self):
        for selection in self.filters.curselection():
            self.chaincomposer.add(selection)


if __name__ == '__main__':
    root = tk.Tk()
    app = ChainComposerDialog(root)
    root.mainloop()
