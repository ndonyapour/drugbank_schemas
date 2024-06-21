from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://www.drugbank.ca"


class ActionListType(BaseModel):
    class Meta:
        name = "action-list-type"

    model_config = ConfigDict(defer_build=True)
    action: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class AffectedOrganismListType(BaseModel):
    class Meta:
        name = "affected-organism-list-type"

    model_config = ConfigDict(defer_build=True)
    affected_organism: List[str] = field(
        default_factory=list,
        metadata={
            "name": "affected-organism",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class AhfsCodeListType(BaseModel):
    class Meta:
        name = "ahfs-code-list-type"

    model_config = ConfigDict(defer_build=True)
    ahfs_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ahfs-code",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class AtcCodeLevelType(BaseModel):
    class Meta:
        name = "atc-code-level-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    code: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class CalculatedPropertyKindType(Enum):
    LOG_P = "logP"
    LOG_S = "logS"
    WATER_SOLUBILITY = "Water Solubility"
    IUPAC_NAME = "IUPAC Name"
    TRADITIONAL_IUPAC_NAME = "Traditional IUPAC Name"
    MOLECULAR_WEIGHT = "Molecular Weight"
    MONOISOTOPIC_WEIGHT = "Monoisotopic Weight"
    SMILES = "SMILES"
    MOLECULAR_FORMULA = "Molecular Formula"
    IN_CH_I = "InChI"
    IN_CH_IKEY = "InChIKey"
    POLAR_SURFACE_AREA_PSA = "Polar Surface Area (PSA)"
    REFRACTIVITY = "Refractivity"
    POLARIZABILITY = "Polarizability"
    ROTATABLE_BOND_COUNT = "Rotatable Bond Count"
    H_BOND_ACCEPTOR_COUNT = "H Bond Acceptor Count"
    H_BOND_DONOR_COUNT = "H Bond Donor Count"
    P_KA_STRONGEST_ACIDIC = "pKa (strongest acidic)"
    P_KA_STRONGEST_BASIC = "pKa (strongest basic)"
    PHYSIOLOGICAL_CHARGE = "Physiological Charge"
    NUMBER_OF_RINGS = "Number of Rings"
    BIOAVAILABILITY = "Bioavailability"
    RULE_OF_FIVE = "Rule of Five"
    GHOSE_FILTER = "Ghose Filter"
    MDDR_LIKE_RULE = "MDDR-Like Rule"


class CalculatedPropertySourceType(Enum):
    CHEM_AXON = "ChemAxon"
    ALOGPS = "ALOGPS"


class CategoryType(BaseModel):
    class Meta:
        name = "category-type"

    model_config = ConfigDict(defer_build=True)
    category: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    mesh_id: str = field(
        metadata={
            "name": "mesh-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ClassificationType(BaseModel):
    """Drug classification is obtained from ClassyFire (http://classyfire.wishartlab.com)."""

    class Meta:
        name = "classification-type"

    model_config = ConfigDict(defer_build=True)
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    direct_parent: str = field(
        metadata={
            "name": "direct-parent",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    kingdom: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    superclass: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    class_value: str = field(
        metadata={
            "name": "class",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    subclass: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    alternative_parent: List[str] = field(
        default_factory=list,
        metadata={
            "name": "alternative-parent",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    substituent: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class DosageType(BaseModel):
    class Meta:
        name = "dosage-type"

    model_config = ConfigDict(defer_build=True)
    form: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    route: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    strength: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class DrugTypeType(Enum):
    SMALL_MOLECULE = "small molecule"
    BIOTECH = "biotech"


class DrugbankDrugIdType(BaseModel):
    """The DrugBank ID is used to uniquely identify a drug entry.

    There is a primary ID and several secondary IDs that come from older
    ID formats or merged entries.
    """

    class Meta:
        name = "drugbank-drug-id-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
            "pattern": r"DB[0-9]{5}|APRD[0-9]{5}|BIOD[0-9]{5}|BTD[0-9]{5}|EXPT[0-9]{5}|NUTR[0-9]{5}",
        },
    )
    primary: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class DrugbankMetaboliteIdType(BaseModel):
    """The metabolite DrugBank ID uniquely identifies a metabolite entry.

    Multiple IDs indicate a merged entry.
    """

    class Meta:
        name = "drugbank-metabolite-id-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
            "pattern": r"DBMET[0-9]{5}",
        },
    )
    primary: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class DrugbankSaltIdType(BaseModel):
    """The salt DrugBank ID uniquely identifies a salt entry.

    Multiple IDs indicate a merged entry.
    """

    class Meta:
        name = "drugbank-salt-id-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "white_space": "collapse",
            "pattern": r"DBSALT[0-9]{6}",
        },
    )
    primary: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


class ExperimentalPropertyKindType(Enum):
    WATER_SOLUBILITY = "Water Solubility"
    MELTING_POINT = "Melting Point"
    BOILING_POINT = "Boiling Point"
    LOG_P = "logP"
    LOG_S = "logS"
    HYDROPHOBICITY = "Hydrophobicity"
    ISOELECTRIC_POINT = "Isoelectric Point"
    CACO2_PERMEABILITY = "caco2 Permeability"
    P_KA = "pKa"
    MOLECULAR_WEIGHT = "Molecular Weight"
    MOLECULAR_FORMULA = "Molecular Formula"


class ExternalIdentifierResourceType(Enum):
    UNI_PROT_KB = "UniProtKB"
    WIKIPEDIA = "Wikipedia"
    CH_EBI = "ChEBI"
    PUB_CHEM_COMPOUND = "PubChem Compound"
    PUB_CHEM_SUBSTANCE = "PubChem Substance"
    DRUGS_PRODUCT_DATABASE_DPD = "Drugs Product Database (DPD)"
    KEGG_COMPOUND = "KEGG Compound"
    KEGG_DRUG = "KEGG Drug"
    CHEM_SPIDER = "ChemSpider"
    BINDING_DB = "BindingDB"
    NATIONAL_DRUG_CODE_DIRECTORY = "National Drug Code Directory"
    GEN_BANK = "GenBank"
    PHARM_GKB = "PharmGKB"
    PDB = "PDB"
    IUPHAR = "IUPHAR"
    GUIDE_TO_PHARMACOLOGY = "Guide to Pharmacology"


class ExternalLinkResourceType(Enum):
    RX_LIST = "RxList"
    PDRHEALTH = "PDRhealth"
    DRUGS_COM = "Drugs.com"


class FoodInteractionListType(BaseModel):
    class Meta:
        name = "food-interaction-list-type"

    model_config = ConfigDict(defer_build=True)
    food_interaction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "food-interaction",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class GoClassifierType(BaseModel):
    class Meta:
        name = "go-classifier-type"

    model_config = ConfigDict(defer_build=True)
    category: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class GroupType(Enum):
    """
    Drugs are grouped into a category like approved, experimental, illict.
    """

    APPROVED = "approved"
    ILLICIT = "illicit"
    EXPERIMENTAL = "experimental"
    WITHDRAWN = "withdrawn"
    NUTRACEUTICAL = "nutraceutical"
    INVESTIGATIONAL = "investigational"


class InternationalBrandType(BaseModel):
    class Meta:
        name = "international-brand-type"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    company: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class KnownActionType(Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


class ManufacturerType(BaseModel):
    class Meta:
        name = "manufacturer-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    generic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MixtureType(BaseModel):
    class Meta:
        name = "mixture-type"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    ingredients: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PackagerType(BaseModel):
    class Meta:
        name = "packager-type"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    url: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PatentType(BaseModel):
    class Meta:
        name = "patent-type"

    model_config = ConfigDict(defer_build=True)
    number: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    country: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    approved: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    expires: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PathwayEnzymeListType(BaseModel):
    class Meta:
        name = "pathway-enzyme-list-type"

    model_config = ConfigDict(defer_build=True)
    uniprot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uniprot-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PfamType(BaseModel):
    class Meta:
        name = "pfam-type"

    model_config = ConfigDict(defer_build=True)
    identifier: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PolypeptideExternalIdentifierResourceType(Enum):
    UNI_PROT_KB = "UniProtKB"
    UNI_PROT_ACCESSION = "UniProt Accession"
    HUGO_GENE_NOMENCLATURE_COMMITTEE_HGNC = (
        "HUGO Gene Nomenclature Committee (HGNC)"
    )
    HUMAN_PROTEIN_REFERENCE_DATABASE_HPRD = (
        "Human Protein Reference Database (HPRD)"
    )
    GEN_ATLAS = "GenAtlas"
    GENE_CARDS = "GeneCards"
    GEN_BANK_GENE_DATABASE = "GenBank Gene Database"
    GEN_BANK_PROTEIN_DATABASE = "GenBank Protein Database"
    CH_EMBL = "ChEMBL"
    IUPHAR = "IUPHAR"
    GUIDE_TO_PHARMACOLOGY = "Guide to Pharmacology"


class PolypeptideSynonymListType(BaseModel):
    class Meta:
        name = "polypeptide-synonym-list-type"

    model_config = ConfigDict(defer_build=True)
    synonym: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PriceType(BaseModel):
    """
    The price for the given drug in US or Canadian currency.
    """

    class Meta:
        name = "price-type"

    model_config = ConfigDict(defer_build=True)
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    cost: "PriceType.Cost" = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    unit: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )

    class Cost(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        currency: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


class ProductCountryType(Enum):
    """Drug products are currently only imported from the U.S.

    (FDA) and Canada (Canadian Drug Product Database, or DPD).
    """

    US = "US"
    CANADA = "Canada"


class ProductSourceType(Enum):
    """
    Drug products are currently only imported from the FDA and the Canadian Drug
    Product Database, or DPD.
    """

    FDA_NDC = "FDA NDC"
    DPD = "DPD"


class ReactionElementType(BaseModel):
    class Meta:
        name = "reaction-element-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: str = field(
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ReactionEnzymeType(BaseModel):
    class Meta:
        name = "reaction-enzyme-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: str = field(
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    uniprot_id: str = field(
        metadata={
            "name": "uniprot-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class SequenceListType(BaseModel):
    class Meta:
        name = "sequence-list-type"

    model_config = ConfigDict(defer_build=True)
    sequence: List["SequenceListType.Sequence"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )

    class Sequence(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        format: str = field(
            const=True,
            default="FASTA",
            metadata={
                "type": "Attribute",
            },
        )


class SequenceType(BaseModel):
    class Meta:
        name = "sequence-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    format: str = field(
        const=True,
        default="FASTA",
        metadata={
            "type": "Attribute",
        },
    )


class SnpAdverseDrugReactionType(BaseModel):
    class Meta:
        name = "snp-adverse-drug-reaction-type"

    model_config = ConfigDict(defer_build=True)
    protein_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "protein-name",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    gene_symbol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "gene-symbol",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    uniprot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uniprot-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    rs_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "rs-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    allele: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    adverse_reaction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "adverse-reaction",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    pubmed_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pubmed-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )


class SnpEffectType(BaseModel):
    class Meta:
        name = "snp-effect-type"

    model_config = ConfigDict(defer_build=True)
    protein_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "protein-name",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    gene_symbol: List[str] = field(
        default_factory=list,
        metadata={
            "name": "gene-symbol",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    uniprot_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "uniprot-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    rs_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "rs-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    allele: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    defining_change: List[str] = field(
        default_factory=list,
        metadata={
            "name": "defining-change",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )
    pubmed_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pubmed-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "sequence": 1,
        },
    )


class SynonymType(BaseModel):
    class Meta:
        name = "synonym-type"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    coder: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class AtcCodeType(BaseModel):
    class Meta:
        name = "atc-code-type"

    model_config = ConfigDict(defer_build=True)
    level: List[AtcCodeLevelType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "min_occurs": 4,
            "max_occurs": 4,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class CalculatedPropertyType(BaseModel):
    class Meta:
        name = "calculated-property-type"

    model_config = ConfigDict(defer_build=True)
    kind: CalculatedPropertyKindType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    source: CalculatedPropertySourceType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class CategoryListType(BaseModel):
    class Meta:
        name = "category-list-type"

    model_config = ConfigDict(defer_build=True)
    category: List[CategoryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class DosageListType(BaseModel):
    class Meta:
        name = "dosage-list-type"

    model_config = ConfigDict(defer_build=True)
    dosage: List[DosageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class DrugInteractionType(BaseModel):
    class Meta:
        name = "drug-interaction-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: DrugbankDrugIdType = field(
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ExperimentalPropertyType(BaseModel):
    class Meta:
        name = "experimental-property-type"

    model_config = ConfigDict(defer_build=True)
    kind: ExperimentalPropertyKindType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    source: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ExternalIdentifierType(BaseModel):
    class Meta:
        name = "external-identifier-type"

    model_config = ConfigDict(defer_build=True)
    resource: ExternalIdentifierResourceType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    identifier: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ExternalLinkType(BaseModel):
    class Meta:
        name = "external-link-type"

    model_config = ConfigDict(defer_build=True)
    resource: ExternalLinkResourceType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    url: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class GoClassifierListType(BaseModel):
    class Meta:
        name = "go-classifier-list-type"

    model_config = ConfigDict(defer_build=True)
    go_classifier: List[GoClassifierType] = field(
        default_factory=list,
        metadata={
            "name": "go-classifier",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class GroupListType(BaseModel):
    class Meta:
        name = "group-list-type"

    model_config = ConfigDict(defer_build=True)
    group: List[GroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "min_occurs": 1,
            "max_occurs": 6,
        },
    )


class InternationalBrandListType(BaseModel):
    class Meta:
        name = "international-brand-list-type"

    model_config = ConfigDict(defer_build=True)
    international_brand: List[InternationalBrandType] = field(
        default_factory=list,
        metadata={
            "name": "international-brand",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ManufacturerListType(BaseModel):
    class Meta:
        name = "manufacturer-list-type"

    model_config = ConfigDict(defer_build=True)
    manufacturer: List[ManufacturerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class MixtureListType(BaseModel):
    class Meta:
        name = "mixture-list-type"

    model_config = ConfigDict(defer_build=True)
    mixture: List[MixtureType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PackagerListType(BaseModel):
    class Meta:
        name = "packager-list-type"

    model_config = ConfigDict(defer_build=True)
    packager: List[PackagerType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PatentListType(BaseModel):
    class Meta:
        name = "patent-list-type"

    model_config = ConfigDict(defer_build=True)
    patent: List[PatentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PathwayDrugType(BaseModel):
    class Meta:
        name = "pathway-drug-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: DrugbankDrugIdType = field(
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PfamListType(BaseModel):
    class Meta:
        name = "pfam-list-type"

    model_config = ConfigDict(defer_build=True)
    pfam: List[PfamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PolypeptideExternalIdentifierType(BaseModel):
    class Meta:
        name = "polypeptide-external-identifier-type"

    model_config = ConfigDict(defer_build=True)
    resource: PolypeptideExternalIdentifierResourceType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    identifier: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PriceListType(BaseModel):
    class Meta:
        name = "price-list-type"

    model_config = ConfigDict(defer_build=True)
    price: List[PriceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ProductType(BaseModel):
    """
    :ivar name:
    :ivar ndc_id:
    :ivar ndc_product_code:
    :ivar dpd_id: DPD ID from the Canadian Drug Product Database. Only
        present for drugs that are marketed in Canada.
    :ivar started_marketing_on:
    :ivar ended_marketing_on:
    :ivar dosage_form:
    :ivar strength:
    :ivar route:
    :ivar fda_application_number:
    :ivar generic:
    :ivar over_the_counter:
    :ivar approved:
    :ivar country:
    :ivar source:
    """

    class Meta:
        name = "product-type"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    ndc_id: str = field(
        metadata={
            "name": "ndc-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    ndc_product_code: str = field(
        metadata={
            "name": "ndc-product-code",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    dpd_id: Optional[str] = field(
        metadata={
            "name": "dpd-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "nillable": True,
        }
    )
    started_marketing_on: str = field(
        metadata={
            "name": "started-marketing-on",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    ended_marketing_on: str = field(
        metadata={
            "name": "ended-marketing-on",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    dosage_form: str = field(
        metadata={
            "name": "dosage-form",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    strength: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    route: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    fda_application_number: str = field(
        metadata={
            "name": "fda-application-number",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    generic: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    over_the_counter: bool = field(
        metadata={
            "name": "over-the-counter",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    approved: bool = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    country: ProductCountryType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    source: ProductSourceType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class ReactionEnzymeListType(BaseModel):
    class Meta:
        name = "reaction-enzyme-list-type"

    model_config = ConfigDict(defer_build=True)
    enzyme: List[ReactionEnzymeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class SaltType(BaseModel):
    class Meta:
        name = "salt-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: List[DrugbankSaltIdType] = field(
        default_factory=list,
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    cas_number: str = field(
        metadata={
            "name": "cas-number",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    inchikey: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class SnpAdverseDrugReactionListType(BaseModel):
    class Meta:
        name = "snp-adverse-drug-reaction-list-type"

    model_config = ConfigDict(defer_build=True)
    reaction: List[SnpAdverseDrugReactionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class SnpEffectListType(BaseModel):
    class Meta:
        name = "snp-effect-list-type"

    model_config = ConfigDict(defer_build=True)
    effect: List[SnpEffectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class SynonymListType(BaseModel):
    class Meta:
        name = "synonym-list-type"

    model_config = ConfigDict(defer_build=True)
    synonym: List[SynonymType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class AtcCodeListType(BaseModel):
    class Meta:
        name = "atc-code-list-type"

    model_config = ConfigDict(defer_build=True)
    atc_code: List[AtcCodeType] = field(
        default_factory=list,
        metadata={
            "name": "atc-code",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class CalculatedPropertyListType(BaseModel):
    class Meta:
        name = "calculated-property-list-type"

    model_config = ConfigDict(defer_build=True)
    property: List[CalculatedPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class DrugInteractionListType(BaseModel):
    class Meta:
        name = "drug-interaction-list-type"

    model_config = ConfigDict(defer_build=True)
    drug_interaction: List[DrugInteractionType] = field(
        default_factory=list,
        metadata={
            "name": "drug-interaction",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ExperimentalPropertyListType(BaseModel):
    class Meta:
        name = "experimental-property-list-type"

    model_config = ConfigDict(defer_build=True)
    property: List[ExperimentalPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ExternalIdentifierListType(BaseModel):
    class Meta:
        name = "external-identifier-list-type"

    model_config = ConfigDict(defer_build=True)
    external_identifier: List[ExternalIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "external-identifier",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ExternalLinkListType(BaseModel):
    class Meta:
        name = "external-link-list-type"

    model_config = ConfigDict(defer_build=True)
    external_link: List[ExternalLinkType] = field(
        default_factory=list,
        metadata={
            "name": "external-link",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PathwayDrugListType(BaseModel):
    class Meta:
        name = "pathway-drug-list-type"

    model_config = ConfigDict(defer_build=True)
    drug: List[PathwayDrugType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "min_occurs": 1,
        },
    )


class PolypeptideExternalIdentifierListType(BaseModel):
    class Meta:
        name = "polypeptide-external-identifier-list-type"

    model_config = ConfigDict(defer_build=True)
    external_identifier: List[PolypeptideExternalIdentifierType] = field(
        default_factory=list,
        metadata={
            "name": "external-identifier",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ProductListType(BaseModel):
    class Meta:
        name = "product-list-type"

    model_config = ConfigDict(defer_build=True)
    product: List[ProductType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class ReactionType(BaseModel):
    class Meta:
        name = "reaction-type"

    model_config = ConfigDict(defer_build=True)
    sequence: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    left_element: ReactionElementType = field(
        metadata={
            "name": "left-element",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    right_element: ReactionElementType = field(
        metadata={
            "name": "right-element",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    enzymes: ReactionEnzymeListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class SaltListType(BaseModel):
    class Meta:
        name = "salt-list-type"

    model_config = ConfigDict(defer_build=True)
    salt: List[SaltType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PathwayType(BaseModel):
    class Meta:
        name = "pathway-type"

    model_config = ConfigDict(defer_build=True)
    smpdb_id: str = field(
        metadata={
            "name": "smpdb-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    drugs: PathwayDrugListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    enzymes: PathwayEnzymeListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )


class PolypeptideType(BaseModel):
    class Meta:
        name = "polypeptide-type"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    general_function: str = field(
        metadata={
            "name": "general-function",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    specific_function: str = field(
        metadata={
            "name": "specific-function",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    gene_name: str = field(
        metadata={
            "name": "gene-name",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    locus: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    cellular_location: str = field(
        metadata={
            "name": "cellular-location",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    transmembrane_regions: str = field(
        metadata={
            "name": "transmembrane-regions",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    signal_regions: str = field(
        metadata={
            "name": "signal-regions",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    theoretical_pi: str = field(
        metadata={
            "name": "theoretical-pi",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    molecular_weight: str = field(
        metadata={
            "name": "molecular-weight",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    chromosome_location: str = field(
        metadata={
            "name": "chromosome-location",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    organism: "PolypeptideType.Organism" = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    external_identifiers: PolypeptideExternalIdentifierListType = field(
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    synonyms: PolypeptideSynonymListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    amino_acid_sequence: SequenceType = field(
        metadata={
            "name": "amino-acid-sequence",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    gene_sequence: SequenceType = field(
        metadata={
            "name": "gene-sequence",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    pfams: PfamListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    go_classifiers: GoClassifierListType = field(
        metadata={
            "name": "go-classifiers",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    source: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    class Organism(BaseModel):
        model_config = ConfigDict(defer_build=True)
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        ncbi_taxonomy_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ncbi-taxonomy-id",
                "type": "Attribute",
            },
        )


class ReactionListType(BaseModel):
    class Meta:
        name = "reaction-list-type"

    model_config = ConfigDict(defer_build=True)
    reaction: List[ReactionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class CarrierType(BaseModel):
    class Meta:
        name = "carrier-type"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    organism: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    actions: ActionListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    known_action: KnownActionType = field(
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    polypeptide: List[PolypeptideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class EnzymeType(BaseModel):
    class Meta:
        name = "enzyme-type"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    organism: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    actions: ActionListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    known_action: KnownActionType = field(
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    polypeptide: List[PolypeptideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    inhibition_strength: str = field(
        metadata={
            "name": "inhibition-strength",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    induction_strength: str = field(
        metadata={
            "name": "induction-strength",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PathwayListType(BaseModel):
    class Meta:
        name = "pathway-list-type"

    model_config = ConfigDict(defer_build=True)
    pathway: List[PathwayType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class PolypeptideListType(BaseModel):
    class Meta:
        name = "polypeptide-list-type"

    model_config = ConfigDict(defer_build=True)
    polypeptide: List[PolypeptideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class TargetType(BaseModel):
    class Meta:
        name = "target-type"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    organism: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    actions: ActionListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    known_action: KnownActionType = field(
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    polypeptide: List[PolypeptideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class TransporterType(BaseModel):
    class Meta:
        name = "transporter-type"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    organism: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    actions: ActionListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    known_action: KnownActionType = field(
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    polypeptide: List[PolypeptideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class CarrierListType(BaseModel):
    class Meta:
        name = "carrier-list-type"

    model_config = ConfigDict(defer_build=True)
    carrier: List[CarrierType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class EnzymeListType(BaseModel):
    class Meta:
        name = "enzyme-list-type"

    model_config = ConfigDict(defer_build=True)
    enzyme: List[EnzymeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class TargetListType(BaseModel):
    class Meta:
        name = "target-list-type"

    model_config = ConfigDict(defer_build=True)
    target: List[TargetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class TransporterListType(BaseModel):
    class Meta:
        name = "transporter-list-type"

    model_config = ConfigDict(defer_build=True)
    transporter: List[TransporterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )


class DrugType(BaseModel):
    class Meta:
        name = "drug-type"

    model_config = ConfigDict(defer_build=True)
    drugbank_id: List[DrugbankDrugIdType] = field(
        default_factory=list,
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "min_occurs": 1,
        },
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    cas_number: str = field(
        metadata={
            "name": "cas-number",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    groups: GroupListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    general_references: str = field(
        metadata={
            "name": "general-references",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    synthesis_reference: str = field(
        metadata={
            "name": "synthesis-reference",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    indication: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    pharmacodynamics: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    mechanism_of_action: str = field(
        metadata={
            "name": "mechanism-of-action",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    toxicity: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    metabolism: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    absorption: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    half_life: str = field(
        metadata={
            "name": "half-life",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    protein_binding: str = field(
        metadata={
            "name": "protein-binding",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    route_of_elimination: str = field(
        metadata={
            "name": "route-of-elimination",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    volume_of_distribution: str = field(
        metadata={
            "name": "volume-of-distribution",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    clearance: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    classification: Optional[ClassificationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    salts: SaltListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    synonyms: SynonymListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    products: ProductListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    international_brands: InternationalBrandListType = field(
        metadata={
            "name": "international-brands",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    mixtures: MixtureListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    packagers: PackagerListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    manufacturers: ManufacturerListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    prices: PriceListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    categories: CategoryListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    affected_organisms: AffectedOrganismListType = field(
        metadata={
            "name": "affected-organisms",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    dosages: DosageListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    atc_codes: AtcCodeListType = field(
        metadata={
            "name": "atc-codes",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    ahfs_codes: AhfsCodeListType = field(
        metadata={
            "name": "ahfs-codes",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    patents: PatentListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    food_interactions: FoodInteractionListType = field(
        metadata={
            "name": "food-interactions",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    drug_interactions: DrugInteractionListType = field(
        metadata={
            "name": "drug-interactions",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    sequences: Optional[SequenceListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    calculated_properties: Optional[CalculatedPropertyListType] = field(
        default=None,
        metadata={
            "name": "calculated-properties",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
        },
    )
    experimental_properties: ExperimentalPropertyListType = field(
        metadata={
            "name": "experimental-properties",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    external_identifiers: ExternalIdentifierListType = field(
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    external_links: ExternalLinkListType = field(
        metadata={
            "name": "external-links",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    pathways: PathwayListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    reactions: ReactionListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    snp_effects: SnpEffectListType = field(
        metadata={
            "name": "snp-effects",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    snp_adverse_drug_reactions: SnpAdverseDrugReactionListType = field(
        metadata={
            "name": "snp-adverse-drug-reactions",
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    targets: TargetListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    enzymes: EnzymeListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    carriers: CarrierListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    transporters: TransporterListType = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "required": True,
        }
    )
    type_value: DrugTypeType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    created: XmlDate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    updated: XmlDate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class DrugbankType(BaseModel):
    """
    This is the root element type for the DrugBank database schema.

    :ivar drug:
    :ivar version: The DrugBank version for the exported XML file.
    :ivar exported_on: The date the XML file was exported.
    """

    class Meta:
        name = "drugbank-type"

    model_config = ConfigDict(defer_build=True)
    drug: List[DrugType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.drugbank.ca",
            "min_occurs": 1,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    exported_on: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "exported-on",
            "type": "Attribute",
        },
    )


class Drugbank(DrugbankType):
    """This is the root element for the DrugBank database schema.

    DrugBank is a database on drug and drug-targets.
    """

    class Meta:
        name = "drugbank"
        namespace = "http://www.drugbank.ca"

    model_config = ConfigDict(defer_build=True)
