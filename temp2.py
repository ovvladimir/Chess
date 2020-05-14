import sys
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
text = tk.Text(root, tabs=(200,))
vsb = tk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(side="left", fill="both", expand=True)

pieces = u"\u2654\u2655\u2656\u2657\u2658\u2659\u265A\u265B\u265C\u265D\u265E\u265F\n"
for count, family in enumerate(sorted(tkFont.families())):
    font = tkFont.Font(family=family, size=18)
    tag = "font-%s" % count
    text.tag_configure((tag,), font=font)
    text.insert("end", family)
    text.insert("end", "\t" + pieces, tag)

root.mainloop()
