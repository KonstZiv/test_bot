from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2022-11-25T20:17:48:123803"
VERSION = "0.91.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    def run():
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
