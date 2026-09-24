import file_organizer as organizer
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class OrganizerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("650x450")

        # State: single source of truth
        self.target_dir: Path | None = None
        self.config: dict = organizer.load_config()
        self.path_label: tk.Label

        self._build_top_panel()

    def _build_top_panel(self):
        frame = tk.LabelFrame(self.root, text="Directory Selection")
        frame.pack(fill='x', padx=10, pady=5)
        tk.Button(frame, text="Browse", command=self.choose_directory).grid(column=0, row=0,padx=5, pady=10)
        self.path_label = tk.Label(frame, text="No Folder Selected")
        self.path_label.grid(column=0, row=1,padx=5, pady=10)
        self.organize_button = tk.Button(frame, text="Organize Files", command=self.organize_files)
        self.organize_button.grid(column=0, row=2,padx=5, pady=10)
        self.organize_button.config(state='disabled')


    def _build_editor_panel(self):
        pass

    def organize_files(self):
        if not issubclass(type(self.target_dir), Path):
            print("You have not selected a path.")
            messagebox.showerror(title="Can not sort", message="You have not selected a path. Please select a path first.")
        else:
            organizer.sort_files(str(self.target_dir.resolve()))

    def choose_directory(self):
        chosen_dir = filedialog.askdirectory()
        if chosen_dir:
            self.target_dir = Path(chosen_dir)
            if len(chosen_dir) > 65:
                self.path_label['text']=(f'{chosen_dir[0:21]} |...| {chosen_dir[-20:]}')
            else:
                self.path_label['text']=(chosen_dir)
            self.organize_button.config(state='normal')

if __name__ == "__main__":
    window = tk.Tk()
    app = OrganizerApp(window)
    window.mainloop()