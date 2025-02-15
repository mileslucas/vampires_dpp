import os
from datetime import date

from pkg_resources import DistributionNotFound, get_distribution

from vampires_dpp.cli.dpp import (
    calib_parser,
    new_parser,
    run_parser,
    sort_parser,
    table_parser,
)
from vampires_dpp.pipeline.templates import (
    VAMPIRES_PDI,
    VAMPIRES_SDI,
    VAMPIRES_SINGLECAM,
)

# -- Project information -----------------------------------------------------
try:
    __version__ = get_distribution("vampires_dpp").version
except DistributionNotFound:
    __version__ = "unknown version"

# The full version, including alpha/beta/rc tags
version = __version__
release = __version__

project = "vampires_dpp"
author = "Miles Lucas"
# get current year
current_year = date.today().year
years = range(2022, current_year + 1)
copyright = f"{', '.join(map(str, years))}, {author}"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "myst_nb",
]
myst_enable_extensions = ["dollarmath", "substitution"]

singlecam_toml = f"""
<details>
<summary>Single-cam example</summary>

```toml
{VAMPIRES_SINGLECAM.to_toml()}
```
</details>
"""
pdi_toml = f"""
<details>
<summary>PDI example</summary>

```toml
{VAMPIRES_PDI.to_toml()}
```
</details>
"""
sdi_toml = f"""
<details>
<summary>H-alpha example</summary>

```toml
{VAMPIRES_SDI.to_toml()}
```
</details>
"""

myst_substitutions = {
    "dpprun_help": f"```\n{run_parser.format_help()}```",
    "dppsort_help": f"```\n{sort_parser.format_help()}```",
    "dppnew_help": f"```\n{new_parser.format_help()}```",
    "dppcalib_help": f"```\n{calib_parser.format_help()}```",
    "dpptable_help": f"```\n{table_parser.format_help()}```",
    "singlecam_toml": singlecam_toml,
    "pdi_toml": pdi_toml,
    "sdi_toml": sdi_toml,
}
myst_heading_anchors = 2
source_suffix = {".rst": "restructuredtext", ".md": "myst-nb", ".ipynb": "myst-nb"}
nb_execution_mode = "cache"
nb_execution_show_tb = os.environ.get("CI", "false") == "true"
nb_execution_timeout = 600

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_typehints = "description"
autodoc_typehints_format = "short"

# -- Options for HTML output -------------------------------------------------

html_theme = "alabaster"
html_static_path = ["_static"]
html_title = "VAMPIRES DPP"
html_theme = "sphinx_book_theme"
html_logo = "scexao_logo.svg"
html_theme_options = {
    "github_url": "https://github.com/scexao-org/vampires_dpp",
    "repository_url": "https://github.com/scexao-org/vampires_dpp",
    "use_repository_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_fullscreen_button": False,
}
