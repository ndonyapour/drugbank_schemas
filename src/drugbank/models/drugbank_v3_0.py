from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from xsdata_pydantic.fields import field

__NAMESPACE__ = "http://drugbank.ca"


class BondActionsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    action: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


class DrugTypeType(Enum):
    SMALL_MOLECULE = "small molecule"
    BIOTECH = "biotech"


class EmptyStringType(Enum):
    VALUE = ""


class IdentifiersType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    external_identifier: List["IdentifiersType.ExternalIdentifier"] = field(
        default_factory=list,
        metadata={
            "name": "external-identifier",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )

    class ExternalIdentifier(BaseModel):
        model_config = ConfigDict(defer_build=True)
        resource: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://drugbank.ca",
                "required": True,
            }
        )
        identifier: str = field(
            metadata={
                "type": "Element",
                "namespace": "http://drugbank.ca",
                "required": True,
            }
        )


class PropertyTypeKind(Enum):
    LOG_P = "logP"
    LOG_S = "logS"
    LOG_P_HYDROPHOBICITY = "logP/hydrophobicity"
    WATER_SOLUBILITY = "Water Solubility"
    CACO2_PERMEABILITY = "caco2 Permeability"
    P_KA_STRONGEST_ACIDIC = "pKa (strongest acidic)"
    P_KA_STRONGEST_BASIC = "pKa (strongest basic)"
    IUPAC_NAME = "IUPAC Name"
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
    PHYSIOLOGICAL_CHARGE = "Physiological Charge"


class PropertyTypeSource(Enum):
    JCHEM = "JChem"
    ALOGPS = "ALOGPS"
    VALUE = ""


class SequenceType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    chain: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )


class SynonymsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    synonym: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


class TargetBondTypeKnownAction(Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


class AffectedOrganisms(BaseModel):
    class Meta:
        name = "affected-organisms"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    affected_organism: List[str] = field(
        default_factory=list,
        metadata={
            "name": "affected-organism",
            "type": "Element",
        },
    )


class AhfsCodes(BaseModel):
    class Meta:
        name = "ahfs-codes"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    ahfs_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ahfs-code",
            "type": "Element",
        },
    )


class AtcCodes(BaseModel):
    class Meta:
        name = "atc-codes"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    atc_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "atc-code",
            "type": "Element",
        },
    )


class Brands(BaseModel):
    class Meta:
        name = "brands"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    brand: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Categories(BaseModel):
    class Meta:
        name = "categories"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    category: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Cost(BaseModel):
    class Meta:
        name = "cost"
        namespace = "http://drugbank.ca"

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


class Dosage(BaseModel):
    class Meta:
        name = "dosage"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    form: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    route: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    strength: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class DrugInteraction(BaseModel):
    class Meta:
        name = "drug-interaction"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    drug: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class EssentialityValue(Enum):
    ESSENTIAL = "Essential"
    NON_ESSENTIAL = "Non-Essential"


class ExternalLink(BaseModel):
    class Meta:
        name = "external-link"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    resource: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    url: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class FoodInteractions(BaseModel):
    class Meta:
        name = "food-interactions"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    food_interaction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "food-interaction",
            "type": "Element",
        },
    )


class GoClassifier(BaseModel):
    class Meta:
        name = "go-classifier"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    category: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class GroupsGroup(Enum):
    APPROVED = "approved"
    ILLICIT = "illicit"
    EXPERIMENTAL = "experimental"
    WITHDRAWN = "withdrawn"
    NUTRACEUTICAL = "nutraceutical"


class Manufacturer(BaseModel):
    class Meta:
        name = "manufacturer"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    generic: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Mixture(BaseModel):
    class Meta:
        name = "mixture"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ingredients: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Packager(BaseModel):
    class Meta:
        name = "packager"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    url: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Patent(BaseModel):
    class Meta:
        name = "patent"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    number: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    country: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    approved: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    expires: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Pfam(BaseModel):
    class Meta:
        name = "pfam"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    identifier: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Salts(BaseModel):
    class Meta:
        name = "salts"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    salt: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class SecondaryAccessionNumbers(BaseModel):
    class Meta:
        name = "secondary-accession-numbers"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    secondary_accession_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "secondary-accession-number",
            "type": "Element",
        },
    )


