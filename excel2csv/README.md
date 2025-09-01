# Excel → CSV Converter

Projeto simples em **Python** para converter planilhas Excel (`.xlsx`) em arquivos CSV, com escolha de delimitador e seleção de abas.

---

## 🚀 Como usar

### 1. Converter Excel em CSV
- Execute **`app.py`** (Run ▶ no VSCode ou `python app.py`).
- Escolha o arquivo `.xlsx`.
- Informe o delimitador (padrão `;`).
- Escolha a aba a exportar (ou `ALL` para exportar todas).
- O(s) arquivo(s) `.csv` serão criados na mesma pasta do Excel, com o padrão:
  ```
  <nome_do_excel>__<nome_da_aba>.csv
  ```

### 2. Conferir um CSV exportado
- Execute **`check.py`**.
- Escolha um `.csv` já exportado.
- O programa mostra no console as primeiras 10 linhas e a contagem total.

---

## 📂 Estrutura

```
excel2csv/
├─ app.py        # Script principal (Excel → CSV)
├─ check.py      # Script auxiliar (visualizar CSV)
├─ exemplos.xlsx # Exemplo opcional
└─ README.md     # Documentação
```

---

## 🛠️ Requisitos

- Python 3.10+ instalado  
- Biblioteca `openpyxl`:
  ```bash
  pip install openpyxl
  ```

---

## 💡 Observações

- Funciona apenas com arquivos `.xlsx` (Excel moderno).  
- Exporta todos os valores como texto (para máxima compatibilidade).  
- Encoding padrão do CSV: `utf-8-sig` (abre direto no Excel sem problemas de acentuação).  