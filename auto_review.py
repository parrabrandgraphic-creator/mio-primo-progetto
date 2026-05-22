import subprocess

def ottieni_modifiche():
    """Legge le modifiche recenti al codice"""
    risultato = subprocess.run(
        ["git", "diff", "HEAD"],
        capture_output=True,
        text=True
    )
    return risultato.stdout

def analizza_con_claude(codice):
    """Passa il codice a Claude Code per l'analisi"""
    prompt = "Analyze these code changes and list: 1) potential bugs 2) possible improvements 3) what is done well. Here is the code: " + codice

    risultato = subprocess.run(
        ["claude.cmd", "-p", prompt],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return risultato.stdout

def main():
    print("📥 Leggo le modifiche al codice...")
    modifiche = ottieni_modifiche()

    if not modifiche:
        print("✅ Nessuna modifica trovata!")
        return

    print("🤖 Analizzo con Claude...")
    feedback = analizza_con_claude(modifiche)

    print("\n=== FEEDBACK DI CLAUDE ===")
    print(feedback)

if __name__ == "__main__":
    main()