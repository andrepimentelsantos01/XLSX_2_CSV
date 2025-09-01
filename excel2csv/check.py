import csv
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


def pick_csv() -> Path | None:
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="Selecione um arquivo CSV",
        filetypes=[("CSV", "*.csv"), ("Todos os arquivos", "*.*")]
    )
    root.destroy()
    return Path(path) if path else None


def main():
    csv_path = pick_csv()
    if not csv_path:
        print("Nenhum arquivo selecionado.")
        return

    try:
        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=";")
            rows = list(reader)
        print(f"Arquivo: {csv_path.name}")
        print(f"Total de linhas: {len(rows)}")
        print("Primeiras 10 linhas:")
        for r in rows[:10]:
            print(r)
        messagebox.showinfo("OK", f"Linhas lidas: {len(rows)} (mostradas 10 no console)")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        raise


if __name__ == "__main__":
    main()