###
import pandas as pd
import tkinter as tk

### Datei Excel einlesen
df = pd.read_excel("./Preisliste 2.xlsx")

### Importieren der Preise
 
# Import Unterhaltungspreise
DJ = df.iloc[9,2]
Barkeeper = df.iloc[10,2]

# Import Einladungspreise
Postkarteppp = df.iloc[12,1]
Postkarte = df.iloc[12,2]
Email = df.iloc[12,2]

### Ausgabe der Auswahlen/Eingaben

# Unterhaltung Dropdown Ausgabe 
def on_unterhaltung_select(*args):
    selected = unterhaltung_selected_option.get()
    if selected == "DJ":
        unterhaltung_preis_label.config(text=f"Preis für DJ: {DJ} €")
    elif selected == "Barkeeper + Bar":
        unterhaltung_preis_label.config(text=f"Preis für Barkeeper + Bar: {Barkeeper} €")
    else:
        unterhaltung_preis_label.config(text="")
        

# Einladungen Dropdown Ausgabe 
def on_einladung_select(*args):
    selected = selected_einladung_option.get()
    if selected == "Ja, ich möchte eine Online Einladung als Email bestellen":
        einladung_preis_label.config(text=f"Preis für eine Email Einladung: {Email} €")
        einladung_anzahl_label.pack_forget()
        einladung_anzahl_entry.pack_forget()
        einladung_gesamtpreis_label.config(text="")
    elif selected == "Ja, ich möchte Einladungen in gedruckter Form als Postkarte bestellen":
        einladung_preis_label.config(text=f"Preis pro Person: {Postkarteppp} €, Grundpreis: {Postkarte} €")
        einladung_anzahl_label.pack()
        einladung_anzahl_entry.pack()
    else:
        einladung_preis_label.config(text="")
        einladung_anzahl_label.pack_forget()
        einladung_anzahl_entry.pack_forget()
        einladung_gesamtpreis_label.config(text="")


def berechne_Gesamtpreis(*args):
    try:
        anzahl = int(einladung_anzahl_entry.get())
        einladung_gesamtpreis = anzahl * Postkarteppp + Postkarte
        einladung_gesamtpreis_label.config(text=f"Gesamtpreis: {einladung_gesamtpreis} €")
        print("XX: anzahl, einladung_gesamtpreis:", anzahl, einladung_gesamtpreis, einladung_gesamtpreis_label)
    except ValueError:
        einladung_gesamtpreis_label.config(text="!!Fehler in berechne_Gesamtpreis!!")


# Budget für die Gestaltung Ausgabe 

def zeig_budget(*args):
    budget = design_limit_entry.get()
    budget_label.config(text=f"Budget für die Gestaltung: {budget} €")



root = tk.Tk()
root.title("Dropdown")

### Unterhaltung 

# Art der Unterhaltung Dropdown Optionen
unterhaltung_frame = tk.Frame(root)
unterhaltung_frame.pack(pady=5)

unterhaltung_label = tk.Label(unterhaltung_frame, text="Wählen Sie die Art der Unterhaltung:")
unterhaltung_label.pack()

unterhaltung_selected_option = tk.StringVar()
unterhaltung_selected_option.trace("w", on_unterhaltung_select)
options = ["DJ", "Barkeeper + Bar", "Keine"]
unterhaltung_dropdown = tk.OptionMenu(unterhaltung_frame, unterhaltung_selected_option, *options)
unterhaltung_dropdown.pack()

unterhaltung_preis_label = tk.Label(unterhaltung_frame, text="")
unterhaltung_preis_label.pack()


### Einladungen

# Art der Einladungen Dropdown Optionen
einladung_frame = tk.Frame(root)
einladung_frame.pack(pady=5)

einladung_label = tk.Label(einladung_frame, text="Möchten Sie Einladungen?")
einladung_label.pack()

selected_einladung_option = tk.StringVar()
selected_einladung_option.trace("w", on_einladung_select)
options = ["Ja, ich möchte eine Online Einladung als Email bestellen", "Ja, ich möchte Einladungen in gedruckter Form als Postkarte bestellen", "Nein, ich möchte keine Einladungen bestellen"]
einladung_dropdown = tk.OptionMenu(einladung_frame, selected_einladung_option, *options)
einladung_dropdown.pack()

einladung_preis_label = tk.Label(einladung_frame, text="")
einladung_preis_label.pack()


# Eingabefeld um die Einladungen zu beschränken (nur für gedruckte Postkarten)
einladung_anzahl_label = tk.Label(einladung_frame, text="Wie viele Einladungen möchten Sie bestellen?")
einladung_anzahl_entry = tk.Entry(einladung_frame)
einladung_anzahl_entry.configure(validate="key", validatecommand=(root.register(lambda char: char.isdigit()), '%S'))
einladung_anzahl_entry.bind("<KeyRelease>", berechne_Gesamtpreis)

# Initially hidden
einladung_anzahl_label.pack_forget()
einladung_anzahl_entry.pack_forget()

einladung_gesamtpreis_label = tk.Label(einladung_frame, text="")
einladung_gesamtpreis_label.pack()



### Gestaltung

# Eingabefeld für die Budgetbeschränkung der Gestaltung
design_limit_frame = tk.Frame(root)
design_limit_frame.pack(pady=5)

design_limit_label = tk.Label(design_limit_frame, text="Geben Sie Ihr Budget für die Gestaltung ein:")
design_limit_label.pack()

design_limit_entry = tk.Entry(design_limit_frame)
design_limit_entry.configure(validate="key", validatecommand=(root.register(lambda char: char.isdigit()), '%S'))
design_limit_entry.bind("<KeyRelease>", zeig_budget)
design_limit_entry.pack()

budget_label = tk.Label(design_limit_frame, text="")
budget_label.pack()



### Kostenvoranschlag berechnen





root.mainloop()
