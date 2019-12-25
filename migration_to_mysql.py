from import_export import resources
from tablib import Dataset
from callback.models import CallBack
from category.models import Category
from feedback.models import Feedback
from order.models import Order
from product.models import Product, ProductManager, Add, AddManager, Labels
from section.models import SharesSection, DocumentSection, HowToSection, \
              ContactSection, EmailSection, SocialSection, OrderSection, FooterSectionText, \
              Votes
from subscribers.models import Subscriber
from tag.models import Tag

MODELS_LIST = [
    CallBack,
    Category,
    Feedback,
    Order,
    Product,
    ProductManager,
    Add,
    AddManager,
    Labels,
    SharesSection,
    DocumentSection,
    HowToSection,
    ContactSection,
    EmailSection,
    SocialSection,
    OrderSection,
    FooterSectionText,
    Votes,
    Subscriber,
    Tag,
    ]

def resources_objects_factory(_model):
    class DynamicResource(resources.ModelResource):
        model_name = _model.__name__
        class Meta:
            model = _model
    #class Meta:
    #    model = model
    #DynamicResource.Meta = Meta
    print("Model Resource - %s - created" % _model)
    return DynamicResource()

def main():
    for model in MODELS_LIST:
        resource = resources_objects_factory(model)
        dataset = resource.export()
        with open('csv_files/%s.csv' % str(resource.model_name), 'w') as file:
            file.write(dataset.csv)


def import_data():
    for model in MODELS_LIST:
        resource = resources_objects_factory(model)
        dataset = Dataset()
        with open('csv_files/%s.csv' % str(resource.model_name), 'r') as file:
            imported_data = dataset.load(file.read())

        result = resource.import_data(imported_data, dry_run= True)

        if not result.has_errors():
            resource.import_data(dataset, dry_run= False)

if __name__ == "__main__":
    main()

"""
from migration_to_mysql import resources_objects_factory, MODELS_LIST
test_resource = resources_objects_factory(MODELS_LIST[0])
dataset = test_resource.export()
with open('%s.csv' % str(test_resource.model_name), 'w') as file:
    file.write(dataset.csv)


# import data
from migration_to_mysql import resources_objects_factory, MODELS_LIST
for model in MODELS_LIST:
    resource = resources_objects_factory(model)
    dataset = Dataset()
    with open('csv_files/%s.csv' % str(resource.model_name), 'r') as file:
        imported_data = dataset.load(file.read())

    result = resource.import_data(imported_data, dry_run= True)
    print(result.has_errors())

#    if not result.has_errors():
#        resource.import_data(dataset, dry_run= False)

"""
