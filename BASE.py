import os
import time
import chromadb
from chromadb.utils import embedding_functions
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURAÇÕES ---
# Coloque o caminho da sua pasta de notas do Obsidian abaixo
PATH_OBSIDIAN = os.path.expanduser("~/Documents/Obsidian") 
DB_PATH = "./vector_db_memoria"

# Modelo neural leve (roda liso no notebook)
emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Inicializa o banco de dados
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection(name="meu_reflexo", embedding_function=emb_fn)

def processar_arquivo(caminho):
    if not caminho.endswith(".md"): return
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            texto = f.read()
            if len(texto.strip()) > 5:
                nome_id = os.path.basename(caminho)
                # Upsert: se a nota já existe, ele atualiza a memória
                collection.upsert(
                    documents=[texto],
                    metadatas=[{"fonte": nome_id}],
                    ids=[nome_id]
                )
                print(f"🧠 Memória Sincronizada: {nome_id}")
    except Exception as e:
        print(f"❌ Erro ao processar: {e}")

# Monitor de alterações em tempo real
class ObsidianHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory: processar_arquivo(event.src_path)
    def on_created(self, event):
        if not event.is_directory: processar_arquivo(event.src_path)

if __name__ == "__main__":
    # Escaneia tudo na primeira vez
    print("🔄 Sincronizando seu Obsidian com seu cérebro digital...")
    for root, _, files in os.walk(PATH_OBSIDIAN):
        for f in files: processar_arquivo(os.path.join(root, f))
    
    # Inicia o monitoramento
    observer = Observer()
    observer.schedule(ObsidianHandler(), PATH_OBSIDIAN, recursive=True)
    observer.start()
    print(f"🚀 Sistema Ativo! Monitorando: {PATH_OBSIDIAN}")
    
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()