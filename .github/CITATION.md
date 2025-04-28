<!-- BEGIN LiminalCognition LLC CITATION.MD V0.0.1 BLOCK -->

# 📖 How to Cite {{ project_name }}

If you use **{{ project_name }}** in your work or publications, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/{{ zenodo_doi_badge_id }}.svg)](https://doi.org/{{ zenodo_doi_number }})

{{ author_name }} ({{ year }}, {{ month }}). **{{ paper_title }}**. {{ publisher_name }}. [https://doi.org/{{ zenodo_doi_number }}](https://doi.org/{{ zenodo_doi_number }})

---

## 📚 BibTeX Citation

```bibtex
@misc{ {{ citation_key }},
  author       = { {{ author_name }} },
  title        = { {{ paper_title }} },
  month        = {{ month_abbreviation }},
  year         = {{ year }},
  doi          = { {{ zenodo_doi_number }} },
  url          = { https://doi.org/{{ zenodo_doi_number }} }
}
```

---

# 🛠️ Template Fields Explained

| Placeholder | Meaning |
|:------------|:--------|
| `{{ project_name }}` | The name of your software/project |
| `{{ zenodo_doi_badge_id }}` | The Zenodo badge identifier (e.g., `{doi}`) |
| `{{ zenodo_doi_number }}` | The DOI itself (same as above without splitting) |
| `{{ author_name }}` | Author's full name |
| `{{ year }}` | Year of publication |
| `{{ month }}` | Full month (e.g., March) |
| `{{ month_abbreviation }}` | Short month (`mar`, `apr`, etc.) for BibTeX |
| `{{ paper_title }}` | Full title of the software, publication, or paper |
| `{{ publisher_name }}` | Organization hosting the record (e.g., Zenodo) |
| `{{ citation_key }}` | The BibTeX identifier (e.g., `wiechman_2016`) |

---

# ✨ Example Filled In (your original version)

```markdown
# 📖 How to Cite Re-Frame

If you use **Re-Frame** in your work or publications, please cite it as follows:

[![DOI](https://zenodo.org/badge/DOI/{doi}.svg)](https://doi.org/{doi})

Joshua Wiechman (2016, January). **Coder Plugin**. [https://doi.org/{doi}](https://doi.org/{doi})

---

## 📚 BibTeX Citation

```bibtex
@misc{wiechman_2016,
  author       = {Wiechman, Joshua},
  title        = {Coder Plugin},
  month        = jan,
  year         = 2016,
  doi          = {{doi}},
  url          = {https://doi.org/{doi}}
}

<!-- END LiminalCognition LLC CITATION.MD BLOCK -->
