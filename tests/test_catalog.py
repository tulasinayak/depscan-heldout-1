import io

from hub.catalog import read_items

SAMPLE = b"""<?xml version="1.0"?>
<catalog>
  <item><sku>A-1</sku><name>Widget</name><quantity>4</quantity></item>
  <item><sku>B-2</sku><name>Gadget</name><quantity>0</quantity></item>
</catalog>
"""


def test_read_items():
    items = read_items(io.BytesIO(SAMPLE), limit=10)
    assert [i["sku"] for i in items] == ["A-1", "B-2"]
    assert items[0]["quantity"] == 4


def test_limit():
    assert len(read_items(io.BytesIO(SAMPLE), limit=1)) == 1
