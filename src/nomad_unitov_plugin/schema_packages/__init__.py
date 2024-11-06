from nomad.config.models.plugins import SchemaPackageEntryPoint


class HySprintPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_unitov_plugin.schema_packages.unitov_package import m_package
        return m_package


hysprint_package = HySprintPackageEntryPoint(
    name='HySprint',
    description='Package for HZB HySprint Lab',
)

class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_unitov_plugin.schema_packages.schema_package import m_package
        return m_package


schema_package_entry_point = MySchemaPackageEntryPoint(
    name='SchemaHySprint',
    description='SchemaPackage for HZB HySprint Lab',
)


class MySolutionPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_unitov_plugin.schema_packages.solution import m_package

        return m_package


solution_entry_point = MySolutionPackageEntryPoint(
    name='SchemaHySprint',
    description='SchemaPackage for HZB HySprint Lab',
)