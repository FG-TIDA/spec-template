# Starting a specification in a TIDA Working Group

This guide explains how a TIDA Working Group (WG) creates and publishes a
specification using the TIDA specification template. No prior Sphinx or
reStructuredText experience is required — you edit text files and push, and the
site and PDF are built for you.

## How TIDA organises specifications

- **One GitHub organization per Working Group**, for example `fg-tida-wg1`. The
  central `FG-TIDA` organization holds only the shared templates
  (`FG-TIDA/wg-charter-template` and `FG-TIDA/spec-template`).
- **Each specification is its own repository**, created from
  `FG-TIDA/spec-template` inside the Working Group's organization: one repo per
  document, each with its own web page, PDF, issues, and history.
- **Repositories follow the naming convention** `wg<n>-<acronym>-<spec-name>`,
  where `<n>` is the Working Group number and `<acronym>` is its acronym — for
  example `wg1-ra-aai`, `wg1-ra-trust-framework`. The Working Group's charter
  repository uses `wg<n>-<acronym>-charter`.

A WG that wants a single landing page listing all its specs can use the
`profile/README.md` of its organization's `.github` repository.

## Create a new specification (once per spec)

1. Go to **https://github.com/FG-TIDA/spec-template**.
2. Click **Use this template → Create a new repository**.
3. Set **Owner** to your Working Group's organization (for example `fg-tida-wg1`,
   **not** the central `FG-TIDA` organization) and **Repository name** to
   `wg<n>-<acronym>-<spec-name>` (for example `wg1-ra-aai`). Make it **Public**.
4. Click **Create repository**.
5. In the new repository, go to **Settings → Pages** and set
   **Source** to **GitHub Actions**.

That is all the setup. Every push to the `main` branch now rebuilds the site and
PDF automatically and publishes them to:

> `https://fg-tida-wg<n>.github.io/wg<n>-<acronym>-<spec-name>/`

The downloadable PDF is at `…/specification.pdf`.

## Fill in your specification

The document content lives under `src/doc/`. Edit these, replacing the
`<placeholders>` and the *lorem ipsum* example text with your own content.

**1. The front matter and document identity — `src/doc/index.rst`**

Replace the placeholders on the landing page:

| Placeholder | Put your… |
| --- | --- |
| `<acronym>` | short document identifier |
| `<title>` | full document title |
| `<subtitle of this document>` | subtitle / one-line summary |
| `<version>`, `<date>` | version and date in the History table |
| author name / affiliation / e-mail | authors in the Authors table |

Also fill in the **Abstract**, **Keywords** and **Foreword** sections, and edit
the **History** and **Authors** tables.

**2. The document metadata — `src/doc/conf.py`** (near the top)

Set `project`, `release`, `author`, `copyright` and the `cover_*` values
(these appear on the PDF cover and in the page/tab title).

**3. The chapters — `src/doc/chapters/`**

The template ships with example chapters that both **explain and demonstrate**
how to write content — text, lists, tables, figures, diagrams, cross-references,
and an auto-generated API reference. Read them in the built site, then replace
their content with your specification. Add or remove chapters by editing the
`toctree` in `index.rst`.

To document an API, put your OpenAPI (Swagger 3.0) file in `src/doc/yaml/` and
follow the pattern in `chapters/04_chapter4/`.

## Preview your changes

- **Easiest:** just push to `main` and read the published site — nothing to
  install.
- **Locally (optional):** see `CONTRIBUTING.md` in the repository for building on your
  own machine with a live preview.

## Getting help

- Read the template's own chapters — they are written as a tutorial.
- See `CONTRIBUTING.md` for build details and the customisation rules.
- Open an issue in your spec's repository for content questions, or in
  `FG-TIDA/spec-template` for template/tooling issues.
