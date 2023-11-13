from pathlib import Path

BASE_PATH = Path("/Users/alexandre/Downloads")

TYPE_FILE = {
    ".mp3" : "Musique",
    ".wav" : "Musique",
    ".flac" : "Musique",
    ".avi" : "Videos",
    ".mp4" : "Videos",
    ".gif" : "Videos",
    ".bmp" : "Images",
    ".png" : "Images",
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".txt" : "Documents",
    ".docx" : "Documents",
    ".pptx" : "Documents",
    ".csv" : "Documents",
    ".xls" : "Documents",
    ".odp" : "Documents",
    ".pages" : "Documents",
    "autre" : "Divers"}


files = [f for f in BASE_PATH.iterdir()if f.is_file()]

for file in files:
    extension = file.suffix
    dossier_cible = TYPE_FILE.get(extension, "Divers")
    dossier_cible_final = BASE_PATH / dossier_cible
    dossier_cible_final.mkdir(exist_ok=True)
    fichier_cible = dossier_cible_final / file.name
    file.rename(fichier_cible)
