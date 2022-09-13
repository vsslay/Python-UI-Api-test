class SqlService:

    def __init__(self, connection):
        self.connection = connection

    def execute_sql_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_orders_id_count(self):
        numbers_of_orders = self.execute_sql_query("SELECT COUNT(id) FROM lc_orders")[0][0]
        return numbers_of_orders
