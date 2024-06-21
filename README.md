# rxiv-types (v0.1.0)

<p align="center">
    <img src="https://img.shields.io/pypi/dm/rxiv-types?style=flat-square" />
    <img src="https://img.shields.io/pypi/l/rxiv-types?style=flat-square"/>
    <img src="https://img.shields.io/pypi/v/rxiv-types?style=flat-square"/>
    <a href="https://github.com/tefra/xsdata-pydantic">
        <img alt="Built with: xsdata-pydantic" src="https://img.shields.io/badge/Built%20with-xsdata--pydantic-blue">
    </a>
    <a href="https://github.com/dbrgn/coverage-badge">
        <img src="./images/coverage.svg">
    </a>
</p>

## Introduction

This package goal is to provide the Pydantic models for Drugbank schema files (XSD).


## Why do I need this?

Parsing XML on its own is challenging. Add to it the feature rich data inside of each
citation, and you will find yourself with hours or days of navigating the XML structure.

The approach here was to autogenerate Pydantic classes to parse the XML using the
`xsdata-pydantic` tool. This approach has the benefit of making sure every piece of data
is parsed properly, and an error is thrown if something is missing or incorrect. Instead
of using dictionaries to hold the data, Pydantic classes have the benefit of providing
type hints with tab completion for IDEs, making it easier to navigate the complex
structure of the citation data.

## How do I use it?
You can import the generated Pydantic models for drunbank schema files and use them 
to parse your drugbank XML files.

### Example 1: Parse ChemRxiv Data

```python
from pathlib import Path

import requests

from rxiv_types import chemrxiv_records

chemrxiv_url = "https://chemrxiv.org/engage/chemrxiv/public-api/v1/oai?verb=ListRecords&metadataPrefix=oai_dc&from=2000-01-01"

# 1. Get some chemrxiv data from the API
result = requests.get(chemrxiv_url)
destination = Path(f"downloads/data/chemrxiv.xml")
destination.parent.mkdir(parents=True, exist_ok=True)
with open(destination, "wb") as fw:
    fw.write(result.content)

# 2. Parse the data, and display the first article title
result = chemrxiv_records(destination)

# 3. Print some information about the first record
print("Paper 1:")
print(f"Title: {''.join(result.list_records.record[0].metadata.dc.title)}")
print(f"Authors: {'; '.join(result.list_records.record[0].metadata.dc.creator)}")
print(f"Abstract: {''.join(result.list_records.record[0].metadata.dc.description)}")
```

Output:
<!-- 
```bash
Paper 1:
Title: Excitonics: A universal set of binary gates for molecular exciton processing and signaling
Authors: Nicolas, Sawaya; Dmitrij, Rappoport; Daniel, Tabor; Alan, Aspuru-Guzik
Abstract: The ability to regulate energy transfer pathways through materials is an
 important goal of nanotechnology, as a greater degree of control is 
crucial for developing sensing, solar energy, and bioimaging 
applications. Such control necessitates a toolbox of actuation methods 
that can direct energy transfer based on user input. Here we propose a 
novel molecular exciton gate, analogous to a traditional transistor, for
 controlling exciton migration in chromophoric systems. The gate may be 
activated with an input of light or an input flow of excitons. Unlike 
previous gates and switches that control exciton transfer, our proposal 
does not require isomerization or molecular rearrangement, instead 
relying on excitation migration via the second singlet (S2) state of the
 gate molecule--hence the system is named an "S2 exciton gate." After 
presenting a set of system properties required for proper function of 
the S2 exciton gate, we show how one would overcome the two possible 
challenges: short-lived excited states and suppression of false 
positives. Precision and error rates are studied computationally in a 
model system with respect to excited-state decay rates and variations in
 molecular orientation. Finally, we demonstrate that the S2 exciton gate
 gate can be used to produce binary logical AND, OR, and NOT operations,
 providing a universal excitonic computation platform with a range of 
potential applications, including e.g. in signal processing for 
microscopy.
``` -->

<!-- 
### Why are the return structures so complicated?

The return structures are a direct reflection of the XML format defined by OAI and any
customizations from the hosting preprint servers. In the future some utility classes
might be made for common components (title, authors, etc), but for now this is intended
to be an unbiased way of parsing the XML. -->
