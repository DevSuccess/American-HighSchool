from django.shortcuts import render
from . import models


# Create your views here.
def get_src_content(iframe_html):
    start_index = iframe_html.find('src="') + 5
    end_index = iframe_html.find('"', start_index)
    src_content = iframe_html[start_index:end_index]
    return src_content


def base_context(request):
    addresses = models.AddressAHSM.objects.all()
    maps_values = [value.map for value in addresses]

    maps = [get_src_content(html) for html in maps_values]

    context = {
        'addresses_ahsm': addresses,
        'maps': maps
    }
    return context



def index(request):
    pass
