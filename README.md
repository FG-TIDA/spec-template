# Specification Template

A turnkey template for writing technical **specifications** with
[Sphinx](https://www.sphinx-doc.org/). It bundles everything a spec author
needs — structured chapters, tables, diagrams, an auto-generated API reference,
and one-command publishing to the web and PDF — so you can start writing
content instead of wiring up tooling.

The published document is available at
<https://debora-com.github.io/CUTEspecs/>.

## Features

- **Web + PDF from one source** — the same content builds a modern HTML site and
  a print-ready PDF.
- **API reference from OpenAPI** — drop an OpenAPI (Swagger) file in `yaml/` and
  the endpoints, schemas, and examples are generated automatically.
- **Diagrams as text** — sequence, class, and other diagrams via
  [PlantUML](https://plantuml.com), kept in version control alongside the prose.
- **Self-documenting** — the template's own chapters explain and demonstrate the
  authoring system as you read them.
- **Automatic publishing** — pushing to `main` builds and deploys the site (and
  PDF) via GitHub Actions and GitHub Pages.

## Getting started

1. Create your own copy (use the green **Use this template** button on GitHub, or
   clone this repository).
2. Replace the `<placeholders>` and the *lorem ipsum* content with your own. The
   landing page (`src/doc/index.rst`) is the document's front matter; the content
   lives under `src/doc/chapters/`.
3. Read the built chapters — they explain how to write text, tables, diagrams,
   cross-references, and API references.
4. Build and preview locally (see the [HOWTO](HOWTO.md)), or just push to `main`
   and let GitHub Pages publish it.

## Building the documentation

Full instructions are in [HOWTO.md](HOWTO.md). In short:

```shell
pip install -r requirements.txt
sphinx-build -b html src/doc target/html
```

Diagrams require [PlantUML](https://plantuml.com/download); API reference
generation and PDF output need their respective tools, all covered in the HOWTO.

## Built on

This template stands on excellent open-source projects:

- [Sphinx](https://www.sphinx-doc.org/) — the documentation engine
- [Furo](https://github.com/pradyunsg/furo) — the HTML theme (MIT), with custom
  styling on top
- [sphinxcontrib-openapi](https://sphinxcontrib-openapi.readthedocs.io/),
  [sphinxcontrib-plantuml](https://github.com/sphinx-contrib/plantuml) — the API
  and diagram extensions

## License

Released under the [MIT License](LICENSE) — free to use, modify, and
distribute, including for your own specifications. The bundled dependencies keep
their own licenses (for example [Furo](https://github.com/pradyunsg/furo) is
MIT); preserve their notices when you redistribute.
