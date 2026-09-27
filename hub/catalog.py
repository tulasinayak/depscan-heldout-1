from lxml import etree


def read_items(stream, limit):
    items = []
    for _event, element in etree.iterparse(stream, events=("end",), tag="item"):
        items.append({
            "sku": (element.findtext("sku") or "").strip(),
            "name": (element.findtext("name") or "").strip(),
            "quantity": int(element.findtext("quantity") or 0),
        })
        element.clear()
        if len(items) >= limit:
            break
    return items