class SpeciesCategory(Enum):
    HUMAN = "human"
    BACTERIAL = "bacterial"
    FUNGAL = "fungal"
    VIRAL = "viral"
    PARASITIC = "parasitic"


class Substructure(BaseModel):
    class Meta:
        name = "substructure"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    class_value: str = field(
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        }
    )


class BondType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    actions: BondActionsType = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    partner: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PropertyType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    kind: PropertyTypeKind = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    source: PropertyTypeSource = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )


class Dosages(BaseModel):
    class Meta:
        name = "dosages"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    dosage: List[Dosage] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class DrugInteractions(BaseModel):
    class Meta:
        name = "drug-interactions"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    drug_interaction: List[DrugInteraction] = field(
        default_factory=list,
        metadata={
            "name": "drug-interaction",
            "type": "Element",
        },
    )


class Essentiality(BaseModel):
    class Meta:
        name = "essentiality"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    value: EssentialityValue = field()


class ExternalLinks(BaseModel):
    class Meta:
        name = "external-links"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    external_link: List[ExternalLink] = field(
        default_factory=list,
        metadata={
            "name": "external-link",
            "type": "Element",
        },
    )


class GoClassifiers(BaseModel):
    class Meta:
        name = "go-classifiers"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    go_classifier: List[GoClassifier] = field(
        default_factory=list,
        metadata={
            "name": "go-classifier",
            "type": "Element",
        },
    )


class Groups(BaseModel):
    class Meta:
        name = "groups"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    group: List[GroupsGroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Manufacturers(BaseModel):
    class Meta:
        name = "manufacturers"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    manufacturer: List[Manufacturer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Mixtures(BaseModel):
    class Meta:
        name = "mixtures"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    mixture: List[Mixture] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Packagers(BaseModel):
    class Meta:
        name = "packagers"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    packager: List[Packager] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Patents(BaseModel):
    class Meta:
        name = "patents"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    patent: List[Patent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Pfams(BaseModel):
    class Meta:
        name = "pfams"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    pfam: List[Pfam] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Price(BaseModel):
    class Meta:
        name = "price"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    description: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cost: Cost = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    unit: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class ProteinSequences(BaseModel):
    class Meta:
        name = "protein-sequences"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    protein_sequence: List[SequenceType] = field(
        default_factory=list,
        metadata={
            "name": "protein-sequence",
            "type": "Element",
        },
    )


class Species(BaseModel):
    class Meta:
        name = "species"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    category: Optional[SpeciesCategory] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    uniprot_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "uniprot-name",
            "type": "Element",
        },
    )
    uniprot_taxon_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "uniprot-taxon-id",
            "type": "Element",
        },
    )


