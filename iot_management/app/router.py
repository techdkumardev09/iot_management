class TelemetryDataRouter:
    def db_for_read(self, model, **hints):
        print(model.__name__)
        if model._meta.app_label == 'app' and model.__name__ == 'TelemetryData':
            return 'timescaledb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app' and model.__name__ == 'TelemetryData':
            return 'timescaledb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None 

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'telemetrydata':
            return db == 'timescaledb'
        elif model_name == 'device':
            return db == 'default'
        return None
