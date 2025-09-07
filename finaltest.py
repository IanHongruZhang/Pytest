from unittest.mock import Mock
from order import Order
from payment_processor import PaymentProcessor
from inventory import Inventory

# 测试支付后库存更新
def test_order_payment_and_inventory_update():
    # 模拟支付处理
    mock_payment_processor = Mock(spec=PaymentProcessor)
    mock_payment_processor.process_payment.return_value = True

    # 创建订单和库存
    order = Order(order_id=1, amount=100)
    inventory = Inventory()

    # 支付成功
    order.process_payment(mock_payment_processor)

    # 模拟库存更新
    inventory.update_stock('item_1', 5)

    # 验证支付后订单状态
    assert order.status == 'paid'
    # 验证库存是否更新
    assert inventory.stock['item_1'] == 5