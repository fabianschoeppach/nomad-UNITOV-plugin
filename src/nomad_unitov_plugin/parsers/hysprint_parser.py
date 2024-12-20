#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from nomad.datamodel import EntryArchive
from nomad.parsing import MatchingParser

from nomad_unitov_plugin.schema_packages.unitov_package import (
    Unitov_JVmeasurement,
    Unitov_EQEmeasurement, 
    Unitov_SimpleMPPTracking,
    Unitov_Measurement
) #Removed all other imports


from baseclasses.helper.utilities import set_sample_reference, create_archive, get_entry_id_from_file_name, get_reference
from nomad.datamodel.data import (
    EntryData,
)
from nomad.metainfo import (
    Quantity,
)
from nomad.datamodel.metainfo.basesections import (
    Entity,
)
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)

import os
import datetime

'''
This is a hello world style example for an example parser/converter.
'''


class RawFileHZB(EntryData):
    processed_archive = Quantity(
        type=Entity,
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
        )
    )


class HySprintParser(MatchingParser):

    def parse(self, mainfile: str, archive: EntryArchive, logger):
        # Log a hello world, just to get us started. TODO remove from an actual parser.

        mainfile_split = os.path.basename(mainfile).split('.')
        notes = ''
        if len(mainfile_split) > 2:
            notes = ".".join(mainfile_split[1:-2])
        measurment_type = mainfile_split[-2].lower()
        entry = Unitov_Measurement()
        if mainfile_split[-1] == "txt" and measurment_type == "jv":
            entry = Unitov_JVmeasurement()
        # if mainfile_split[-1] == "txt" and measurment_type == "spv":
        #     entry = HySprint_trSPVmeasurement()
        # if mainfile_split[-1] == "txt" and measurment_type == "eqe":
        #     entry = Unitov_EQEmeasurement()
        # if mainfile_split[-1] in ["tif", "tiff"] and measurment_type.lower() == "sem":
        #     entry = HySprint_SEM()
        #     entry.detector_data = [os.path.basename(mainfile)]
        # if measurment_type == "pl":
        #     entry = HySprint_PLmeasurement()
        # if measurment_type == "pli":
        #     entry = HySprint_PLImaging()
        # if measurment_type == "xrd" and mainfile_split[-1] == "xy":
        #     entry = HySprint_XRD_XY()
        # if measurment_type == "uvvis":
        #     entry = HySprint_UVvismeasurement()
        #     entry.data_file = [os.path.basename(mainfile)]
        # if mainfile_split[-1] in ["txt"] and measurment_type == "env":
        #     entry = HZB_EnvironmentMeasurement()
        # if mainfile_split[-1] in ["nk"]:
        #     entry = HZB_NKData()

        if mainfile_split[-1] in ["txt"] and measurment_type == "mppt":
            entry = Unitov_SimpleMPPTracking()
        archive.metadata.entry_name = os.path.basename(mainfile)

        # if not mainfile_split[-1] in ["nk"]:
        #     search_id = mainfile_split[0]
        #     set_sample_reference(archive, entry, search_id)

        #     entry.name = f"{search_id} {notes}"
        #     entry.description = f"Notes from file name: {notes}"

        # if not measurment_type in ["uvvis", "sem", "SEM"]:
        #     entry.data_file = os.path.basename(mainfile)
        entry.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        file_name = f'{os.path.basename(mainfile)}.archive.json'
        eid = get_entry_id_from_file_name(file_name, archive)
        archive.data = RawFileHZB(processed_archive=get_reference(archive.metadata.upload_id, eid))
        create_archive(entry, archive, file_name)