class Substructures(BaseModel):
    class Meta:
        name = "substructures"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    substructure: List[Substructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class PartnerType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    general_function: str = field(
        metadata={
            "name": "general-function",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    specific_function: str = field(
        metadata={
            "name": "specific-function",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    gene_name: str = field(
        metadata={
            "name": "gene-name",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    locus: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    reaction: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    signals: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    cellular_location: str = field(
        metadata={
            "name": "cellular-location",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    transmembrane_regions: str = field(
        metadata={
            "name": "transmembrane-regions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    theoretical_pi: Union[Decimal, EmptyStringType] = field(
        metadata={
            "name": "theoretical-pi",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    molecular_weight: str = field(
        metadata={
            "name": "molecular-weight",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    chromosome: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    species: Species = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    essentiality: Essentiality = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    references: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    external_identifiers: IdentifiersType = field(
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    synonyms: SynonymsType = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    protein_sequence: Optional[SequenceType] = field(
        default=None,
        metadata={
            "name": "protein-sequence",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    gene_sequence: Optional[SequenceType] = field(
        default=None,
        metadata={
            "name": "gene-sequence",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    pfams: Pfams = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    go_classifiers: GoClassifiers = field(
        metadata={
            "name": "go-classifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    id: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class PropertiesType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    property: List[PropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )


class TargetBondType(BondType):
    model_config = ConfigDict(defer_build=True)
    known_action: TargetBondTypeKnownAction = field(
        metadata={
            "name": "known-action",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )


class Carriers(BaseModel):
    class Meta:
        name = "carriers"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    carrier: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Enzymes(BaseModel):
    class Meta:
        name = "enzymes"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    enzyme: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Prices(BaseModel):
    class Meta:
        name = "prices"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    price: List[Price] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Taxonomy(BaseModel):
    class Meta:
        name = "taxonomy"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    kingdom: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    substructures: Substructures = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class Transporters(BaseModel):
    class Meta:
        name = "transporters"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    transporter: List[BondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class Targets(BaseModel):
    class Meta:
        name = "targets"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    target: List[TargetBondType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


class DrugType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    drugbank_id: str = field(
        metadata={
            "name": "drugbank-id",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    cas_number: str = field(
        metadata={
            "name": "cas-number",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    general_references: str = field(
        metadata={
            "name": "general-references",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    synthesis_reference: str = field(
        metadata={
            "name": "synthesis-reference",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    indication: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    pharmacology: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    mechanism_of_action: str = field(
        metadata={
            "name": "mechanism-of-action",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    toxicity: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    biotransformation: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    absorption: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    half_life: str = field(
        metadata={
            "name": "half-life",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    protein_binding: str = field(
        metadata={
            "name": "protein-binding",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    route_of_elimination: str = field(
        metadata={
            "name": "route-of-elimination",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    volume_of_distribution: str = field(
        metadata={
            "name": "volume-of-distribution",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    clearance: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    secondary_accession_numbers: SecondaryAccessionNumbers = field(
        metadata={
            "name": "secondary-accession-numbers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    groups: Groups = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    taxonomy: Taxonomy = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    synonyms: SynonymsType = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    salts: Salts = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    brands: Brands = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    mixtures: Mixtures = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    packagers: Packagers = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    manufacturers: Manufacturers = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    prices: Prices = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    categories: Categories = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    affected_organisms: AffectedOrganisms = field(
        metadata={
            "name": "affected-organisms",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    dosages: Dosages = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    atc_codes: AtcCodes = field(
        metadata={
            "name": "atc-codes",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    ahfs_codes: AhfsCodes = field(
        metadata={
            "name": "ahfs-codes",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    patents: Patents = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    food_interactions: FoodInteractions = field(
        metadata={
            "name": "food-interactions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    drug_interactions: DrugInteractions = field(
        metadata={
            "name": "drug-interactions",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    protein_sequences: Optional[ProteinSequences] = field(
        default=None,
        metadata={
            "name": "protein-sequences",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    calculated_properties: Optional[PropertiesType] = field(
        default=None,
        metadata={
            "name": "calculated-properties",
            "type": "Element",
            "namespace": "http://drugbank.ca",
        },
    )
    experimental_properties: PropertiesType = field(
        metadata={
            "name": "experimental-properties",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    external_identifiers: IdentifiersType = field(
        metadata={
            "name": "external-identifiers",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    external_links: ExternalLinks = field(
        metadata={
            "name": "external-links",
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    targets: Targets = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    enzymes: Enzymes = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    transporters: Transporters = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
            "required": True,
        }
    )
    carriers: Carriers = field(
        metadata={
            "type": "Element",
            "namespace": "http://drugbank.ca",
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
    updated: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    created: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Decimal = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Drugs(BaseModel):
    class Meta:
        name = "drugs"
        namespace = "http://drugbank.ca"

    model_config = ConfigDict(defer_build=True)
    drug: List[DrugType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    partners: "Drugs.Partners" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )

    class Partners(BaseModel):
        model_config = ConfigDict(defer_build=True)
        partner: List[PartnerType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
