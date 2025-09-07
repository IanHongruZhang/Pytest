from inventory import Inventory

# 测试库存更新
def test_inventory_update_success():
    inventory = Inventory()
    result = inventory.update_stock('item_1', 5)
    assert result is True
    assert inventory.stock['item_1'] == 5

# 测试库存不足
def test_inventory_update_failure():
    inventory = Inventory()
    result = inventory.update_stock('item_1', 15)  # 超过库存
    assert result is False
    assert inventory.stock['item_1'] == 10  # 库存保持不变