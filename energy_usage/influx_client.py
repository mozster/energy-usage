from influxdb import InfluxDBClient


class InfluxClient:
    def __init__(self, server, port, database, username, password):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password

        self.client = InfluxDBClient(
            host=self.server,
            port=self.port,
            database=self.database,
            username=self.username,
            password=self.password)

    def write_points(self, body):
        self.client.write_points(body)
