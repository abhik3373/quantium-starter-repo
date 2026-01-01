import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app
from dash import html, dcc


def find_component(component, component_type):
    if isinstance(component, component_type):
        return True
    if hasattr(component, "children"):
        children = component.children
        if isinstance(children, list):
            return any(find_component(child, component_type) for child in children)
        else:
            return find_component(children, component_type)
    return False


# Test 1: Header is present
def test_header_present():
    layout = app.app.layout
    assert find_component(layout, html.H1)


# Test 2: Visualization (graph) is present
def test_graph_present():
    layout = app.app.layout
    assert find_component(layout, dcc.Graph)


# Test 3: Region picker (radio buttons) is present
def test_region_picker_present():
    layout = app.app.layout
    assert find_component(layout, dcc.RadioItems)
