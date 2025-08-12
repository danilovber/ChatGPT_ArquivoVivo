
from pathlib import Path
from datetime import datetime

# Caminho local do seu repositório
repo_path = Path(r"C:/CAMINHO/DO/SEU/REPOSITORIO")  # <-- ALTERE AQUI

def criar_indice_md(base_path: Path) -> str:
    linhas = ["# INDEX\n", f"_Última atualização: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n"]
    for pasta in sorted(base_path.iterdir()):
        if pasta.is_dir():
            linhas.append(f"\n## {pasta.name}\n")
            for arquivo in sorted(pasta.glob("*.md")):
                nome = arquivo.stem
                if "_" in nome:
                    data, titulo = nome.split("_", 1)
                    link = arquivo.relative_to(base_path).as_posix()
                    linhas.append(f"- **{data}** — [{titulo}]({link})")
    return "\n".join(linhas)

if __name__ == "__main__":
    indice_md = criar_indice_md(repo_path)
    index_path = repo_path / "INDEX.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(indice_md)
    print(f"INDEX.md atualizado em: {index_path}")
