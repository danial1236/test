import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import font as tkfont
from termcolor import colored

class Arbeitszeitrechner:
    def __init__(self, root):
        self.root = root
        self.root.title("Arbeitszeitrechner")

        # Schriftart erstellen
        self.custom_font = tkfont.Font(size=30)

        ################ das ist nur ein test für github danach kann man einfach diese linie ignorieren!#####################
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Anzahl der gearbeiteten Tage:", font=self.custom_font).grid(row=0, column=0, padx=10, pady=10)
        self.anzahl_tage_entry = tk.Entry(self.root, font=self.custom_font)
        self.anzahl_tage_entry.grid(row=0, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Bestätigen", font=self.custom_font, command=self.submit)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

    def submit(self):
        try:
            anzahl_tage = int(self.anzahl_tage_entry.get())
            arbeitsstunden_pro_tag = []

            for tag in range(1, anzahl_tage + 1):
                stunden = float(simpledialog.askstring("Arbeitsstunden eingeben", f"Arbeitsstunden für Tag {tag}:", parent=self.root))
                arbeitsstunden_pro_tag.append(stunden)

            self.show_results(arbeitsstunden_pro_tag)

        except ValueError:
            messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")

    def show_results(self, arbeitsstunden_pro_tag):
        volle_tage, halbe_tage = self.berechne_volle_halbe_tage(arbeitsstunden_pro_tag)

        ergebnis_fenster = tk.Toplevel(self.root)
        ergebnis_fenster.title("Ergebnisse")
        ergebnis_fenster.geometry("600x400")

        # Schriftart für Ergebnisse erstellen
        result_font = tkfont.Font(size=20)

        tk.Label(ergebnis_fenster, text=f"Sie haben insgesamt {volle_tage} volle Arbeitstage und {halbe_tage} halbe Arbeitstage.", font=result_font).pack()

        maximale_volle_tage = 140
        maximale_halbe_tage = 280

        verbleibende_volle_tage = maximale_volle_tage - volle_tage
        verbleibende_halbe_tage = maximale_halbe_tage - halbe_tage

        tk.Label(ergebnis_fenster, text=f"Verbleibende volle Arbeitstage: {verbleibende_volle_tage}", font=result_font).pack()
        tk.Label(ergebnis_fenster, text=f"Verbleibende halbe Arbeitstage: {verbleibende_halbe_tage}", font=result_font).pack()

    def berechne_volle_halbe_tage(self, arbeitsstunden_pro_tag):
        volle_tage = sum(1 for stunden in arbeitsstunden_pro_tag if stunden >= 8)
        halbe_tage = sum(1 for stunden in arbeitsstunden_pro_tag if 4 <= stunden < 8)

        return volle_tage, halbe_tage

def main():
    print(colored("Willkommen bei unserem Arbeitszeitrechner!\n", "green"))

    root = tk.Tk()
    app = Arbeitszeitrechner(root)
    root.mainloop()

if __name__ == "__main__":
    main()
