from django import template

register = template.Library()

class_converter = {
    "textinput": "textinput textInput",
    "fileinput": "fileinput fileUpload",
    "passwordinput": "textinput textInput",
    "select": "select selectInput"
}

@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"

@register.filter
def with_class(field):
    class_name = field.field.widget.__class__.__name__.lower()
    class_name = class_converter.get(class_name, class_name)
    if "class" in field.field.widget.attrs:
        class_name = ' '.join([class_name, field.field.widget.attrs['class']])
    field.field.widget.attrs['class'] = field.css_classes(extra_classes=class_name)
    return field
