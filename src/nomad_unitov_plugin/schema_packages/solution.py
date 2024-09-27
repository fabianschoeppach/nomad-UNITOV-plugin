from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config

# from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage
from nomad_material_processing.solution.general import Solution

configuration = config.get_plugin_entry_point(
    "nomad_unitov_plugin.schema_packages:solution_entry_point"
)

m_package = SchemaPackage()


class UNITOVSolution(Solution):
    # name = Quantity(
    #     type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    # )
    message = Quantity(type=str)

    def normalize(self, archive: "EntryArchive", logger: "BoundLogger") -> None:
        super().normalize(archive, logger)

        logger.info("Normalizing UNITOVSolution")
        self.message = f"Hello {self.name}!"


m_package.__init_metainfo__()
