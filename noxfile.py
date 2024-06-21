import subprocess
from contextlib import closing
from pathlib import Path

import nox


@nox.session
def generate_packages(session):
    session.install("requests", "xsdata-pydantic[cli,lxml,soap]")

    # Get the article schema
    base_path = Path("downloads/schemas")
    base_path.mkdir(exist_ok=True, parents=True)

    drugbank_schemas = {
        "v3.0": "http://go.drugbank.com/docs/drugbank_v3.0.xsd",
        "v4.1": "http://go.drugbank.com/docs/drugbank_v4.1.xsd",
        "v4.2": "http://go.drugbank.com/docs/drugbank_v4.2.xsd",
        "v4.3": "http://go.drugbank.com/docs/drugbank_v4.3.xsd",
        "v4.6": "http://go.drugbank.com/docs/drugbank_v4.6.xsd",
        "v5.0": "http://go.drugbank.com/docs/drugbank_v5.0.xsd",
        "latest": "http://go.drugbank.com/docs/drugbank.xsd"
    }

    for schema_version, schema_url in drugbank_schemas.items():
        try:
            # Run wget command to download the file
            result = subprocess.run(['wget', schema_url, '-O', base_path.joinpath(f"drugbank_{schema_version}.xsd")], 
                                    check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Downloaded drugbank_{schema_version}.xsd successfully.")
            print(result.stdout.decode())
        except subprocess.CalledProcessError as e:
            print(f"Failed to download drugbank_{schema_version}.xsd.")
            print(e.stderr.decode())
        
        # with closing(request.urlopen(schema_url)) as url:
        #     print(url)
        #     with open(base_path.joinpath(schema_version + ".xsd"), "wb") as fw:
        #         fw.write(url.read())

        # Generate the models
        session.run(
            "xsdata",
            f"downloads/schemas/drugbank_{schema_version}.xsd",
            "--output",
            "pydantic",
            "--package",
            f"src.drugbank.models",
            "--debug",
        )

    # Remove extraneous __init__ file
    Path("src/__init__.py").unlink()
