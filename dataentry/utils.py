from django.apps import apps


def get_all_custom_models():
    default_models = ['ContentType', 'Session', 'LogEntry', 'Permission', 'Group', 'User', 'Upload']
    custom_model = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_model.append(model.__name__)
    return custom_model
