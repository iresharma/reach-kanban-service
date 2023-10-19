from playhouse.migrate import *

reach_db = PostgresqlDatabase("reach-systems")
migrator = PostgresqlMigrator(reach_db)

migrate(
    migrator.alter_column_type('item', 'desc', TextField()),
    migrator.alter_column_type('comment', 'message', TextField())
)