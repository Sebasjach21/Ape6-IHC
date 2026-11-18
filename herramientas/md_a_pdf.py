#!/usr/bin/env python3
"""Convierte archivos .md (títulos, tablas, listas, citas) a PDF A4 horizontal.

Uso:
    pip install pymupdf
    python herramientas/md_a_pdf.py Fase2-Pilotaje/Resumen_Metricas.md [otro.md ...]

Genera el .pdf junto a cada .md. Volver a ejecutarlo después de llenar el .md.
"""
import html
import re
import sys
from pathlib import Path

import pymupdf

CSS = """
body { font-family: sans-serif; font-size: 9pt; color: #111; }
h1 { font-size: 16pt; color: #1a3a6b; margin-bottom: 4pt; }
h2 { font-size: 12pt; color: #1a3a6b; margin-top: 12pt; margin-bottom: 3pt; }
h3 { font-size: 10pt; margin-top: 8pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0; }
th { background-color: #dfe7f5; font-weight: bold; text-align: left; }
th, td { border: 0.6pt solid #888; padding: 2pt 3pt; font-size: 8pt; }
blockquote { color: #444; margin-left: 8pt; border-left: 2pt solid #aaa; padding-left: 6pt; }
code { font-family: monospace; font-size: 8pt; }
p, li { margin: 2pt 0; }
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    return s


def md_a_html(md):
    out, tabla, lista = [], [], False
    lineas = md.splitlines()

    def cerrar_tabla():
        nonlocal tabla
        if not tabla:
            return
        filas = [[c.strip() for c in l.strip().strip("|").split("|")] for l in tabla]
        filas = [f for f in filas if not all(re.fullmatch(r":?-{2,}:?", c) for c in f)]
        h = "<table>"
        for i, f in enumerate(filas):
            tag = "th" if i == 0 else "td"
            celdas = [inline(c.replace("\\_", "_")) or "&nbsp;" for c in f]
            h += "<tr>" + "".join("<%s>%s</%s>" % (tag, c, tag) for c in celdas) + "</tr>"
        out.append(h + "</table>")
        tabla = []

    def cerrar_lista():
        nonlocal lista
        if lista:
            out.append("</ul>")
            lista = False

    for l in lineas:
        if l.strip().startswith("|"):
            cerrar_lista()
            tabla.append(l)
            continue
        cerrar_tabla()
        m = re.match(r"^(#{1,3})\s+(.*)", l)
        if m:
            cerrar_lista()
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif re.match(r"^\s*[-*]\s+", l):
            if not lista:
                out.append("<ul>")
                lista = True
            out.append("<li>" + inline(re.sub(r"^\s*[-*]\s+", "", l)) + "</li>")
        elif re.match(r"^\s*\d+\.\s+", l):
            cerrar_lista()
            out.append("<p>" + inline(l.strip()) + "</p>")
        elif l.startswith(">"):
            cerrar_lista()
            out.append("<blockquote>" + inline(l.lstrip("> ")) + "</blockquote>")
        elif l.strip() in ("---", "```", "```bash"):
            cerrar_lista()
        elif l.strip():
            cerrar_lista()
            out.append("<p>" + inline(l) + "</p>")
    cerrar_tabla()
    cerrar_lista()
    return "<body>" + "\n".join(out) + "</body>"


def convertir(md_path):
    md_path = Path(md_path)
    cuerpo = md_a_html(md_path.read_text(encoding="utf-8"))
    pdf_path = md_path.with_suffix(".pdf")
    mediabox = pymupdf.paper_rect("a4-l")
    where = mediabox + (30, 30, -30, -30)
    story = pymupdf.Story(html=cuerpo, user_css=CSS)
    writer = pymupdf.DocumentWriter(str(pdf_path))
    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
    writer.close()
    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for a in sys.argv[1:]:
        print("OK ->", convertir(a))
